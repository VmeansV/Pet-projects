def verification(login, password, success, failure):
    s1 = any(ch.islower() for ch in password)
    s2 = any(ch.isupper() for ch in password)
    s3 = any(ch.isdigit() for ch in password)
    s4 = any(ch.isalpha() for ch in password)
    res = s1 and s2 and s3 and s4
    if res:
        success(login)
    else:
        if not s4:
            text = "в пароле нет ни одной буквы"
            failure(login, text)
        if not s2:
            text = "в пароле нет ни одной заглавной буквы"
            failure(login, text)
        if not s1:
            text = "в пароле нет ни одной строчной буквы"
            failure(login, text)
        if not s3:
            text = "в пароле нет ни одной цифры"
            failure(login, text)

в пароле нет ни одной буквы
в пароле нет ни одной заглавной буквы
в пароле нет ни одной строчной буквы
в пароле нет ни одной цифры

