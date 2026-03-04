import sys
import time

def run_liric():
    #config
    def_sleep = 0 #default sleep time = 0
    typing_speed = 0.08 #type speed in terminal
    lines = [
        ("Cause all . . .", 2.5),
        ("I need", 1.3),
        ("Is a beauty and a beat . . .", 1.5),
        ("Who can make my life complete . . . . . ", 2.5),
        ("It's all . . .", 2.3),
        ("'bout you", 1.5),
        ("When the music makes you move", 1),
        ("Baby, do it like you do . . . . .", 1),
    ]

    print("--- Beauty in a Beat ---\n")
    time.sleep(def_sleep) 

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
