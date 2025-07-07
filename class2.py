class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def show_report(self):
        print(f"{self.name} ({self.roll}) — Average: {self.average()}")

# Create objects
s1 = Student("Puja", 101, [90, 85, 95])
s2 = Student("Ritu", 102, [80, 70, 88])

s1.show_report()
s2.show_report()
