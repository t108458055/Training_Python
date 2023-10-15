# 印出 1 加 10的結果
def SumTotal():
  j = 0
  for i in range(1,11):
    j += i
  return j

print("從1加到10 :", SumTotal())

# 算式計算
def Calcultor():
  return ((5 + 3) * (18 -2))/(15 - 10)

print("算式計算：", Calcultor())

# 印出 1小時又 10分鐘總共有幾秒
def CovertSecond():
  return (60*60*60+10*60)

print("總共幾秒 :", CovertSecond())
# 
def predict_population(year):
    # 已知數據
    initial_population = 50  # 1987年的人口（單位： 億人）
    final_population = 60    # 1999年的人口（單位：億人）
    years = 12               # 1987年到1999年的年數

    # 計算年均成長率
    annual_growth_rate = (final_population - initial_population) / years

    # 計算預估人口數量
    predicted_population = initial_population + annual_growth_rate * (year - 1987)

    return predicted_population

# 預測人口數量
year_2023 = 2029
predicted_population_2023 = predict_population(year_2023)

print(f"{year_2023}年的預測人口總數為: {predicted_population_2023} 億人。")

#
num = type(1000)
print(num)