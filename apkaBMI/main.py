import tkinter as tk


class Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height / 100

    def calculate_bmi(self):
        try:
            bmi = self.weight / (self.height ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return "Error: Height cannot be zero."


class GUI:
    def __init__(self, root_gui):
        self.root = root_gui
        self.root.title("BMI Calculator")

        self.weight_label = tk.Label(root_gui, text="Enter Weight (kg):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root_gui)
        self.weight_entry.pack()

        self.height_label = tk.Label(root_gui, text="Enter Height (cm):")
        self.height_label.pack()

        self.height_entry = tk.Entry(root_gui)
        self.height_entry.pack()

        self.calculate_button = tk.Button(root_gui, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(root_gui, text="")
        self.result_label.pack()

        self.category_label = tk.Label(root_gui, text="")
        self.category_label.pack()

    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())

        calculator = Calculator(weight, height)
        result = calculator.calculate_bmi()

        if isinstance(result, float):
            message = f"Your BMI is: {result}"
            if result < 16:
                category = "Underweight (Severe thinness)"
            elif 16 <= result < 17:
                category = "Underweight (Moderate thinness)"
            elif 17 <= result < 18.5:
                category = "Underweight (Mild thinness)"
            elif 18.5 <= result < 25:
                category = "Normal range"
            elif 25 <= result < 30:
                category = "Overweight (Pre-obese)"
            elif 30 <= result < 35:
                category = "Obese (Class I)"
            elif 35 <= result < 40:
                category = "Obese (Class II)"
            else:
                category = "Obese (Class III)"

        else:
            message = result

        self.result_label.config(text=message)
        self.category_label.config(text=category)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
