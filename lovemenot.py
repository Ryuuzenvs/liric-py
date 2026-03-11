import sys
import time

def run_liric():
    # Global Config
    default_typing_speed = 0.8
    def_sleep = 0.9
    
    # Format: (Lirik, Jeda antar baris, Kecepatan ketik)
    lines = [
        ("Wake up in the morning, everything's alright", 1.0, 0.06),
        ("At the end of the story . . . you're holdin' me tight", 1.4, 0.06),
        ("I don't need to worry, am I out of my mind?", 0.5, 0.06),
        ("And, oh, it's hard to see you,", 0.1, 0.05),
        ("But I wish you were right here", 0.3, 0.04),
        ("Oh, it's hard to leave you", 0.3, 0.05),
        ("When I get you everywhere", 0.6, 0.06),
        ("All this time I'm thinking,", 0.3, 0.06),
        ("I'm strong enough to sink it", 0.8, 0.06),
        ("Oh, no, I don't need you,", 0.5, 0.06),
        ("But I miss you, come here", 2.0, 0.07),
    ]

    print(f"{'='*10} Love Me Not (Laufey) {'='*10}\n")
    time.sleep(def_sleep) 

    for baris, pause, speed in lines:
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
