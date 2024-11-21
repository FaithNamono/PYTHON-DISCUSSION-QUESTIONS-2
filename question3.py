#DICTIONARIES
#Basic
#Create a dictionary with student information and point each key-value pair

student={'name':'John','age':20,'grade':'A'}
for key, value in student.items():#We use .items() to iterate through the dictionary's key-value pairs
    print(f'{key}: {value}')

#Intermediate
#Return names of people 21 or older from a dictionary
people ={'Alice':24,'Bob':19,'Charlie':30}
def filter_adults(people):
    return[name for name, age in people.items() if age >= 21]
print(filter_adults(people))

#Advanced
#Calculate the total cost from a list of items bought
store = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = sum(store[item] for item in items_bought)
print("Total cost:", total_cost)

#Challenge
#Count the occurrences of each word in a sentence
sentence='hello world hello'
words = sentence.split()#spliting sentence into words
word_count = {}
for word in words:
    word_count[word]=word_count.get(word, 0) +1

print(word_count)
