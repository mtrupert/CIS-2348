user_string = str(input())
string = user_string.replace(' ','')

if string == string[::-1]:
    print(user_string, 'is a palindrome')
else:
    print(user_string, 'is not a palindrome')

