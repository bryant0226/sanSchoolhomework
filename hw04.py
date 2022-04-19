#質數為可被1和自己整除的數
for i in range(2,101):
    prime_number=True#事先假設進來的是數字都是質數，所以設為True
    for x in range(2,i):
        if i%x == 0:
            prime_number=False
    if prime_number:
        print(i,"為質數")

