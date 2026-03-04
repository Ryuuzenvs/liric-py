import sys
import time

def run_liric():
    #config
    def_sleep = 0 #default sleep time = 0
    typing_speed = 0.35 #type speed in terminal
    lines = [
#        ("話したいことがたくさんあるよ", 0.5),
#        ("どんな話でも聞きたいよ", 0.5),
#        ("ほんの数秒も宝物で魔法になる", 0.3),
        ("淋しさはきっとあなたを想うため", 0.5),
        ("切なさはきっとここにある", 1.5),
        ("願いを叶えるための", 2.5),
        ("二人の約束", 1.5),
    ]

    print("--- A Promise (Aira Yuuki) ---\n")
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
