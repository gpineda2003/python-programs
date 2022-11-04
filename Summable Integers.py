n = int(input("Please enter a positive integer:\n"))

t = n
start = 0
end = 0

while t % 2 == 0:
    t = t/2

if t == 1:
    print("\nNo summation possible")

elif t == n:
    start = int(n/2)
    end = start + 1
    print("The starting number is:", int(start))
    print("The ending number is:", int(end))
else:
    c = n / t
    start = c - int(t/2)
    end = c + int(t/2)

    if start <= 0:
        start = -1*start + 1

    print("The starting number is:", int(start))
    print("The ending number is:", int(end))

