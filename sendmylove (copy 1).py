import sys
import time

def run_liric():
    # Global Config
    default_typing_speed = 0.08 #type speed in terminal
    def_sleep = 0 #default sleep time = 0
    
    # Format: (Liric, Delay row, Speed row)
    lines = [
        ("No one's gotta know, just us and the moon", 0.1, 0.06), # fast
        ("Till the sun starts waking", 0.8, 0.06),
        ("", 0.2, 0), #  null, delay row
        ("Up's the only direction I see", 1.0, 0.15), # slow/Deep
        ("As long as we keep this", 0.5, 0.15),
        ("", 0.2, 0),
        ("Low, low, low, low, low, low, low, lowkey", 0.5, 0.05), #fast+
        ("(Ah-ah-ah-ah-ah, ah-ah-ah-ah-ah)", 0.8, 0.1),
        ("You ain't even gotta lo-, lo-, lo-, lo-, lo-, lo-, lo-, love me", 1.0, 0.07),
    ]

    print("--- Lowkey (NIKI) - Terminal Version ---\n")
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
