from random import *
from re import A

# list = ["apple", "banana", "orange"]

# quiz = list[randrange(0,len(list))]
quiz = "apple"
print("현재 단어 :", quiz)
quiz_pr = quiz

a = input("알파벳을 입력하세요 :")

for i in range(0,len(quiz)):
    print(quiz[i])
