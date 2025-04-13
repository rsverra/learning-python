import time
import os
import random
import sys
from tqdm import tqdm

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_type(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def fake_login():
    clear()
    slow_type("Welcome to Secure Terminal Access v1.0\n")
    username = input("Username: ")
    password = input("Password: ")
    slow_type("\nAuthenticating", 0.1)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
    time.sleep(1)
    print("\nAccess Granted! Welcome, Agent", username)
    time.sleep(1)

def matrix_effect(duration=2):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ''.join(random.choice(chars) for _ in range(60))
        print("\033[92m" + line + "\033[0m")
        time.sleep(0.05)

def fake_command(command, duration=2):
    slow_type(f"\n> {command}", 0.05)
    fake_progress(f"Executing '{command}'", duration)

def fake_progress(task, seconds):
    print(f"[+] {task}")
    for _ in tqdm(range(100)):
        time.sleep(seconds / 100)
    print("[✓] Done!\n")

def hacking_sequence():
    commands = [
        "nmap -sS 192.168.1.1",
        "ping -c 4 10.0.0.1",
        "ssh root@target.com",
        "brute_force --target password.txt",
        "scp data.txt agent@localhost:/secured"
    ]
    for cmd in commands:
        fake_command(cmd, random.uniform(1.5, 3))

def fake_shutdown():
    slow_type("\n[!] SYSTEM WARNING: Unauthorized access detected.", 0.05)
    for i in range(5, 0, -1):
        print(f"System will shut down in {i} seconds...")
        time.sleep(1)
    slow_type("System terminated.", 0.1)

# ==== MAIN ====
def main():
    fake_login()
    clear()
    matrix_effect(3)
    hacking_sequence()
    slow_type("\nAccessing top secret files...", 0.04)
    time.sleep(1)
    slow_type("Files successfully extracted to /root/secret/ 🗂️", 0.04)
    fake_shutdown()

if __name__ == "__main__":
    main()
