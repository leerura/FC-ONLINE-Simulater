#내용: 강화 100번 진행했을 때 성공횟수와 실패횟수를 알려준다.

import random
from collections import Counter

percentage = {
    2 : 100 , 3 : 81 , 4 : 64, 5 : 50, 6 : 26, 7 : 15, 8 : 7, 9 : 4, 10 : 2
}


first = int(input("몇 카 강화할 거야?"))
second = float(input("몇 칸 채워?"))

first_input = percentage[first]
real_percentage = first_input*second/5

class reinforce:
    def __init__(self,real_percentage):
        self.per = real_percentage
        self.weights = [real_percentage, 100-real_percentage]
        self.result = [random.choices(["Success","Failure"],self.weights )[0] for i in range(100)]

re = reinforce(real_percentage)

resul = Counter(re.result)
print(resul)