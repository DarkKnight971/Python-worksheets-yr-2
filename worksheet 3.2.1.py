'''1. Write a Python class named Student with two attributes student_id,
      student_name. Add a new attribute student_class and display the
      entire attribute and their values of the said class. Now remove the
      student_name attribute and display the entire attribute with values'''

class Student() :
  student_id = input("Enter student id : ")
  student_name = input("Enter student name : ")
  
def main() :
  print("\nOriginal attributes and their values of the Student class :")
  for attr, value in Student.__dict__.items():
      if not attr.startswith('_'):
          print(f'{attr} -> {value}')

  print("\nNew attributes added and their values of the Student class :")
  Student.student_class  = input("Enter student class")
  for attr, value in Student.__dict__.items():
      if not attr.startswith('_'):
          print(f'{attr} -> {value}')
          
  print("\nRemoved attribute and values of remaining attributes in the Student class :")
  del Student.student_name
  #delattr(Student, 'student_name')
  for attr, value in Student.__dict__.items():
      if not attr.startswith('_'):
          print(f'{attr} -> {value}')
          
if __name__ == "__main__" :
  main()
