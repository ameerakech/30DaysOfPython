# Step 1: Declare variables
age = 25  
height = 5.9  
complex_number = 3 + 4j

# Step 2: Calculate area of a triangle
base = float(12) 
height = float(4) 
area = 0.5 * base * height  
print(f"The area of the triangle is {area}")

# Calculate perimeter of a triangle
side_a = float(12)  
side_b = float(4) 
side_c = float(2) 
perimeter = side_a + side_b + side_c 
print(f"The perimeter of the triangle is {perimeter}")

# Calculate area and perimeter of a rectangle
length = 5 
width = 7 
rectangle_area = length * width 
rectangle_perimeter = 2 * (length + width) 
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

#Calculate area and circumference of a circle
radius = float(7) 
circle_area = 3.14 * radius * radius 
circumference = 2 * 3.14 * radius 
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circumference}")

# Check whether 'jargon' is found in the sentence
sentence = "I hope this course is not full of jargon."
print(f"'jargon' is in the sentence: {'jargon' in sentence}")

# Length of 'python' and convert to float and then to string
length_python = len('python') 
length_python_float = float(length_python) 
length_python_str = str(length_python_float) 
print(f"Length of 'python' as float: {length_python_float}, as string: {length_python_str}")

# Check if a number is even
number = 4 
is_even = number % 2 == 0 
print(f"Is {number} even? {is_even}")

# Check if floor division of 7 by 3 equals int(2.7)
floor_division_check = (7 // 3) == int(2.7) 
print(f"Is floor division of 7 by 3 equal to int(2.7)? {floor_division_check}")


