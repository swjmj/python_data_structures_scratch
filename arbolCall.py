from ARBOL import ARBOL

a = ARBOL(50)

a.insert(30)
a.insert(60)
a.insert(20)
a.insert(90)
a.insert(55)
a.insert(45)
a.insert(345)
a.insert(12)
a.insert(74)


print('--------------------------')
# cont = False
# while cont == False:
#     print('Que número quieres meter?')
#     r = eval(input())

#     if isinstance(r, str):
#         cont = True
#     else:
#         a.insert(r)

print('Los valores en el arbol In-order:')
a.printTreeIn()

print('Los valores en el arbol Pre-order:')
a.printTreePre()

print('Los valores en el arbol Post-order:')
a.printTreePost()

print('--------------------------')
n = 16
print('Buscando el número ', n)
print(a.search(n))
