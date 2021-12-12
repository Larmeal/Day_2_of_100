# คำนวณค่า BMI

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = float(weight)
BMI = new_weight / (new_height ** 2)
result = int(BMI)
print(result)
