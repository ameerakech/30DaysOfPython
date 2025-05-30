def greetings(name):
    print (f"{name} welcome to Python practice")

def square_numbers(a):
    answer = a * a
    return answer

def area_of_a_circle(r):
    pi = 3.14
    answer = pi * r ** 2
    return answer

def sum(*numbers):
    total = 0
    for number in numbers:
        print (number)
        total += number
    return total

def calculate_age (age):
    year = 2025 - age
    return year


def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)

print (square_numbers(4))
print (area_of_a_circle(7))
print (sum(5,9,10))
print (calculate_age(20))
print (generate_groups("Akira","Zamba","simba"))


   