# quick test script to verify primes excluding 2
for i in range(1,101):
    if i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
