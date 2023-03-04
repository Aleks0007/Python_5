"""
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии. 
"""

A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)
    
print(power(A, B))