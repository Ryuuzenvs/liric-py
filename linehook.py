import sys
import time

def run_liric():
    #config
    typing_speed = 0.08 
    lines = [
        ("Is it worth it?", 0.5),
        ("Is it worth it?", 0.5),
        ("Tell me, is it worth . . . . . . . it?", 1),
        ("Oh, baby, I am a wreck when I'm without you", 1.5),
        ("I need you here to stay", 1.5),
        ("Broke all my bones that day I found you", 1.5),
        ("Crying at the lake", 1.5),
    ]

    print("--- Line without a hook ---\n")
    time.sleep(0.5) 

    for baris, delay in lines:
        
        for huruf in baris:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(typing_speed)
        
        time.sleep(delay)
        print("") 

if __name__ == "__main__":
    try:
        run_liric()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")

