import time
import os
import random
from tqdm import tqdm

def slow_type(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_progress(task, seconds):
    print(f"[+] {task}")
    for _ in tqdm(range(100)):
        time.sleep(seconds / 100)
    print("[✓] Done!\n")

def fake_hacking():
    clear_screen()
    slow_type("Starting terminal access...")
    time.sleep(1)
    
    fake_progress("Initializing hacking module", 1.5)
    fake_progress("Bypassing firewall", 2)
    fake_progress("Cracking password...", 3)
    fake_progress("Accessing secure server", 2)
    
    ip = f"192.168.{random.randint(10, 255)}.{random.randint(10, 255)}"
    slow_type(f"HACKED into system at IP: {ip}")
    time.sleep(1)

    slow_type("\nExtracting data...\n", 0.07)
    for i in range(5):
        filename = f"file_{random.randint(1000,9999)}.txt"
        slow_type(f"Downloading {filename}...", 0.04)
        time.sleep(0.3)
    
    slow_type("\n[!] System shutdown initiated...\n", 0.05)
    for i in range(5, 0, -1):
        slow_type(f"Shutting down in {i}...", 0.5)

    slow_type("Goodbye, Agent.", 0.1)

# Run
fake_hacking()
