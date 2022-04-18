import random #匯入模組才能使用裡面的函式庫

print("終極密碼遊戲開始")
num=random.randint(1,100)

guess=0 #預設值，不在亂數範圍內就行
while num != guess:
    guess=int(input("請猜一個數字(0~100): "))
    if guess>num:
        print("數字小一點")
    if guess<num:
        print("數字大一點")
print("恭喜，答案是: ",num)