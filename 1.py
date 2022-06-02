year=int(input(f"나이를 입력하시오:"))
age=2020-year+1
print(age)
if 19<age<27: print("대")
elif 16<age<20: print("고")
elif 13<age<17:  print("중")
elif 7<age<14: print("초")
else: print("학생이 아닙니다")