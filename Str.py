# Program to check if a string is palindrome or not

my_str = input("Enter a String : ")

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)


print(list(my_str),list(rev_str))
if list(my_str) == list(rev_str):
    print("String are Palindrome")
else:    
    print("String are not Palindrome")