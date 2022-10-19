# class Car:
#
#     def __init__(self):
#         self.co = "BMW"
#         self.mil = 10
#def show(self.co, self.mil)
#
# c1 = Car()
# c2 = Car()
# print(c1.co, c1.mil)
# print(c2.mil, c2.co)
# c1.show()

class student:
    school = 'Uganda christian University'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m2) / 3

    def get_m1(self):
        return self.m1

    # @ is used as a class decorator to call a class method
    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def get_info():
        print('This student is in stream A23')


s1 = student(34, 56, 98)
s2 = student(45, 67, 89)

print(s2.avg())
print(s1.get_school())
student.get_info()


