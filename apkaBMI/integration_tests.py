import unittest
import tkinter as tk
from tkinter import Entry
from unittest.mock import patch
from main import Calculator, GUI


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = GUI(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch.object(GUI, 'calculate_bmi')
    def test_button_click_calls_calculate_bmi(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "70")
        self.app.height_entry.insert(0, "175")
        self.app.calculate_bmi()

        mock_calculate_bmi.assert_called_once()

    @patch.object(Calculator, 'calculate_bmi', return_value=22.86)
    def test_calculate_bmi_updates_result_label(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "70")
        self.app.height_entry.insert(0, "175")
        self.app.calculate_bmi()

        result_label_text = self.app.result_label.cget("text")
        self.assertEqual(result_label_text, "Your BMI is: 22.86")

    @patch.object(Entry, 'get', side_effect=["70", "175"])
    @patch.object(Calculator, 'calculate_bmi', return_value=22.86)
    def test_button_click_calls_calculate_bmi_with_entry_values(self, mock_calculate_bmi, mock_entry_get):
        self.app.calculate_bmi()

        mock_entry_get.assert_any_call()
        mock_calculate_bmi.assert_called_once_with()

    @patch.object(Calculator, 'calculate_bmi', return_value=4.44)
    def test_calculate_bmi_updates_category_label_underweight_severe_thinness(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "10")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Severe thinness)")

    @patch.object(Calculator, 'calculate_bmi', return_value=16.89)
    def test_calculate_bmi_updates_category_label_underweight_underweight_moderate_thinness(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "38")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Moderate thinness)")

    @patch.object(Calculator, 'calculate_bmi', return_value=17.78)
    def test_calculate_bmi_updates_category_label_underweight_underweight_mild_thinness(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "40")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Underweight (Mild thinness)")

    @patch.object(Calculator, 'calculate_bmi', return_value=20.00)
    def test_calculate_bmi_updates_category_label_normal_range(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "45")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Normal range")

    @patch.object(Calculator, 'calculate_bmi', return_value=28.89)
    def test_calculate_bmi_updates_category_label_overweight_pre_obese(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "65")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Overweight (Pre-obese)")

    @patch.object(Calculator, 'calculate_bmi', return_value=32.00)
    def test_calculate_bmi_updates_category_label_obese_class_i(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "72")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class I)")

    @patch.object(Calculator, 'calculate_bmi', return_value=37.78)
    def test_calculate_bmi_updates_category_label_obese_class_ii(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "85")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class II)")

    @patch.object(Calculator, 'calculate_bmi', return_value=66.67)
    def test_calculate_bmi_updates_category_label_obese_class_iii(self, mock_calculate_bmi):
        self.app.weight_entry.insert(0, "150")
        self.app.height_entry.insert(0, "150")
        self.app.calculate_bmi()

        category_label_text = self.app.category_label.cget("text")
        self.assertEqual(category_label_text, "Obese (Class III)")


if __name__ == '__main__':
    unittest.main()
