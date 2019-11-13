# Python function to print the characters  
# in sorted order  
def printCharacter(s, l):  
      
    # primary stack 
    stack =[]  
      
    # secondary stack 
    tempstack =[]  
      
    # append first character   
    stack.append(s[0]) 
      
    # iterate for all character in string  
    for i in range(1, l): 
          
        # i-th character ASCII  
        a = ord(s[i]) 
          
        # stack's top element ASCII  
        b = ord(stack[-1])  
          
        # if greater or equal to top element  
        # then push to stack  
        if((a-b)>= 1 or (a == b)): 
            stack.append(s[i])  
              
        # if smaller, then push all element  
        # to the temporary stack  
        elif((b-a)>= 1): 
              
            # push all greater elements  
            while((b-a)>= 1): 
                  
                # push operation  
                tempstack.append(stack.pop()) 
                  
                # push till the stack is not-empty  
                if(len(stack)>0): 
                    b = ord(stack[-1]) 
                else: 
                    break
                      
            # push the i-th character  
            stack.append(s[i]) 
              
            # push the tempstack back to stack  
            while(len(tempstack)>0): 
                stack.append(tempstack.pop())  
                  
    # print the stack in reverse order
    print("Output:",''.join(stack))  
  
  
# Driver Code
def main():
    s = str(input("String: "))
    l = len(s) 
    printCharacter(s, l)

if main() == "__main__":
    main()

'''
TEST CASES
------------
String: 987654321
Output: 123456789

String: cats are better than dogs
Output:     aaabcdeeeghnorrsstttt

String: qwertyuiop
Output: eiopqrtuwy




'''
