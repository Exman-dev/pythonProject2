def check_pc(pc):
    """
    Checks if the personal code of a pacient is valid
    :param pc:
    :return:
    """
    k = 0
    while pc > 0:
        pc = pc // 10
        k = k + 1
    if k == 13:
        return True
    else:
        return False

def form_age(pc):
    """
    Calculates the age of a patient
    :param pc:
    :return:
    """
    f = pc // 1000000000000
    if f <= 2:
        k = pc // 10000000000 % 100
        age = 2021 - (1900 + k)
    else:
        k = pc // 10000000000 % 100
        age = 2021 - (2000 + k)
    return age