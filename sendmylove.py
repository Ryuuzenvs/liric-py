import sys
import time

def run_liric():
    #config
    def_sleep = 0 #default sleep time = 0
    typing_speed = 0.08 #type speed in terminal
    lines = [
        ("We've gotta let go of all of our ghosts", 0.5),
        ("We both know we ain't kids no more", 0.5),
        ("Send my love to your new lover", 0.7),
        ("Treat her better", 0.3),
        ("We've gotta let go of all of our ghosts", 0.5),
        ("We both know we ain't kids no more", 1.5),
    ]

    print("--- Send My Love (Adele) ---\n")
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
