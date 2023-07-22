##############################################################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON
##############################################################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)
import matplotlib
################################################
# NUMPY
################################################

# Neden NumPy? (Why NumPy?)
# NumPy Array'i Oluşturmak (Creating NumPy Arrays)
# NumPy Array Özellikleri (Attibutes of NumPy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# NumPy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

import numpy as np

###############################
# Neden NumPy?
###############################

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

###############################
# NumPy Array'i Oluşturmak
###############################

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))


###############################
# NumPy Array Özellikleri
###############################
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype


###############################
# Yeniden Şekillendirme (Reshaping)
###############################

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


###############################
# Index Seçimi (Index Selection)
###############################

a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[2, 3] = 999
m[2, 3] = 2.9 # 2 olarak kaydeder fix type yani sabit tip np!!!

m[:, 0]
m[1:, ]
m[0:2, 0:3]

###############################
# Fancy Index
###############################

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1, 2, 3]
v[catch]


###############################
# NumPy'da Koşullu İşlemler (Conditions on Numpy)
###############################

v = np.array([1, 2, 3, 4, 5])

##########################
# Klasik döngü ile
##########################

ab = []
for i in v:
    if i < 3:
        ab.append(i)

##########################
# NumPy ile
##########################
v < 3
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]


###############################
# Matematiksel İşlemler (Mathematical Operations)
###############################

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

###############################
# NumPy ile iki bilinmeyenli denklem çözümü
###############################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)


################################################
# PANDAS
################################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri


##########################
# Pandas Series
##########################

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
s.head(3)
s.tail(3)


##########################
# Veri Okuma (Reading Data)
##########################

df = pd.read_csv("Week1_PythonProgrammingforDataScience/datasets/advertising.csv")
df.head()


##########################
# Veriye Hızlı Bakış (Quick Look at Data)
##########################

import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull()
df.isnull().values.any()
df.isnull().sum()
df['sex'].head()
df['sex'].value_counts()


##########################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
##########################

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head()
# df = df.drop(delete_indexes, axis=0) # Kalıcı değiştitrme
# df.drop(delete_indexes, axis=0, inplace=True) # Kalıcı değiştitrme


##########################
# Değişkeni Indexe Çevirmek
##########################

df['age'].head()
df.age.head()

df.index = df.age
df.index

df.drop('age', axis=1).head()
df.drop('age', axis=1, inplace=True)
df.head()

##########################
# Indexi Değişkene Çevirmek
##########################

df.index
df['age'] = df.index
df.head()

df.drop('age', axis=1, inplace=True)
df = df.reset_index()
df.head()


##########################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
##########################

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df['age'].head()
df.age.head()
type(df['age'].head()) # Series

df[['age']].head()
type(df[['age']].head()) # DataFrame

df[['age', 'alive']].head()

col_names = ['age', 'adult_male', 'alive']
df[col_names]

df['age2'] = df['age'] ** 2
df.head()
df['age3'] = df['age'] / df['age2']

df.drop('age3', axis=1).head()
df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains('age')].head()


##########################
# iloc & loc
##########################

df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3]
df.iloc[0, 0]

# iloc: label based selection
df.loc[0:3]


df.iloc[0:3, 'age'] # hatalı
df.iloc[:3, :3]

df.loc[:3, 'age']

col_names = ["age", "embarked", "alive"]
df.loc[:3, col_names]


##########################
# Koşullu Seçim (Conditional Selection)
##########################

df = sns.load_dataset("titanic")
df.head()

df[df["age"]>50].head()
df[df["age"]>50].age.count()

df.loc[df["age"]>50, ["class", 'age']].head()

df.loc[(df["age"] > 50) & (df['sex'] == "male"), ["class", 'age']].head()

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
       & (df['sex'] == "male")
       & ((df.embark_town == "Cherbourg") | (df.embark_town == "Southampton")),
        ["class", 'age', 'embark_town']]

df_new["embark_town"].value_counts()


##########################
# Toplulaştırma & Gruplama (Aggreation & Grouping)
##########################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

df = sns.load_dataset("titanic")
df.head()

df.age.mean()

df.groupby('sex')["age"].mean()
df.groupby('sex').agg({"age": "mean"})

df.groupby('sex').agg({"age": ["mean", "sum"]})

df.groupby('sex').agg({"age": ["mean", "sum"],
                       "embark_town": "count"})

df.groupby('sex').agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(['sex', "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(['sex', "embark_town", 'class']).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(['sex', "embark_town", 'class']).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})


##########################
# Pivot Table
##########################

df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", 'embarked') # ön tanımlı mean alınır

df.pivot_table("survived", "sex", 'embarked', aggfunc="std")
df.pivot_table("survived", "sex", ['embarked', 'class'], aggfunc="std")

df["new_age"] = pd.cut(df['age'], [0, 10, 18, 25, 40, 90])

df.pivot_table('survived', 'sex', 'new_age')

df.pivot_table('survived', 'sex', ['new_age', 'class'])

pd.set_option('display.width', 500)


##########################
# Apply ve Lambda
##########################

df = sns.load_dataset("titanic")
df.head()

df['age2'] = df['age'] * 2
df['age3'] = df['age'] * 5

(df['age']/10).head()
(df['age2']/10).head()
(df['age3']/10).head()

for col in df.columns:
    if "age" in col:
        print(col)


for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df[['age', 'age2', 'age3']].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains('age')].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains('age')].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains('age')].apply(standart_scaler).head()

# df.loc[:, ['age', 'age2', 'age3']] = df.loc[:, df.columns.str.contains('age')].apply(standart_scaler)

df.loc[:, df.columns.str.contains('age')] = df.loc[:, df.columns.str.contains('age')].apply(standart_scaler)

df.head()


##########################
# Birleştirme (Join) İşlemleri
##########################

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

pd.concat([df1, df2], axis=1)


##########################
# Merge ile Birleştirme İşlemleri
##########################

df1 = pd.DataFrame({'employees': ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({'employees': ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4)
