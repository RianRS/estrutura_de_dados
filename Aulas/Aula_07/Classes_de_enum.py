from enum import Enum
Names = Enum('Names', [('Waiz', 8), ('Tom', 5), ('Sara', 7), ('Lee', 10)])
print(Names.Lee.value)
print(Names.Waiz.value)

# or

class Student(Enum):
    Kat = 1
    Lean = 2
    Bob = 3
    Bruce = 4

print(Student.Bruce.value)