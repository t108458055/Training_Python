# PY 基本型態
# 內建型態 四種 1.數值 2.字串 3.容器 4.布林
import sys
## 1. 數值型態 : int, float, complex
# 整數 (int)
i = 99 
print(i,"之型態:",type(i))
print("整數最大值:",sys.maxsize)
print("整數最小值:",-sys.maxsize - 1)
# 浮點數 (float)
f = 999.99
print(f,"之型態:",type(f))
print("浮點數最大值:",sys.float_info.max)
print("浮點數最小值:",-sys.float_info.min)
# 複合數 complex
c = 1+2j
print(c, "是複合數?", isinstance(1+2j,complex))

# 2.字串型態: str, chr 
# chr():把 ASCII 中的數字轉換成字元
# 把ASCII 中的數字轉換成字元
# numASCII = input("請輸入ASCII數字:")
numASCII = 65
print("ASCII數字:", numASCII)
print("字元:",chr(int(numASCII)))

# 3.容器 list dict tuple 
# List (串列) #有順序可以改變
list_de =  ['a','b','c','d','e','f','g']
print("List:", list_de)
print("List[3]:", list_de[3])
# 元組 tuple (序對) #有順序不可以改變
tuple_de = (0,1,2,3,4,5,6,7,8,9)
print("Tuple:", tuple_de)
print("Tuple[3]:",tuple_de[3])
# 把元組中第2個 ~ 第4個資料(到第4個但不包含第4個)拿出來
print("Tuple[1:3]:",tuple_de[1:3])
#  字典 dict 
dict_de = {'age':35, 'name':'Andy', 'Nation':'Taiwan'}
print("dict['name']:", dict_de['name'])


#溫度轉換公式
celsius =  float(input('請輸入溫度(攝氏)°C: '))
fahrenheit =(celsius *1.8) + 32
print('溫度(華氏):%.2f' % fahrenheit, "°F")

