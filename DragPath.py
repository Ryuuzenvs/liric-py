import sys
import time

def run_liric():
    #config
    def_sleep = 0.5 #default sleep time = 0
    typing_speed = 0.12 #type speed in terminal
    lines = [
        ("Can you, can you, can you, can you?", 1),
        ("A drag path", 0.5),
        ("etched in the surface", 0.5),
        ("As evidence", 0.8),
        ("I left there on purpose", 0.7),
        ("A sad sack", 0.5),
        ("laying on the surface", 0.5),
        ("Can you . . .find me . . .?", 1),
    ]

    print("--- Drag path ---\n")
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

