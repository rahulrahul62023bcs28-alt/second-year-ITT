class Car:
   def drive(self):
      print("Vroom!!")

car=Car()
car.drive()
class Book:
   def __init__(self,title,author):
      self.title=title
      self.author=author
   def display(self):
      print(f"{self.title} is  written by {self.author}.")
