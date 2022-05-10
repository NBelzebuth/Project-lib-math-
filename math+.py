def mathplus_help(function='all'):
    function = function.lower()
    if function=="all":
        print(f"""Math+ by Belz. (version 1.8.0, python 3.8 minimum)

Math+ implement a lot of usefull function like:
XOR : xor(x,y) if x=True, y=False -> OUT=True, if x=True, y=False -> OUT=False
TRY INT: try_int(string) if string = "15" -> return 15 if string = "Hello" -> return False
IS NUMBER : is_number(string) if string = "15" -> return True, if string = "Hello" -> return False
EXPONENT : exponent(number, exponent, do_round):
 -- if number = 5, exponent = 2 -> return 25
 -- if number = 5, exponent = 2, do_round = True -> return 25
 -- if number = 5, exponent = 2, do_round = False -> return 25.0
SQUARE : square(n, do_round):
 -- if n = 5 -> return 25
 -- if n = 5, do_round = True -> return 25
 -- if n = 5, do_round = False -> return 25.0
IS EVEN : return if a number is an even number, is_even(n) :
 -- if n = 5 -> retrun False
 -- if n = 4 -> retrun True
IS NOT EVEN : return if a number is not an even number, is_not_even(n) :
 -- if n = 4 -> retrun False
 -- if n = 5 -> retrun True
IS PRIME : return if a number is a prime number, is_prime(n) :
 /!\ the larger the number, the longer the calculation
 -- if n = 9 -> retrun False
 -- if n = 7 -> retrun True
IS NOT PRIME : return if a number is not a prime number, is_not_prime(n) :
 /!\ the larger the number, the longer the calculation
 -- if n = 7 -> retrun False
 -- if n = 9 -> retrun True
PYTHAGORE : pyth(l1, l2, do_round) pythagore theorem
PERCENTAGE : return value by the percentage percentage(percentage, total, do_round) :
 -- if percentage = 50, total = 30 -> return 15
 -- if percentage = 50, total = 30, do_round = True -> return 15
 -- if percentage = 50, total = 30, do_round = False -> return 15.0
GET PERCENTAGE : return value by the percentage percentage(total, nb, do_round) :
 -- if nb = 15, total = 30 -> return 50
 -- if nb = 15, total = 30, do_round = True -> return 50
 -- if nb = 15, total = 30, do_round = False -> return 50.0
CRYPT : crypt(string, key, caracters, alphabet) :
 -- by default: caracters="&=(£é_ç$)+", alphabet=abcdefghijklmnopqrstuvwxyz1234567890,'.!:?  (shouldn't be changed)
 -- IF string = "Hello, World" -> return "==<<<*$*é=====é£çé(((=é=$==*£>>>"
DECRYPT : decrypt(string, key, caracters, alphabet):
 -- by default: caracters="&=(£é_ç$)+", alphabet=abcdefghijklmnopqrstuvwxyz1234567890,'.!:?  (shouldn't be changed)
 -- IF string = "==<<<*$*é=====é£çé(((=é=$==*£>>>" -> return "hello, world"
RANDOM STRING : random_string(lenth, number, caracters, separator)
 /!\ the larger the number, the longer the calculation
 -- ALLOW YOU TO CREATE RANDOM STRING
 -- IF random_string(lenth = 50, number = 1) it wil return : [RANDOM STRING 1]
 -- IF random_string(lenth = 50, number = 2, separator = " | ") it wil return :
 -> [RANDOM STRING 1] | [RANDOM STRING 2]


IN DEV : (
Function : Function allows you to calculate function
)
    
help(function name) for more details
contact me on discord if you have suggestions : 𝕭𝖊𝖑𝖟𝖊𝖇𝖚𝖙𝖍#7378
""")

    if function == "xor":
        print(f"""XOR is based on OR:
        
X------|
       |
    if x!=y ------> return True
       |
Y------|
        
So, if X = 1, Y = 0, it will return {xor(1, 0)}.
But if X = 1, Y = 1, it will return {xor(1, 1)}.
        """)

    if function == "is_number":
        print(f"""IS_NUMBER is a function to try if a string is a number:

So, if you write: is_number("Hello") it will return : {is_number("Hello")}
But if you write: is_number("156") it will return : {is_number("156")}
        """)
    
    if function == "try_int":
        print(f"""TRY_INT is a function to try if a string is a number and to convert it into an int:

So, if you write: try_int("Hello") it will return : {try_int("Hello")}
But if you write: try_int("156") it will return : {try_int("156")}
        """)
    
    if function == "exponent":
        print(f"""EXPONENT is an exponent function:

So if you write: exponent(5, 3) it will return {exponent(5, 3)}
        """)

    if function == "square":
        print(f"""SQUARE is an exponent function:

So if you write: square(5) it will return {exponent(5, 2)}
        """)

    if function == "is_even" or function == "is_not_even":
        print(f"""IS_(NOT_)EVEN is a function to know if a number is even:

So if you write: is_even(6) it will return {is_even(6)}
But if you write: is_even(7) it will return {is_even(7)}
And if you write: is_not_even(7) it will return {is_not_even(7)}
        """)

    if function == "is_prime" or function == "is_not_prime":
        print(f"""IS_(NOT_)Prime is a function to know if a number is prime:

So if you write: is_prime(7) it will return {is_prime(7)}
But if you write: is_prime(6) it will return {is_prime(6)}
And if you write: is_not_prime(6) it will return {is_not_prime(6)}
        """)

if __name__ == "__main__":
    mathplus_help()
    exit()

def xor(x:bool, y:bool):
    return not x==y

def try_int(str: str):
    try:
        return int(str)
    except:
        return 0

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
    if n != 1 and n != 0:
        return_value = True
        n = int(n)
        for i in range(2, n):
            if n % i == 0:
                return_value = False
    else:
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

def string_set(string:str):
    string = list(string)
    for i in range(5):
        string.pop(0)
    for i in range(3):
        string.pop(len(string)-1)
    return string

def random_string(lenth=5, number=1, caracters = '!"#$%&()*+,-./:;<=>?@[]^_`{|}', separator = '\n'):
    ok=False
    passlist = []
    nb = 0
    trys = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    while not ok:
        from random import randint
        caracters = list(caracters)
        alphabet = list(alphabet)
        num = list(num)
        ALPHABET = list("".join(alphabet).upper())
        total = caracters + alphabet + ALPHABET + num
        passwd = []
        if lenth >= 4:
            for i in range(lenth):
                passwd.append(total[randint(0, len(total))-1])

            tcar = False
            tnum = False
            tlow = False
            tupp = False

            for i in range(lenth):
                var = [caracters, num, alphabet, ALPHABET]
                var2 = [tcar, tnum, tlow, tupp]
                for i in range(len(var)):
                    if passwd[i] in var[i]:
                        var2[i] = True


            if not tcar == tnum == tlow == tupp:
                ok=False
                trys+=1
            else:
                if number == 1:
                    ok=True
                    return ''.join(passwd)
                else:
                    passlist.append(''.join(passwd))
                    nb+=1
                if nb == number:
                    return separator.join(passlist)
        else:
            for i in range(lenth):
                passwd.append(total[randint(0, len(total))-1])
            return "".join(passwd)

def crypt(string: str, key=None, helper=False, caracters="*=(£é_ç$+}", alphabet="abcdefghijklmnopqrstuvwxyz1234567890,'.!:? "):
    alphabet = list(alphabet)
    caracters = list(caracters)
    string = "l<<<" + string + '>>>'
    string = list(string.lower())
    l = []
    for i in range(len(string)):
        for j in range(len(alphabet)):
            if string[i] == alphabet[j]:
                if len(k := list(str(j))) != 1:
                    k1 = caracters[int(k[0])]
                    k2 = caracters[int(k[1])]
                    l.append("1")
                else:
                    k1 = caracters[0]
                    k2 = caracters[int(k[0])]
                    l.append("1")
                string[i] = k1+k2
    return f"{''.join(string)}"

def decrypt(string: str, key=None, caracters="*=(£é_ç$+}", alphabet="abcdefghijklmnopqrstuvwxyz1234567890,'.!:? "):
    string = string_set(string)
    alphabet = list(alphabet)
    caracters = list(caracters)

    for i in range(len(string)):
        if not string[i] in caracters:
            string.pop(i)

        for j in range(len(caracters)):
            try:
                if string[i] == caracters[j]:
                    for k in range(len(caracters)):
                        try:
                            if string[i+1] == caracters[k]: string[i] = alphabet[int(str(j)+str(k))]
                        except: pass
            except: pass

    go_string = []
    for i in range(len(string)):
        if is_even(i):
            go_string.append(string[i])

    string = "".join(go_string)
    return string
