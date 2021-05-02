num = int(input("Enter Number:"))  # Taking input from user

primenum = range(2, num+1) # initially putting all numbers in prime number iterable

for i in range(2, num+1):  #starting loop from to the Nth number
    primenum = list(filter(lambda x: x == i or x % i, primenum))   #created lambda expression which will eliminate all the mulitples of number from PRIMENUM iterable.Here numbers satisfying one of the condition will get added to the prime number list

print(primenum)
print(sum(primenum))

