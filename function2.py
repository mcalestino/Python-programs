#NUMBER 1
# A recursive Python program  
# to check whether a given  
# number is palindrome or not 
def palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False
        
print("Problem 1")
s = input("string1: ")
if (palindrome(s)) : 
    print ("Yes", s, "is a palindrome")
else : 
    print ("No", s, "is not a paindrome")
print()    

# NUMBER 2
# Python code to reverse a string  
# using recursion 
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]
    
print("Problem 2")  
s = input("String2: ")
print ("The original string  is : ",end="") 
print (s) 
print ("The reversed string is: ",end="") 
print (reverse(s))
print()    

#NUMBER 3
# Python program to reverse a string using recursion 
# Function to print reverse of the passed string 
def reverse(string): 
    if len(string) == 0: 
        return
      
    temp = string[0] 
    reverse(string[1:]) 
    print(temp, end='') 
  
# Driver program to test above function
print("Problem 3")
string = input("string: ")
print ("The reversed string is: ",end="")
reverse(string)
print()    

'''
This function in Python calculates an
exponential equation.
'''
#NUMBER 4
def exponential(x, n):
    # First base case
    if n == 0:
        return 1
    
    # Second base case
    if n == 1:
        return x
 
    # Even values of (n)
    if n % 2 == 0:
        y = exponential(x, n / 2)
        return y * y
    # Odd values of (n)
    else:
        y = exponential(x, n - 1)
        return x * y
print()
print("Problem 4")
x = int(input("x: "))
n = int(input("n: "))
print(x, "^", n, "=", exponential(x,n))
print()

    
#NUMBER 5
def prefixSum(n,s):
    startpo = (n - s) + 1;
    if s == 1:
        return startpo;
    else:
        return startpo + prefixSum(n, s - 1)
    
print("Problem 5")
'''
print("Enter a list of numbers: ")
n = [int(x) for x in input().split()]
'''
n = int(input("n: "))
s = int(input("s: "))
print (prefixSum(n,s))
print()

# NUMBER 6
# Function to check sum of 
# digit using recursion 
def sum_of_digit(n): 
    if n == 1: 
        return 0
    else:
        return (n % 10 + sum_of_digit(int(n / 10))) 
  
# Driven code to check above
print("Problem 6")
num = int(input("num: "))
result = sum_of_digit(num) 
print("Sum of digits in",num,"is", result)
print()

#NUMBER 7
def binary_search(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid
 
print("Problem 7") 
alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
print()    

#NUMBER 8
# Given an array of size n, where every   
# element is k away from its target  
# position, sorts the array in O(nLogk) time. 
def sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return sort([e for e in arr[1:] if e <= arr[0]]) + [arr[0]] +\
            sort([e for e in arr[1:] if e > arr[0]])

print("Problem 8")
arr = input('Enter a list of numbers: ')
arr2 = arr.split()
arr = [int(x) for x in arr2]
#n = len(arr)
print(sort(arr))
print()
    

#NUMBER 9
def sideways_triangle(a,b):
    if a > b:
        return
    if a==b:
        print(a * "-")
    else:
        print(a * "-")
        sideways_triangle(a+1,b)
        print(a * "-")
print()

print("Problem 9")
a = int(input("a: "))
b = int(input("b: "))
print()
sideways_triangle(a,b)
print()

#NUMBER 10
def printPattern(n, c):
    if n == 1:
        print(c * ' ' + '|')
    else:
        printPattern(n // 2, c)
        print(c * ' ' + n * '-')
        printPattern(n // 2, c + n // 2)

print("Problem 10")
n = int(input("n: "))
c = int(input("c: "))
print()
print(printPattern(n,c))
