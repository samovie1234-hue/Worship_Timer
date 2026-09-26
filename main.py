import tkinter as tk
from tkinter import messagebox

class WorshipTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Church Worship Countdown Timer")
        self.root.geometry("500x450")
        self.root.configure(bg="#1e1e2e")

        self.time_left = 0
        self.timer_running = False
        self.current_label = "Select an Item"

        # Header Label
        self.header_label = tk.Label(
            root, text="Worship Service Timer", font=("Segoe UI", 18, "bold"),
            fg="#f39c12", bg="#1e1e2e"
        )
        self.header_label.pack(pady=10)

        # Current Item Label
        self.status_label = tk.Label(
            root, text=self.current_label, font=("Segoe UI", 14),
            fg="#bdc3c7", bg="#1e1e2e"
        )
        self.status_label.pack(pady=5)

        # Big Timer Display
        self.timer_label = tk.Label(
            root, text="00:00", font=("Consolas", 60, "bold"),
            fg="#2ecc71", bg="#1e1e2e"
        )
        self.timer_label.pack(pady=15)

        # Service Item Buttons Frame
        preset_frame = tk.Frame(root, bg="#1e1e2e")
        preset_frame.pack(pady=10)

        presets = [
            ("Praise & Worship (20m)", "Praise & Worship", 20),
            ("Opening Prayer (5m)", "Opening Prayer", 5),
            ("Offering (7m)", "Offering", 7),
            ("The Word (35m)", "The Word", 35),
            ("Altar Call (10m)", "Altar Call", 10),
        ]

        for text, label, mins in presets:
            btn = tk.Button(
                preset_frame, text=text, font=("Segoe UI", 10),
                bg="#313244", fg="#ffffff", activebackground="#f39c12",
                command=lambda l=label, m=mins: self.set_preset(l, m)
            )
            btn.pack(fill="x", pady=2)

        # Control Buttons Frame
        control_frame = tk.Frame(root, bg="#1e1e2e")
        control_frame.pack(pady=15)

        start_btn = tk.Button(
            control_frame, text="Start / Resume", font=("Segoe UI", 11, "bold"),
            bg="#27ae60", fg="#ffffff", command=self.start_timer
        )
        start_btn.grid(row=0, column=0, padx=5)

        pause_btn = tk.Button(
            control_frame, text="Pause", font=("Segoe UI", 11, "bold"),
            bg="#f39c12", fg="#ffffff", command=self.pause_timer
        )
        pause_btn.grid(row=0, column=1, padx=5)

        reset_btn = tk.Button(
            control_frame, text="Reset", font=("Segoe UI", 11, "bold"),
            bg="#c0392b", fg="#ffffff", command=self.reset_timer
        )
        reset_btn.grid(row=0, column=2, padx=5)

    def update_display(self):
        mins, secs = divmod(self.time_left, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
        
        # Turn red during the last minute
        if self.time_left <= 60 and self.time_left > 0:
            self.timer_label.config(fg="#e74c3c")
        else:
            self.timer_label.config(fg="#2ecc71")

    def set_preset(self, label, minutes):
        self.pause_timer()
        self.current_label = f"Current Item: {label}"
        self.status_label.config(text=self.current_label)
        self.time_left = minutes * 60
        self.update_display()

    def start_timer(self):
        if not self.timer_running and self.time_left > 0:
            self.timer_running = True
            self.run_countdown()

    def run_countdown(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.root.after(1000, self.run_countdown)
        elif self.time_left == 0 and self.timer_running:
            self.timer_running = False
            self.status_label.config(text=f"{self.current_label} - Time Elapsed!")
            messagebox.showinfo("Time Up", "The timer for this service item has ended.")

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.pause_timer()
        self.time_left = 0
        self.status_label.config(text="Select an Item")
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = WorshipTimerApp(root)
    root.mainloop()
