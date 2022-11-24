def get_random_password(n: int = 8) -> str:
    from string import ascii_letters, digits
    from random import sample
    abc = [i for i in ascii_letters] + [str(i) for i in digits]
    nabor = sample(abc, n)
    return ''.join(nabor)

print(get_random_password())
