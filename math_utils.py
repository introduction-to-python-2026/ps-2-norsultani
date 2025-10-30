def find_max_number(num1, num2, num3):
    if num1 > num2 >= num3 or num1 > num3 >= num2:
      return num1
    elif num2 > num1 >= num3 or num2 > num3 >= num1:
      return num2
    elif num3 > num1 >= num2 or num3 > num2 >= num1:
      return num3
    elif num1 == num3 or num1 == num2 or num2 == num3 and num1 == num3 :
      return num1
    elif num1 == num3 or num1 == num2 or num2 == num3 and num2 == num1 :
      return num2
    elif num1 == num3 or num1 == num2 or num2 == num3 and num2 == num3 :
      return num2

def find_mean(num1, num2, num3):
    mean = float((num1 + num2 + num3) / 3)
    return mean


def find_mean_std(num1, num2, num3):
    mean = float((num1 + num2 + num3) / 3)
    std = float(((((num1 - mean) ** 2) + ((num2 - mean) ** 2) + ((num2 - mean) ** 2)) / 3) ** 0.5)
    return mean, std

