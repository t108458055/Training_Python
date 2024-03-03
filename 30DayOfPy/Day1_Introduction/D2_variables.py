"""

This is a multiline comment

that spans multiple lines

in Python

"""
print('Hello world')

# Variables in Python
first_name =  'Asabeneh' # type string
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250 # type int
is_married = True # type boolean
skills = ['HTML', 'CSS', 'JS', 'React', 'Python'] # type  list
person_info = {
'first_name' :  'Asabeneh',
'last_name': 'Yetayeh',
'country' : 'Finland',
'city' : 'Helsinki'
} # type(dict)
tup_ex = (1,2) # type tuple
set_ex = zip([1,2],[3,4]) # type set

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Get User input using the input()  built-in function

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)