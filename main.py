'''
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét 



0 tetszőleges paraméter: négyzet, 

1 tetszőleges paraméter: téglalap, 

2 tetszőleges paraméter: háromszőg, 

3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''


def kerulet(kotelezo, *oldalhossz):
    if len(oldalhossz) == 0:
        return f'a negyzet kerulete: {4*kotelezo} cm'
    elif len(oldalhossz) == 1:
        return f'a teglalap kerulete: {kotelezo * sum(oldalhossz)} cm'
    elif len(oldalhossz) == 2:
        return f'a haromszog kerulete: {kotelezo + sum( oldalhossz)} cm'
    elif len(oldalhossz) == 3:
        return f'a sokszog kerülete: {kotelezo + sum(oldalhossz)} cm'

print(kerulet(4))
print(kerulet(4,9))
print(kerulet(4,9,4))
print(kerulet(4,9,4,10))