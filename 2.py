def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("1st number :"))
num2 = int(input("2nd number :"))
num3 = int(input("3rd number :"))

largest_num = find_largest(num1, num2, num3)
print("the largest number is :", largest_num)