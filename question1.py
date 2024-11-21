## LOOPS

#Python program that prints all even numbers between 1 and 20 using a for loop
#Basic
for even in range(1,21):# we use range to generate numbers from 1 to 20
    if even  % 2==0: #checks if the number is divisible by 2(even)
        print(even)#if true the number is printed
#OR
def even_number():
    for even in range(2,20,2):
        print(even)
even_number()        

#Intermediate
#Use a while loop to ask the user to input a number until they provide a number greater than 10
number =0#we initialize number with 0 to enter the loop
while number <=10:#While loop runs as long as the input number is less than or equal to 10
    number = int(input('Enter a number greater than 10: '))#The loop stops when the user inputs a number greater than 10
    if number <= 10:
        print('Number should be greater than 10. Try again')
    else:
        print('Congratulations! You entered a number greater than 10:',number)
   
#Advanced
#A program that prints the multiplication table(from 1 to 10)for numbers from 1 to 5 using nested for loops
for number in range(1, 6):#Outer loop for numbers 1 to 5
    print(f'\nMultiplication table for {number}:\t')
    for multiplier in range(1, 11):#Inner loop for multiplication from 1 to 10
        result = number * multiplier
        print(f'{number}*{multiplier} = {result}')
print()
#Challenge
#A list of integers [4,7,2,9,12,15], find the sum of all odd numbers
numbers =[4,7,2,9,12,15]
odd_sum=0
for number in numbers:
    if number % 2 !=0:#check if the number is odd
        odd_sum+=number
print('Sum of odd numbers:', odd_sum)

