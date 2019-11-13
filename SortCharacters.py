def sortCharacters(S):
    chrArr = [0] * 256
    for c in S:
        chrArr[ord(c)] += 1

    inString = ""
    for i, freq in enumerate(chrArr):
        if freq > 0:
            while freq > 0:
                inString += chr(i)
                freq -= 1
    return inString

def main():
    S = input("String: ")
    print("Output :", sortCharacters(S))

if __name__ == '__main__':
    main()

'''
TEST CASES
--------------
String: mnbvcxzlkjasdfgqwertyuiop09876521
Output : 01256789abcdefgijklmnopqrstuvwxyz
>>> 
=========== RESTART: /Users/m_calestino/Desktop/SortCharacters.py ===========
String: i think cats are awesome
Output :     aaaceeehiikmnorssttw
'''    
