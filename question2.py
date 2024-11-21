#LISTS

#Basic 
#Create a list of 5 fruits and print each fruiton a new line using a for loop
fruits=['Apple','Cherry','Mango','Pawpaw','Orange']
for fruit in fruits:
    print(fruit)

#Intermediate
#A function that takes a list of numbers and returns a new list with each number squared
def squareNumbers(numbers):
    return[number ** 2 for number in numbers]
print(squareNumbers([1,2,3]))#output:[1,4,9]

#Advanced
#Combine List1=[1,2,3] and list2=[4,5,6] into [1,4,2,5,3,6]
list1=[1,2,3]
list2=[4,5,6]
combined =[]
for i in range(len(list1)):
    combined.append(list1[i])
    combined.append(list2[i])
print(combined)
#OR
list1=[1,2,3]
list2=[4,5,6]
combined = list1 + list2
print(combined)

#Challenge
#Two largest numbers in [3, 1, 4, 1, 5, 9, 2] without using max().
numbers = [3, 1, 4, 1, 5, 9, 2]
first_largest = second_largest = float('-inf')

for number in numbers:
    if number > first_largest:
        second_largest = first_largest
        first_largest = number
    elif number > second_largest:
        second_largest = number

print("Two largest numbers are:", first_largest, "and", second_largest)

