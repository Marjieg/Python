#pintar cuadrado con *
a=int(input('introduce la altura'))
for i in range(0,a,1):
    for j in range(1,a,1):
        print('*',end=' ')
    print('*')

#otra forma
alt=int(input('introduce la altura'))
for i in range(0,alt):
    print('* '*alt)