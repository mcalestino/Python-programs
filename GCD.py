def gcd(m, n):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif m >= n:
        return gcd(n, m - n)
    elif n > m:
        return gcd(m, n - m)

def main():
    m = int(input("m: "))
    n = int(input("n: "))
    print("The Greatest Common Divisor = ",gcd(m,n))

if __name__ == '__main__':
    main()
