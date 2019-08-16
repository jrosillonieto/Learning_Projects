def is_armstrong_number(number):
    number_str = str(number)
    number_len = len(number_str)
    sum = 0
    for digit in number_str:
        sum = sum + int(digit)**(int(number_len))
        if sum == number:
            return True
    return False
