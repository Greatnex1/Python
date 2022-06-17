firstNumber = int(input("Enter first integer :"))
secondNumber = int(input("Enter second integer :"))
thirdNumber = int(input("Enter third integer :"))
sum = firstNumber + secondNumber + thirdNumber
product = firstNumber * secondNumber * thirdNumber
average: float = sum / 3
if firstNumber > secondNumber and firstNumber > thirdNumber:
    print("largest number is :", firstNumber)
if secondNumber > thirdNumber:
    print("Largest number is :", secondNumber)
else:
    print("Largest number is:", thirdNumber)
print('Sum of three integers entered is:', sum)
print("Product of integers is :", product)
print("Average  is", average)
