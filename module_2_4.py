numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # исходный список
print(numbers)
primes = [2, 3, 5, 7, 11, 13]  # простые числы
print(primes)
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]  # составные числы
print(not_primes)
primes_1 = [" ", " ", " ",]
print(primes_1)
not_primes_1 = [" ", ' ', ' ', ' ',]
print(not_primes_1)
x = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
        return True
    print(x)

# def is_prime(a):
 # if a % 2 == 0:
     # return a == 2
    #d = 3
    #while d * d <= a and a % d != 0:
       # return d * d > a
   # print(is_prime(int(input("Enter a number: "))))

 # return True
 # else:
     # return False

#a = int(input("Enter a number: "))
  #print(is_prime(a))
for i in range(1, 15):
 for j in range(1, 15):
   print(f'{i} x {j} = {i * j}')

























