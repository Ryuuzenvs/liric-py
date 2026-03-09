import sys
import time

def run_liric():
    # Global Config
    default_typing_speed = 0.08 #type speed in terminal
    def_sleep = 5 #default sleep time = 0
#    def_sleep = 0 #default sleep time = 0
    
    # Format: (Lirik, Delay row, Speed row)
    lines = [
        ("Genggam", 0.6, 0.3),
        ("Tanganku, sa. . . . .yang", 1.5, 0.07),
        ("Kota ini tak sama tanpamu", 3, 0.09),
        ("Masih rasa ingin lagi", 0.8, 0.1),
        ("Habiskan waktu di sini", 0.8, 0.13),
        ("Mungkin tiga atau empat hari lagi . . . . .", 0.7, 0.1),
    ]

    print("--- kota ini tak sama tanpamu (Nadhif Basalamah) ---\n")
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
