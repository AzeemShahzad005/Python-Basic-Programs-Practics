#find factorail of any number using python (if else) conditions 
num = int(input("Enter the Number: "))
factorial = 1
if num < 0:
    print("Factorial can not be found for -ve numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
      for i in range(1, num + 1):
        factorial = factorial * i
        
print("Factorial of ", num, "is: ", factorial)
