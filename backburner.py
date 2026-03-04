import sys
import time

def run_liric():
    #config
    typing_speed = 0.08 
    lines = [
        ("I’ll always be in your corner", 1),
        ("Cause I don’t feel alive ‘til I’m \nburning on your back . . . . . . . burner", 6),
        ("And I know that it’s sad that \nI settle for the back . . . . . . . burner", 7),
    ]

    print("--- Backburner (NIKI) ---\n")
    time.sleep(1) 

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
