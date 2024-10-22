# prime_generator.py

s = 0
p = 1
n = int(input("Enter a number (n): "))
ip = True

print("Prime numbers below", n, "are:", end=" ")
for j in range(2, n + 1):
    for i in range(2, j // 2 + 1):
        if j % i == 0:
            ip = False
            break
        else:
            ip = True
    if ip:
        print(f"{j}  ", end="")
        s = s + j
        p = p * j

print(f"\nSum of all prime numbers below {n} is {s}.")
new_prime = p + 1
print(f"The new prime candidate (p + 1) is {new_prime}.")
