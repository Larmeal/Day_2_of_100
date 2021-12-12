# คำนวณเงินที่ต้องจ่ายใน 1 บิล ว่าแต่ละคนต้องจ่ายเงินกี่บาท

print("Welcome to the tip calculator.")
Bill = float(input("What was the total bill? $"))

Tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
result = (Bill * (Tip / 100)) + Bill

People = input("How many people to split the bill? ")
final_result = round(float(result) / float(People), 2)

print(f"Each person should pay: ${final_result}")