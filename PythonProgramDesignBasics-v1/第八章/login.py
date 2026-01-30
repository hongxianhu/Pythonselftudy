# 登录名制作器
def get_login_name(first: str, last: str, idnumber: str) -> str:
    """"""
    set1 = first[:3]

    set2 = last[:3]

    set3 = idnumber[-3:]

    login_name = set1 + set2 + set3

    return login_name




# 密码验证器
def valid_password(password: str) -> bool:
    correct_lenght = False
    has_uppercase = False
    has_lowercase = False
    has_dight = False
    if len(password) >= 7:
        correct_lenght = True
        
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_dight = True

    if correct_lenght and has_uppercase and has_lowercase and has_dight:
        is_valid = True
    else:
        is_valid = False

    return is_valid
valid_password("Leopard6")
