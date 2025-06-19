import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32

        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)
root.configure(bg="#e0f7fa")  # Set background color

# Widgets
tk.Label(root, text="Enter Temperature:", bg="#e0f7fa").pack(pady=5)
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

tk.Label(root, text="From:", bg="#e0f7fa").pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.current(0)
combo_from.pack()

tk.Label(root, text="To:", bg="#e0f7fa").pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.current(1)
combo_to.pack()

tk.Button(root, text="Convert", command=convert_temperature, bg="#b2ebf2").pack(pady=10)

label_result = tk.Label(root, text="Result: ", bg="#e0f7fa")
label_result.pack(pady=5)

# Run the GUI
root.mainloop()
