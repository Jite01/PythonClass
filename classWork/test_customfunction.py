import unittest
import customfunction

class DivideEvaluation(unittest.TestCase):
	def test_get_divide_exists(self):
		customfunction.get_divide(5)
	
	def test_that_get_divide_outputs_correct_result(self):
		actual = customfunction.get_divide(12)
		expected = 2
		self.assertEqual(actual, expected)

	def test_that_get_divide_tolerates_invalid_input(self):
		actual = customfunction.get_divide("omo")
		expected = "Be fr. Invalid input"
		self.assertEqual(actual, expected)

	def test_that_get_divide_tolerates_invalid_input(self):
		actual = customfunction.get_divide()
		self.assertEqual(TypeError, customfunction.get_divide, )

	def test_that_get_divide_tolerates_negative_integers(self):
		actual = customfunction.get_divide(-100)
		expected = 10.0
		self.assertEqual(actual, expected)

	
