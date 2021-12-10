Capitals={} 
Capitals = dict() 
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Countries=input("Введи страну: ") 
if Countries in Capitals:
    print('Столица страны ' + Countries + ': ' + Capitals[Countries])
else:
    print('В базе нет страны c названием ' + Countries)

