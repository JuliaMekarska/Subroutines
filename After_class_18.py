def sum():
    sum_of_digits = 0
    for digit in number:
        sum_of_digits = sum_of_digits + int(digit)
    print(sum_of_digits)
    
number = input("Enter the number: ")
sum()
