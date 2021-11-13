


#实现登录功能

def login(username,password):

    if username is None or username == '':
        return "用户名不能为空"
    if password is None or password == '':
        return "密码不能为空"

    if username == "admin" and password =="123456":
        return "登录成功"
    else:
        return "登录失败"


def age(age):
    if age < 2:
        return "baby"
    elif age >=2 and age < 4:
        return "learning walk"
    elif age >=4 and age < 13:
        return "child"
    elif age >= 13 and age < 20:
        return "teenager"
    elif age >= 20 and age < 65:
        return "adult"
    else:
        return "the aged"
age(1)