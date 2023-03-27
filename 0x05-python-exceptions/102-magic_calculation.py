def magic_calculation(a, b):
    a = 2
    b = 3
    result = 0
    for i in range(94, 103):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except:
            result += a + b
            break
    return result
