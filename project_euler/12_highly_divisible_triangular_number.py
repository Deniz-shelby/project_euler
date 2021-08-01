'''
Highly divisible triangular number
Problem 12


The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

def get_triangle_number(n):
    triangle_number_list = []
    for i in range(1, n + 1):
        triangle_number = (i ** 2 + i)//2
        triangle_number_list.append(triangle_number)
    return triangle_number_list

#get_triangle_number(10)

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


#print(get_factors(28))

def highly_divisible_triangular_number(n):
    triangle_number_list = get_triangle_number(n)
    for triangle_number in triangle_number_list:
        if len(get_factors(triangle_number)) > 500:
            return triangle_number

print(highly_divisible_triangular_number(1000))

