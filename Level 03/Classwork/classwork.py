# Task1. შექმენით 1 int ტიპის ცვლადი, 1 float ტიპის ცვლადი, მიამატეთ ერთმანეთს და კომენტარის სახით თქვენი სიტყვებით ახსენით როგორი ტიპის პასუხი გამოაქვს და რატომ 

num1 = 10
num2 = 15.5
print(num1 + num2)     #int + float გამოვიდა float რადგან int გახდა float 10 > 10.5

# Task2. შექმენით 2 boolean ტიპის ცვლადი და int() ფუნქციის გამოყენებით მიამატეთ ერთმანეთს, კომენტარის სახით თქვენი სიტყვებით ახსენით რატომ გამოვიდა ის პასუხი რაც გამოიტანა

num1 = True
num2 = False 
print(int(num1) + int(num2))     #ტერმინალმა გამოიტანა 1 რადგან True უდრის 1; ხოლო False უდრის 0 | 1+0=1

# Task3. შექმენით 2 int ტიპის ცვლადი, ერთის მნიშვნელობა იყოს 20, ერთის 24 და გამოიტანეთ 2024.

num1 = 20
num2 = 24
print(str(num1) + str(num2))