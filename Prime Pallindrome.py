def prime_pallindrome(N):
    n1 = 2
    a = []
    z = []
    while n1 <= N:
        is_prime = True
        for i in range(2, n1 // 2 + 1):
            if n1 % i == 0:
                is_prime = False
                break
        if is_prime == True:
            a.append(n1)

        n1 += 1
    for i in a:
        l = str(i)
        y = l[::-1]
        if y == l:
            z.append(y)

    q = ','.join(z)
    return q


N = eval(input("Enter a Number to print  prime numbers in  palindrome format : "))
output = prime_pallindrome(N)
print('''These are the prime palindrome  numbers for the given Number "%i"''' % N, '\n\n',
      '(%s)' % output, '\n')
