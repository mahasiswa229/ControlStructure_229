def print_design(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end=' ')
        print()

n = int(input("Enter a number : "))
print_design(n)