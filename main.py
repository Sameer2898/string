'''Write a program to make a string as inut and cheks wheather characters area repeated in string or not.
If characters are not repeated then duplicate these else not.'''

user = input('Enter a string:- ')
output = []
for i in user:
    output.append(i)
    if user.count(i) == 1:
        output.append(i)
print(f'The entered string is:- {user}')
print(''.join(output))
print(f'The output string is:- {user}')