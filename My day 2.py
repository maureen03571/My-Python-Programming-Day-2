#Greeting pogram
name=input("What is your name? ")
age=int(input("How old are you? "))
color=input("What is your favorite color? ")
print("Hello " + name + ", you are " + str(age) + " years old and  " + color + " is your favorite color!")
print("Welcome to Maureen's page")
from faker import Faker
fake=Faker()
for _ in range(10):
    print(fake.name())