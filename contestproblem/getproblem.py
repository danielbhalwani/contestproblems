
'''
if all 3 inputs = 60, output equilateral
if all 3 inputs = 180 but two inputs are same, output isoseles
if all 3 inputs = 180 but no inputs are the same, output scalene 
if all 3 inputs ≠ 180 output error
'''
# each integer must be on their own separate line
# each integer must be <0 but >180 precondition
# three angles = one of the three conditions
# going to need multiple if statements and assignment statements 

a = input()
a = int(a)

b = input()
b = int(b)

c = input()
c = int(c)

sum = a + b + c



if (sum!= 180):
	print("Error")

elif (a == 0 or b == 0 or c == 0):
	print("Error")

elif (a == 60 and b ==60 and c==60):
	print ("Equilateral")

elif (a == b or a == c or b == c): 
	print ("Isoseles")

elif (a != b and a!= c and b!= c): 
	print("Scalene")




