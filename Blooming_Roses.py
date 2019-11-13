# Blooms defined as m roses in a row
# find latest date where there are k longRuns
# a contains the date at which each rose bush will bloom
#   ex. [1,5,2,6,7,3,4,7,8,3,4,7]
#       rose bush 1 will bloom on the 1st day
#       rose bush 3 will bloom on the 2nd day
def blooms(A, k, m):
    if len(A) < k*m or len(A) < m:
        return 0
    maxDateInA = max(A)
    beginIndex = 0
    endIndex = A.index(maxDateInA)
    longRuns = 0

    while True:
        
        if endIndex-beginIndex >= m:
            longRuns += 1

            print("long run from %d to %d" % (beginIndex, endIndex))
            print(A[beginIndex:endIndex], "\n")

            beginIndex = endIndex+1
        try:
            endIndex = A.index(maxDateInA, beginIndex)
        except ValueError as e:
            break

    if longRuns == k:
        return maxLongRunDate
    else:
        return 0
    
def main():    
    a = input("A: ")
    input_A = [int(i) for i in a.split(',') if i.isdigit()]
    k = int(input("K: "))
    m = int(input("M: "))
    blooms(a,k,m)

if __name__ == '__main__':
    main()

#blooms([1,5,2,6,7,3,4,7,8,3,4,7], 2, 3)

'''
TEST CASES
------------
A: 1,5,6,7,1,2,3,4,5,9
K: 3
M: 4
long run from 0 to 18
1,5,6,7,1,2,3,4,5,

A: 1,2,3,4,5
K: 3
M: 2
long run from 0 to 8
1,2,3,4, 

'''
    

    
