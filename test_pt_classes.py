import unittest
import pt_classes

class tests(unittest.TestCase):
    
    def test_pt_classes(self):
        Student0080 = pt_classes.Student(99,88,92,96,79,54)
        self.assertEqual(Student0080.averageActual(), 79.33333333333333, "Should be 79.33333333333333")
        self.assertEqual(Student0080.progress()[0], -1.1, "Maths Progress: should return -1.1")
        self.assertEqual(Student0080.progress()[1], 0.4, "English Progress: should return 0.4")
        self.assertEqual(Student0080.progress()[2], -2.5, "Science Progress: should return -2.5")
        self.assertEqual(Student0080.progress()[3], -1.0666666666666667, "Average Progress:should return -1.066....7")

        Student6911 = pt_classes.Student(56,98,74,59,67,51)
        self.assertEqual(Student6911.averageActual(), 69.33333333333333, "Should be 69.33333333333333")
        self.assertEqual(Student6911.progress()[0], 4.2, "Maths Progress: should return 4.2")
        self.assertEqual(Student6911.progress()[1], -1.5, "English Progress: should return -1.5")
        self.assertEqual(Student6911.progress()[2], -1.6, "Science Progress: should return -1.6")
        self.assertEqual(Student6911.progress()[3], 0.3666666666666667, "Average Progress: should return 0.366...7")


if __name__ == "__main__":
    unittest.main()
