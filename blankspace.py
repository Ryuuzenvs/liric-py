import sys
import time

def run_liric():
    # Global Config
    default_typing_speed = 0.08 #type speed in terminal
    def_sleep = 5 #default sleep time = 0
    
    # Format: (Lirik, Delay row, Speed row)
    lines = [
        ("So it's gonna be forever", 0.6, 0.07),
        ("Or it's gonna go down in flames", 0.5, 0.07),
        ("You can tell me when it's over", 0.5, 0.06),
        ("If the high was worth the pain", 1.0, 0.07),
        ("Got a long list of ex-lovers", 0.5, 0.06),
        ("They'll tell you I'm insane", 0.5, 0.07),
        ("'Cause you know I love the players", 0.3, 0.06),
        ("And you love the game", 0.5, 0.08),
    ]

    print("--- blankspace (Taylor Swift) ---\n")
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
