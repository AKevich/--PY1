def get_unique_list_numbers() -> list[int]:
    from random import  sample
    spisok = sample([i for i in range(-10, 11)], 15)
    return spisok

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
