import tkinter as tk
from tkinter import messagebox # Import messagebox for displaying alerts

class CelsiusFahrenheitConverter:
    def __init__(self, master):
        self.master = master
        master.title("C-F Converter")
        master.geometry("300x150") # Set initial window size
        master.resizable(False, False) # Make window not resizable

        # Configure grid for better layout
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        # 1. Celsius Input Label and Entry
        self.celsius_label = tk.Label(master, text="Celsius:")
        self.celsius_label.grid(row=0, column=0, padx=10, pady=5, sticky="e") # Align to east

        self.celsius_entry = tk.Entry(master, width=15)
        self.celsius_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w") # Align to west
        self.celsius_entry.focus_set() # Set focus to this entry when the app starts

        # 2. Convert Button
        self.convert_button = tk.Button(master, text="Convert to Fahrenheit", command=self.convert_temperature)
        self.convert_button.grid(row=1, column=0, columnspan=2, pady=10) # Span across two columns

        # 3. Fahrenheit Output Label
        self.fahrenheit_label = tk.Label(master, text="Fahrenheit: ")
        self.fahrenheit_label.grid(row=2, column=0, columnspan=2, pady=5) # Span across two columns

    def convert_temperature(self):
        """
        Converts the Celsius temperature entered by the user to Fahrenheit
        and displays the result. Handles non-numeric input.
        """
        try:
            celsius_str = self.celsius_entry.get()
            if not celsius_str: # Check if the input is empty
                messagebox.showwarning("Input Error", "Please enter a Celsius value.")
                return

            celsius_value = float(celsius_str)
            fahrenheit_value = (celsius_value * 9/5) + 32
            self.fahrenheit_label.config(text=f"Fahrenheit: {fahrenheit_value:.2f}°F")
        except ValueError:
            # Display an error message if the input is not a valid number
            messagebox.showerror("Input Error", "Please enter a valid number for Celsius.")
        except Exception as e:
            # Catch any other unexpected errors
            messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

# Main part of the program
if __name__ == "__main__":
    root = tk.Tk() # Create the main window
    app = CelsiusFahrenheitConverter(root) # Create an instance of our converter app
    root.mainloop() # Start the Tkinter event loop
