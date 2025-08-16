def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step == 0:
        return numbers
    elif step > 0:
        for i in range(step):
            temp = numbers.pop()
            numbers.insert(0, temp)
        return numbers
    else:
        numbers.reverse()
        for i in range(abs(step)):
            temp = numbers.pop()
            numbers.insert(0, temp)
        numbers.reverse()    
        return numbers