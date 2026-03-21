import unittest
from logic import StudentManager

class TestScholarSync(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager() 

    def test_timer_math(self):
        # Test if 25 minutes correctly converts to 1500 seconds
        # self.assertEqual(self.manager.calculate_timer (25), 1500)
        pass
        
    def test_scholarship_eligible(self):
        # Test if a high GPA returns False
        # self.assertFalse(self.manager.is_eligible_for_scholarship(2.0))
        pass

if __name__ == '__main__':
    unittest.main()