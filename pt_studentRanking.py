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
