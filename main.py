#프로젝트 목적: 클래스를 써보고 싶어서...
#내용: FC 온라인 강화 시뮬레이션을 하며 자신의 운을 테스트 할 수 있다.

import random


percentage = {
    2 : 100 , 3 : 81 , 4 : 64, 5 : 50, 6 : 26, 7 : 15, 8 : 7, 9 : 4, 10 : 2
} # 5칸 채울 시 강화 성공확률 ex) 2:100 => 2카 강화 5칸 채울 시 100퍼센트 확률로 성공


first = int(input("몇 카 강화할 거야? ( Ex) 4 -> 5 강화진행은 숫자 5만 입력)")) 
second = float(input("몇 칸 채워? ( Ex) 5칸 다 채울거면 숫자 5만 입력 , 2.5칸 채울거면 숫자 2.5만 입력"))

first_input = percentage[first] 
real_percentage = first_input*second/5
print(f"성공확률은 {real_percentage}%입니다")

question = input("시도하시겠습니까? (y/n)")

on = ""

if question == "y":
    on = True
else:
    on = False



class reinforce:
    def __init__(self,real_percentage):
        self.per = real_percentage
        self.weights = [real_percentage, 100-real_percentage]
        self.result = random.choices(["Success","Failure"],self.weights )[0]
 

while on == True:
    resul = reinforce(real_percentage)
    print(resul.result)
    re = input("다시 시도하시겠습니까? (y/n)")
    if re == "n":
        on = False
        








