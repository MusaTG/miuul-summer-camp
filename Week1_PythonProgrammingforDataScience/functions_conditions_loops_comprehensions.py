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


##############################################################################
# KOŞULLAR (CONDITIONS)
##############################################################################

# True-False Hatırlatma

1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 1

if number == 10:
    print("number is 10")

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)

##########################
# else
##########################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(11)

##########################
# elif
##########################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(11)


##########################
# DÖNGÜLER (LOOPS)
##########################

# for loop

students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student)


for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 / 100 + salary))

for salary in salaries:
    print(int(salary * 30 / 100 + salary))

for salary in salaries:
    print(int(salary * 50 / 100 + salary))

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 10))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))


##########################
# Uygulama - Mülakat Sorusu
##########################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

for i in range(0,5):
    print(i)

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    return new_string


result = alternating("hi my name is john and i am learning python")


##########################
# Break & Continue & While
##########################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in  salaries:
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while

number = 1
while number < 5:
    print(number)
    number += 1


##########################
# Enumerate: Otomatik Counter/Indexer ile for loop
##########################

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

# for index, student in enumerate(students, 1):
for index, student in enumerate(students):
        print(index,student)


A = []
B = []

for index, student in enumerate(students):
    if index % 2 ==0:
        A.append(student)
    else:
        B.append(student)


##########################
# Uygulama - Mülakat Sorusu
##########################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek inddexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]


##########################
# Alternating fonksiyonunun enumerate ile yazılması
##########################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")


##########################
# Zip
##########################

students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

list(zip(students,departments,ages))


##########################
# Lambda & Map & Filter & Reduce
##########################

# lambda == kullan at
def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b
new_sum(3, 5)


# map == döngüden kurtarır

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5500)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

list(map(lambda x: x * 20 / 100 + x, salaries))

list(map(lambda x: x ** 2, salaries))


# FILTER

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))


# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)


##############################################################################
# COMPREHENSIONS
##############################################################################

##########################
# List Comprehension
##########################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

##########################
# Dict Comprehension
##########################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

##########################
# Uygulama - Mülakat Sorusu
##########################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
# Key'ler orjinal değerler value'ler ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}


#########################################
# List & Dict Comprehension Uygulamalar
#########################################

##########################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
##########################

# before:
# ['total','speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'is_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
   A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

##########################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
##########################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']


[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


##########################
# Amaç keyi string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenleri için yapmak istiyoruz.
##########################

# output:
# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_losses': ['mean', 'min', 'max', 'var']

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"] # o ifade object yani kategoriktir
soz = {}
agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)
