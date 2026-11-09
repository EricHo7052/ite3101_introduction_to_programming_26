def cube(number: float) -> float:
    return number * number * number


def by_three(number: float) -> float:
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print(by_three(9))
