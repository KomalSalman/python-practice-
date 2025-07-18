import tkinter as tk
from tkinter import messagebox

def calculate_age():
    try:
        # Get age from entry and convert to integer
        age = int(age_entry.get())
        
        if age <= 0:
            messagebox.showerror("Error", "Age must be a positive number")
            return
            
        # Perform calculations
        months = 12 * age
        weeks = 52 * age
        days = 365 * age
        hours = 24 * days
        minutes = 60 * hours
        seconds = 60 * minutes
        
        # Update result labels
        months_label.config(text=f"Months: {months:,}")
        weeks_label.config(text=f"Weeks: {weeks:,}")
        days_label.config(text=f"Days: {days:,}")
        hours_label.config(text=f"Hours: {hours:,}")
        minutes_label.config(text=f"Minutes: {minutes:,}")
        seconds_label.config(text=f"Seconds: {seconds:,}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age (whole number)")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Set a modern color scheme
bg_color = "#f0f0f0"
accent_color = "#4a6fa5"
root.configure(bg=bg_color)

# Create and place widgets
tk.Label(root, text="Age Calculator", font=("Arial", 18, "bold"), bg=bg_color, fg=accent_color).pack(pady=10)

tk.Label(root, text="Enter your age (years):", font=("Arial", 12), bg=bg_color).pack(pady=5)

age_entry = tk.Entry(root, font=("Arial", 12), justify="center")
age_entry.pack(pady=5)

calculate_btn = tk.Button(root, text="Calculate", command=calculate_age, 
                         bg=accent_color, fg="white", font=("Arial", 12))
calculate_btn.pack(pady=10)

# Frame for results
results_frame = tk.Frame(root, bg=bg_color)
results_frame.pack(pady=10)

# Result labels
months_label = tk.Label(results_frame, text="Months: ", font=("Arial", 11), bg=bg_color)
weeks_label = tk.Label(results_frame, text="Weeks: ", font=("Arial", 11), bg=bg_color)
days_label = tk.Label(results_frame, text="Days: ", font=("Arial", 11), bg=bg_color)
hours_label = tk.Label(results_frame, text="Hours: ", font=("Arial", 11), bg=bg_color)
minutes_label = tk.Label(results_frame, text="Minutes: ", font=("Arial", 11), bg=bg_color)
seconds_label = tk.Label(results_frame, text="Seconds: ", font=("Arial", 11), bg=bg_color)

# Grid layout for results
months_label.grid(row=0, column=0, sticky="w", padx=10, pady=2)
weeks_label.grid(row=1, column=0, sticky="w", padx=10, pady=2)
days_label.grid(row=2, column=0, sticky="w", padx=10, pady=2)
hours_label.grid(row=3, column=0, sticky="w", padx=10, pady=2)
minutes_label.grid(row=4, column=0, sticky="w", padx=10, pady=2)
seconds_label.grid(row=5, column=0, sticky="w", padx=10, pady=2)

# Run the application
root.mainloop()