print("""Math+ by Belz. (version 1.7.9, python 3.8 minimum)
Thanks for the support ! Final version is almost there :)
""")

def xor(x:bool, y:bool):
    return not x==y
def try_int(str: str):
    try:
        return int(str)
    except:
        return False
def is_number(str: str):
    try:
        str = int(str)
        return True
    except:
        return False
def exponent(n, exponent=2, do_round=True):
    if do_round: return round(n ** exponent)
    else: return n ** exponent
def square(n, do_round=True):
    if do_round: return round(n ** 2)
    else: return n ** 2
def square_root(n:int, do_round=True):
    if do_round: return round(n ** (1/2))
    else: return n ** (1/2)
def is_even(n:int):
    return round(n/2) == n/2
def is_not_even(n:int):
    return not is_even(n)
def is_prime(n):
    return_value = True
    n = int(n)
    for i in range(2, n):
        if n % i == 0:
            return_value = False

    return return_value
def is_not_prime(n):
    return not is_prime(n)
def pyth(l1, l2, do_round=True):
    return square_root(square(l1, do_round) + square(l2, do_round), do_round)
def get_percentage(total=100, nb=100, do_round=True):
    if do_round: return round((100*nb)/total)
    else: return (100*nb)/total
def percentage(percentage=100, total=100, do_round=True):
    if do_round: return round((percentage*total)/100)
    else: return (percentage*total)/100
