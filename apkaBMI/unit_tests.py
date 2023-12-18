import unittest
from tkinter import Tk
from main import Calculator, GUI


class TestCalculator(unittest.TestCase):

    def test_calculate_bmi_valid_input(self):
        calculator = Calculator(70, 175)
        result = calculator.calculate_bmi()
        self.assertEqual(result, 22.86)

    def test_calculate_bmi_zero_height(self):
        calculator = Calculator(70, 0)
        result = calculator.calculate_bmi()
        self.assertEqual(result, "Error: Height cannot be zero.")


class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = GUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_calculate_bmi_button_click_valid_input(self):
        self.app.weight_entry.insert(0, "70")
        self.app.height_entry.insert(0, "175")
        self.app.calculate_bmi()
        result_label_text = self.app.result_label.cget("text")
        self.assertEqual(result_label_text, "Your BMI is: 22.86")

    def test_calculate_bmi_button_click_zero_height(self):
        self.app.weight_entry.insert(0, "70")
        self.app.height_entry.insert(0, "0")
        self.app.calculate_bmi()
        result_label_text = self.app.result_label.cget("text")
        self.assertEqual(result_label_text, "Error: Height cannot be zero.")

    def test_calculate_bmi_button_click_and_check_category_underweight_severe_thinness(self):
        self.app.weight_entry.insert(0, "10")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Severe thinness)")

    def test_calculate_bmi_button_click_and_check_category_underweight_moderate_thinness(self):
        self.app.weight_entry.insert(0, "38")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Moderate thinness)")

    def test_calculate_bmi_button_click_and_check_category_underweight_mild_thinness(self):
        self.app.weight_entry.insert(0, "40")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Mild thinness)")

    def test_calculate_bmi_button_click_and_check_category_underweight_normal_range(self):
        self.app.weight_entry.insert(0, "45")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Normal range")

    def test_calculate_bmi_button_click_and_check_category_overweight_pre_obese(self):
        self.app.weight_entry.insert(0, "65")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Overweight (Pre-obese)")

    def test_calculate_bmi_button_click_and_check_category_obese_class_i(self):
        self.app.weight_entry.insert(0, "72")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class I)")

    def test_calculate_bmi_button_click_and_check_category_obese_class_ii(self):
        self.app.weight_entry.insert(0, "85")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class II)")

    def test_calculate_bmi_button_click_and_check_category_obese_class_iii(self):
        self.app.weight_entry.insert(0, "150")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()
        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class III)")


if __name__ == "__main__":
    unittest.main()
