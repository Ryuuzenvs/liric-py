import sys
import time

def run_liric():
    #config
    def_sleep = 0.06 # delay sebelum lirik pertama mulai
    typing_speed = 0.07 # kecepatan ngetik di terminal
    lines = [
        ("Know you're all", 0.6),
        ("that I want", 0.9),
        ("this life", 3.1),
        ("I'll imagine we fell in love ", 0.5),
        ("I'll nap under moonlight skies with you", 0.7),
        ("I think I'll picture us, you with the waves ", 0.3),
        ("The ocean's colors on your face . . . . .", 2.0),
    ]

    print("--- Blue - Yung Kai ---\n")
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
