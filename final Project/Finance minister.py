import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate():
    try:
        hourly_salary = float(entry.get())
        monthly_salary = hourly_salary * 8 * 5 * 4  # Assuming 8 hours per day, 5 days per week, 4 weeks per month
        yearly_salary = monthly_salary * 12
        
        car_payment = monthly_salary * 0.15
        house_payment = monthly_salary * 0.3
        expenses = monthly_salary * 0.4
        savings = monthly_salary * 0.15

        result_text = f"Your monthly income      ${monthly_salary:.2f}\n" \
                      f"Your yearly income          ${yearly_salary:.2f}\n" \
                      f"\n" \
                      f"Car Payment (15%):         ${car_payment:.2f}\n" \
                      f"House Payment (30%):    ${house_payment:.2f}\n" \
                      f"Expenses (40%):              ${expenses:.2f}\n" \
                      f"Savings (15%):                 ${savings:.2f}"

        result_label.config(text=result_text)

        car_button.config(text=f"See Details fo Car Payment", command=lambda: show_details("Car", car_payment))
        house_button.config(text=f"See Details fo House Payment)", command=lambda: show_details("House", house_payment))
        savings_button.config(text=f"See Details for Savings)", command=lambda: show_details("Savings", savings))

        car_button.pack(pady=5)
        house_button.pack(pady=5)
        savings_button.pack(pady=5)
    except ValueError:
        result_label.config(text="Please enter a valid hourly salary")

def show_details(category, amount):
    details_frame.pack_forget()  # Hide frame initially

    if category == "Car":
        message = f"If you buy a car around ${60 * amount:.2f}, you're able to paid off the car in 5 years."
        display_image("C:/Users/Shaf/Documents/Ivy tech/SDEV140-54P-IO-202320-I-82X/FP/pictures/car.png", message)
    elif category == "House":
        message = f"If you buy a house around ${240 * amount:.2f}, you're able to paind off your house in 20 years."
        display_image("C:/Users/Shaf/Documents/Ivy tech/SDEV140-54P-IO-202320-I-82X/FP/pictures/home.png", message)
    elif category == "Savings":
        message = f"You can save ${240 * amount:.2f} in 20 years."
        display_image("C:/Users/Shaf/Documents/Ivy tech/SDEV140-54P-IO-202320-I-82X/FP/pictures/savings.png", message)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")
    car_button.pack_forget()
    house_button.pack_forget()
    savings_button.pack_forget()
    details_frame.pack_forget()

def display_image(image_path, message):
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image  # Keep a reference
    details_label.config(text=message)
    details_frame.pack()  # Display frame after pressing See Details

# Create the main window
root = tk.Tk()
root.geometry("900x1200")
root.title("Finance Minister")


# Load the logo image
logo_image = tk.PhotoImage(file="C:/Users/Shaf/Documents/Ivy tech/SDEV140-54P-IO-202320-I-82X/FP/pictures/logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=5)

# Create and place widgets using the pack system
label = tk.Label(root, text="Enter Hourly Salary:", font=('arial', 18, "bold"))
label.pack()


entry = tk.Entry(root, font=('arial', 18, "bold"))
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('arial', 18, "bold"))
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", justify=tk.LEFT, font=('arial', 16, "bold"))
result_label.pack(pady=20)

car_button = tk.Button(root, text="See Details (Car Payment)", font=('arial', 14))
house_button = tk.Button(root, text="See Details (House Payment)", font=('arial', 14))
savings_button = tk.Button(root, text="See Details (Savings)", font=('arial', 14))

reset_button = tk.Button(root, text="Reset", command=reset, font=('arial', 14))
reset_button.pack(side=tk.BOTTOM, pady=20)

# Frame to display details
details_frame = tk.Frame(root)
details_label = tk.Label(details_frame, text="",font=('arial', 14, "bold"), justify=tk.LEFT)
details_label.pack(padx=10, pady=10)

# Image label
image_label = tk.Label(details_frame)
image_label.pack()

root.mainloop()
