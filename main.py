password = input()

def ask_password(password):
    count = 0
    correct_password = "12345"
    while (True):
        if (password == correct_password):
            print("Доступ разрешён")
            break
        else:
            print("Пароли не совпадают")
            password = input()
            count+=1
            if count ==3:
                print("net popitka")
                break
print(ask_password(password))
jhvkghcvkj
khvjgvjk.