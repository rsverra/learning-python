import tkinter as tk
import time
import threading
import random

# Fake command list
commands = [
    "nmap -A 192.168.0.1",
    "ssh root@192.168.0.101",
    "scp top_secret.txt agent@localhost:/",
    "brute_force -t admin",
    "ping -c 4 8.8.8.8",
    "decrypt --file=secret.enc"
]

# Main App
class HackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Terminal v1.0")
        self.root.geometry("600x400")
        self.root.configure(bg="black")

        self.login_frame = tk.Frame(self.root, bg="black")
        self.login_frame.pack(pady=80)

        self.username_label = tk.Label(self.login_frame, text="Username:", fg="lime", bg="black", font=("Courier", 12))
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame, font=("Courier", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Password:", fg="lime", bg="black", font=("Courier", 12))
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Courier", 12))
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.start_hacking, font=("Courier", 12))
        self.login_button.pack(pady=10)

    def start_hacking(self):
        self.login_frame.destroy()
        self.terminal = tk.Text(self.root, bg="black", fg="lime", font=("Courier", 10))
        self.terminal.pack(expand=True, fill="both")
        threading.Thread(target=self.hack_process).start()

    def type_text(self, text, delay=0.05):
        for char in text:
            self.terminal.insert(tk.END, char)
            self.terminal.see(tk.END)
            self.terminal.update()
            time.sleep(delay)
        self.terminal.insert(tk.END, "\n")

    def hack_process(self):
        self.type_text("Authenticating user...")
        time.sleep(1)
        self.type_text("Access granted. Welcome, Agent.\n")

        for cmd in commands:
            self.type_text(f"> {cmd}", 0.03)
            time.sleep(random.uniform(0.5, 1.2))
            self.type_text("Output: Success.\n", 0.01)

        self.type_text("Extracting data...")
        for i in range(3):
            file = f"data_{random.randint(1000,9999)}.zip"
            self.type_text(f"Downloading {file}...", 0.02)
            time.sleep(0.5)

        self.type_text("\n[!] SYSTEM BREACH DETECTED!")
        for i in range(5, 0, -1):
            self.type_text(f"Shutting down in {i}...", 0.2)

        self.type_text("System Terminated. Goodbye.")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = HackerApp(root)
    root.mainloop()
