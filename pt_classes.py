class Student:
    "This is a Student Class"
    def __init__(self, ma_mock, ma_actual, eng_mock, eng_actual, sci_mock, sci_actual):
        self.ma_mock = ma_mock
        self.ma_actual = ma_actual
        self.eng_mock = eng_mock
        self.eng_actual = eng_actual
        self.sci_mock = sci_mock
        self.sci_actual = sci_actual

    def averageActual(self):
        avg = (self.ma_actual + self.eng_actual + self.sci_actual) / 3
        return avg


    def progress(self):
        maProgress = (self.ma_actual - self.ma_mock) / 10
        engProgress = (self.eng_actual - self.eng_mock) / 10
        sciProgress = (self.sci_actual - self.sci_mock) / 10
        avgProgress = (maProgress + engProgress + sciProgress) / 3
        return maProgress, engProgress, sciProgress, avgProgress

def main():
    print()
    print("First TEST STUDENT: jamessmith")
    jamessmith = Student(80,75,57,65,50,80)
    print("Task 1, as per the provided example data in the second table (there is a discrepancy in Science):", end = '')
    print(jamessmith.averageActual())
    print("Task 2, Progress scores")
    print("Maths: ", end ='')
    print(jamessmith.progress()[0])
    print("English: ", end ='')
    print(jamessmith.progress()[1])
    print("Science: ", end ='')
    print(jamessmith.progress()[2])
    print("Average Progress: ", end ='')
    print(jamessmith.progress()[3])

    print()
    print("SECOND TEST STUDENT: Student0080")
    Student0080 = Student(99,88,92,96,79,54)
    print("Average Actual Test Score :", end ='')
    print(Student0080.averageActual())
    print("Task 2, Progress scores")
    print("Maths: ", end ='')
    print(Student0080.progress()[0])
    print("English: ", end ='')
    print(Student0080.progress()[1])
    print("Science: ", end ='')
    print(Student0080.progress()[2])
    print("Average Progress: ", end ='')
    print(Student0080.progress()[3])
    print()

main()