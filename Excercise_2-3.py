# คำนวณวันตาย โดยให้ทุกคนมีอายุอยู่ที่ 90 ปี

age = input("What is your current age? ")

final_age = 90 - int(age)
Day = final_age * 365
Week = final_age * 52
Month = final_age * 12
print(f"You have {Day} days, {Week} weeks, and {Month} months left.")