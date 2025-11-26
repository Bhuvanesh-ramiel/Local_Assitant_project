import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def confirm_and_run(action_name, func):
    result = messagebox.askyesno("Confirm", f"Do you really want to {action_name}?")
    if result:   # User clicked YES
        func()

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

commands = {
    "np": lambda: os.startfile("notepad.exe"),
    "cal": lambda: os.startfile("calc.exe"),
    "tm": lambda: os.startfile("taskmgr.exe"),
    "set": lambda: os.startfile("ms-settings.exe"),
    "control": lambda: os.startfile("control.exe"),

       # System (Protected with confirmation)
    "lock": lambda: confirm_and_run("lock your PC", 
               lambda: os.system("rundll32.exe user32.dll,LockWorkStation")),

    "sd": lambda: confirm_and_run("shutdown your PC", 
               lambda: os.system("shutdown /s /t 1")),

    "rs": lambda: confirm_and_run("restart your PC", 
               lambda: os.system("shutdown /r /t 1")),


    # Web shortcuts
    "yt": lambda: subprocess.Popen([chrome_path, "https://www.youtube.com"]),
    "gg": lambda: subprocess.Popen([chrome_path, "https://www.google.com"]),
    "gh": lambda: subprocess.Popen([chrome_path, "https://www.github.com"]),
    "ig": lambda: subprocess.Popen([chrome_path, "https://www.instagram.com"]),
    "ldn": lambda: subprocess.Popen([chrome_path, "https://www.Linkedin.com"]),     
}


def run_command():
    cmd = entry.get().strip().lower()
    entry.delete(0, tk.END)

    if cmd in commands:
        try:
            commands[cmd]()
            output_label.config(text=f"Executed: {cmd}", fg="lightgreen")
        except Exception as e:
            output_label.config(text=f"Error: {e}", fg="red")
    else:
        output_label.config(text="Unknown command", fg="red")


# --- GUI WINDOW ---
window = tk.Tk()
window.title("Nara")
window.geometry("250x150+1650+50")  # positioned near right edge (adjust based on your screen)
window.attributes('-topmost', True)  # always on top
window.resizable(True, True)

# ⭐ FIXED: Make window appear instantly
#window.lift()
#window.focus_force()
def fix_visibility():
    window.update_idletasks()

    # Screen and window geometry
    sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = 250, 150  # your known window size
    x = window.winfo_x()
    y = window.winfo_y()

    # Keep window inside screen boundaries
    if x < 0 or y < 0 or x + w > sw or y + h > sh:
        window.geometry(f"{w}x{h}+50+50")

    window.lift()
    window.focus_force()

window.after(50, fix_visibility)



# Frame
frame = tk.Frame(window, bg="#202020")
frame.pack(fill="both", expand=True)

# Text Entry
entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill="x")

# Button
run_btn = tk.Button(frame, text="Run", command=run_command, bg="#444", fg="white")
run_btn.pack(pady=5)

# Output label
output_label = tk.Label(frame, text="", bg="#202020", fg="white")
output_label.pack()

window.mainloop()
