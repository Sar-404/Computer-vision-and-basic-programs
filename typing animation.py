import time
alphabets=" abcdefghijklmnopqrstuvwxyz"
while True:
    message = input("\nEnter the message\n")
    done=""
    timer=0.02
    for i in message:
        if i.islower():
            for j in range(1, alphabets.index(i) + 1):
                print(f"\r{done + alphabets[j]}", end="", flush=True)
                time.sleep(timer)
        elif i.isupper():
            for j in range(1, alphabets.upper().index(i) + 1):
                print(f"\r{done + alphabets[j].upper()}", end="", flush=True)
                time.sleep(timer)
        else:
            print(f"\r{done + i}", end="", flush=True)
            time.sleep(timer*2)
        done = done + i
