# main.py

import functions# functions.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "無法除以零"
    
def square(a):
    return a * a

print("=== 簡易計算機 ===")
print("請選擇運算方式：")
print("1. 加法")
print("2. 減法")
print("3. 乘法")
print("4. 除法")
print("5. 平方")

choice = input("輸入選項 (1/2/3/4/5): ")

a = float(input("輸入第一個數字: "))
if choice != '5':
    b = float(input("輸入第二個數字: "))

if choice == '1':
    result = functions.add(a, b)
elif choice == '2':
    result = functions.subtract(a, b)
elif choice == '3':
    result = functions.multiply(a, b)
elif choice == '4':
    result = functions.divide(a, b)
elif choice == '5':
    result = functions.square(a)
else:
    result = "輸入錯誤"

print("結果:", result)
