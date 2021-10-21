def zarplata():
    t=int(input('Введите выработку в часах: '))
    st=int(input('Введите ставку за час: '))
    p=int(input('Введите премию: '))
    z = t * st + p
    return z
