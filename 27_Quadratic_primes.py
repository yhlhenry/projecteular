a_candi = [x for x in range(-1000, 1000) if x % 2 != 0]
b_candi = [x for x in range(-1000, 1000) if x % 2 != 0]


def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


number_prime_list = []
max_num = 0
for a in a_candi:
    for b in b_candi:
        for n in range(80):
            if not isPrime(n * n + a * n + b):
                if(n > max_num):
                    max_num = n
                    at = a
                    bt = b
                number_prime_list.append(n)
                break

print(max(number_prime_list))
print(at, bt)
