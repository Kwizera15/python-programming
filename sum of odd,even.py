def sum_even_odd(lst):
    even_sum = sum(num for num in lst if num % 2 == 0)
    odd_sum = sum(num for num in lst if num % 2 != 0)
    return (even_sum, odd_sum)


my_list = [1, 2, 3, 4, 5, 6]
result = sum_even_odd(my_list)
print(result)
