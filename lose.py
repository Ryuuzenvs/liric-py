import sys
import time

def run_liric():
    # Global Config
    default_typing_speed = 0.08 #type speed in terminal
    def_sleep = 2 #default sleep time = 0
#    def_sleep = 0 #default sleep time = 0
    
    # Format: (Lirik, Delay row, Speed row)
    lines = [
        ("I know", 2, 0.2),
        ("We know better so", 0, 0.12),
        ("We'd both better go", 0, 0.1),
        ("I", 2, 0.09),
        ("Don't need a reason", 2.5, 0.09),
        ("To keep on dreaming", 3, 0.08),
        ("That we don't lose, yeah", 0, 0.09),
        ("What's the use?", 1.5, 0.09),
    ]

    print("--- Lose (Niki) ---\n")
    time.sleep(def_sleep) 

    for baris, pause, speed in lines:
        # use specific var,if 0 or None use default value
        current_speed = speed if speed > 0 else default_typing_speed
        
        for huruf in baris:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(current_speed)
        
        time.sleep(pause)
        print("") 

if __name__ == "__main__":
    try:
        run_liric()
    except KeyboardInterrupt:
        print("\n\n[!] Program dihentikan.")
