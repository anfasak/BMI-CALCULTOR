import tkinter as tk
from tkinter import messagebox, ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if measurement_combobox.get() == "Metric (kg, cm)":
            height /= 100  # Convert cm to meters
        elif measurement_combobox.get() == "Imperial (lbs, inches)":
            weight *= 0.453592  # Convert pounds to kg
            height *= 0.0254  # Convert inches to meters
        else:
            raise ValueError("Please select a measurement system.")

        age = int(age_entry.get())
        gender = gender_combobox.get()

        if height <= 0 or weight <= 0 or age <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Calculate healthy weight range
        healthy_weight_range = (18.5 * (height * 2), 24.9 * (height * 2))

        # Create a formatted result string
        result = (
            "==============================\n"
            "          BMI RESULT          \n"
            "==============================\n"
            f" Gender: {gender}\n"
            f" Age: {age} years\n"
            f" Weight: {weight:.2f} kg\n"
            f" Height: {height * 100:.2f} cm\n"
            f" Your BMI: {bmi:.2f}\n"
            f" Category: {category}\n"
            f" Healthy Weight Range: {healthy_weight_range[0]:.2f} kg - {healthy_weight_range[1]:.2f} kg\n"
            "==============================\n"
        )

        show_result(result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight, height, age, and select a measurement system.")

def show_result(result):
    result_window = tk.Toplevel(root)
    result_window.title("BMI Result")
    result_window.geometry("400x400")
    result_window.config(bg="#F2EDEB")

    result_label = tk.Label(result_window, text=result, bg="#F2EDEB", font=("Arial", 12))
    result_label.pack(pady=20)

    ok_button = tk.Button(result_window, text="OK", command=result_window.destroy, bg="#00796b", fg="white", font=("Arial", 14))
    ok_button.pack(pady=20)

def reset_fields():
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    gender_combobox.set("Select Gender")
    measurement_combobox.set("Select Measurement")

# Create the main window
root = tk.Tk()
root.title("BMI CALCULATOR")
root.geometry("500x600")
root.config(bg="#F2EDEB")

# Heading
heading_label = tk.Label(root, text="BMI CALCULATOR", bg="#F2EDEB", font=("Arial", 24, "bold"))
heading_label.pack(pady=20)

# Frame for inputs
input_frame = tk.Frame(root, bg="#F2EDEB")
input_frame.pack(pady=10)

# Measurement selection
measurement_label = tk.Label(input_frame, text="Measurement System:", bg="#F2EDEB", font=("Arial", 14, "bold"))
measurement_label.grid(row=0, column=0, padx=10, pady=5)
measurement_combobox = ttk.Combobox(input_frame, values=["Metric (kg, cm)", "Imperial (lbs, inches)"], font=("Arial", 14))
measurement_combobox.grid(row=0, column=1, padx=10, pady=5)
measurement_combobox.set("Select Measurement")

# Age input
age_label = tk.Label(input_frame, text="Age (years):", bg="#F2EDEB", font=("Arial", 14, "bold"))
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(input_frame, font=("Arial", 14))
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Weight input
weight_label = tk.Label(input_frame, text="Weight:", bg="#F2EDEB", font=("Arial", 14, "bold"))
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(input_frame, font=("Arial", 14))
weight_entry.grid(row=2, column=1, padx=10, pady=5)

# Height input
height_label = tk.Label(input_frame, text="Height:", bg="#F2EDEB", font=("Arial", 14, "bold"))
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry = tk.Entry(input_frame, font=("Arial", 14))
height_entry.grid(row=3, column=1, padx=10, pady=5)

# Gender input
gender_label = tk.Label(input_frame, text="Gender:", bg="#F2EDEB", font=("Arial", 14, "bold"))
gender_label.grid(row=4, column=0, padx=10, pady=5)
gender_combobox = ttk.Combobox(input_frame, values=["Male", "Female", "Other"], font=("Arial", 14))
gender_combobox.grid(row=4, column=1, padx=10, pady=5)
gender_combobox.set("Select Gender")

# Create a canvas for the Calculate button
calc_canvas = tk.Canvas(root, width=200, height=50, bg="#F2EDEB", highlightthickness=0)
calc_canvas.pack(pady=20)

# Create the Calculate button
calc_button = calc_canvas.create_rectangle(0, 0, 200, 50, fill="#00796b", outline="#00796b", width=2)
calc_text = calc_canvas.create_text(100, 25, text="Calculate", fill="white", font=("Arial", 16, "bold"))

# Function to handle Calculate button click
def on_calculate_click(event):
    calculate_bmi()

# Bind the click event to the Calculate canvas
calc_canvas.bind("<Button-1>", on_calculate_click)

# Pop-up effect for Calculate button
def on_calculate_enter(event):
    calc_canvas.itemconfig(calc_text, font=("Arial", 18, "bold"))
    calc_canvas.itemconfig(calc_button, fill="#009688")
    calc_canvas.config(bg="#F2EDEB")

def on_calculate_leave(event):
    calc_canvas.itemconfig(calc_text, font=("Arial", 16, "bold"))
    calc_canvas.itemconfig(calc_button, fill="#00796b")

calc_canvas.bind("<Enter>", on_calculate_enter)
calc_canvas.bind("<Leave>", on_calculate_leave)

# Create a canvas for the Reset button
reset_canvas = tk.Canvas(root, width=200, height=50, bg="#F2EDEB", highlightthickness=0)
reset_canvas.pack(pady=10)

# Create the Reset button
reset_button = reset_canvas.create_rectangle(0, 0, 200, 50, fill="#f44336", outline="#f44336", width=2)
reset_text = reset_canvas.create_text(100, 25, text="Reset", fill="white", font=("Arial", 16, "bold"))

# Function to handle Reset button click
def on_reset_click(event):
    reset_fields()

# Bind the click event to the Reset canvas
reset_canvas.bind("<Button-1>", on_reset_click)

# Pop-up effect for Reset button
def on_reset_enter(event):
    reset_canvas.itemconfig(reset_text, font=("Arial", 18, "bold"))
    reset_canvas.itemconfig(reset_button, fill="#e57373")

def on_reset_leave(event):
    reset_canvas.itemconfig(reset_text, font=("Arial", 16, "bold"))
    reset_canvas.itemconfig(reset_button, fill="#f44336")

reset_canvas.bind("<Enter>", on_reset_enter)
reset_canvas.bind("<Leave>", on_reset_leave)

# Run the application
root.mainloop()
