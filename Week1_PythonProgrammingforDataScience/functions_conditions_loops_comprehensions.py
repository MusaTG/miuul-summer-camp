##############################################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
##############################################################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehensions


##########################
# FONKSİYONLAR (FUNCTİONS)
##########################

##########################
# Fonksiyon Okuryazarlığı
##########################

print("a")

# ?print # tanımın çıktısı

print("a", "b")

print("a", "b", sep="__")


##########################
# Fonksiyon Tanımla
##########################

def calculate(x):
    print(x * 2)


calculate(5)

# İki argümanlı/paranetreli bir fonksiyon tanımlayalım.


def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)
summer(8, 7)
summer(arg2=8, arg1=7)


##########################
# Docstring
##########################
# Ayarlardan docstring tarzı seçilebilir. (Python Integrad Tools)

def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    Examples:

    Notes:

    """
    print(arg1 + arg2)

# ?summer

summer(1, 3)


##########################
# Fonksiyonların Statement/Body Bölümü
##########################

# def functio_name(parameters/arguments):
#   statements (function body)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)


# girilen değerleri bir liste içinde saklayacak fonnksiyon

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


##########################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameteres/Arguments)
##########################

def divide(a, b):
    print(a/b)


divide(1, 2)

def divide(a, b=1):
    print(a/b)


divide(1)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb")


##########################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
##########################

# varm, miosture, charge

(56 + 15) / 80
(19 + 45) / 70
(52 + 45) / 90

# DRY
def calculate(varm, miosture, charge):
    print((varm + miosture)/charge)

calculate(98, 12, 78)


##########################
# Return:  Fonksiyon Çıktılarını Girdi Olarak Kullanmak
##########################

def calculate(varm, miosture, charge):
    return (varm + miosture)/charge


calculate(98, 12, 78) * 10

a = calculate(98,12,78)

def calculate(varm, miosture, charge):
    varm *= 2
    miosture *= 2
    charge *= 2
    output = (varm + miosture)/charge

    return varm, miosture, charge, output

calculate(98, 12, 78)
type(calculate(98, 12, 78))

varm, miosture, charge, output = calculate(98, 12, 78)

##########################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
##########################

def calculate(varm, miosture, charge):
    return int((varm + miosture)/charge)

calculate(98, 12, 7)

def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(45, 1)

def all_calculation(varm, miosture, charge, p):
    a = calculate(varm, miosture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)

def all_calculation(varm, miosture, charge, a, p):
    print(calculate(varm, miosture, charge))
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 19, 12)

##########################
# Local & Global Değişkenler (Local & Global Variables)
##########################

list_store = [1, 2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 9)