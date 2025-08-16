def is_good_password(string):
    lower_letters =  'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопстуфхцчшщъыьэюя'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПСТУФХЦЧШЩЪЫЬЭЮЯ'
    digits = '0123456789'
    result = True
    r1 = False
    r2 = False
    r3 = False
    if len(string) < 9:
        result = False
        return result
    for i in string:
        if i in lower_letters:
            r1 = True
        if i in upper_letters:
            r2 = True
        if i in digits:
            r3 = True
    if all([r1, r2, r3]):
        result = True
    else:
        result = False
    return result