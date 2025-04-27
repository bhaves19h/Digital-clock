import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  # call this function again after 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Create label to show time
label = tk.Label(root, font=("Arial", 60), bg="black", fg="cyan")
label.pack(padx=20, pady=20)

update_time()  # call the function once
root.mainloop()  # start the app
