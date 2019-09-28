print('Hello, Django girls!')
if 3 > 2:
    print('To dziala!')
if 5 >2:
    print('jest jednak wieksze od 2')
name = 'Sonja 15'
if name == 'Ola' :
    print('Hej Ola!')
elif name == 'Sonja':
    print('Hej Sonja!')
else:
    print('Hej anonimie!')
volume = 57
if volume < 20 :
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("Perfect,I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
elif 40 <= volume < 60:
    print("Nice to hear it")
else:
    print("My ears are hurting!:(")  # uszy bola bo glasno spiewa
#bkdsosoek 

def hi():
    print('Hej!')
    print('Jak sie masz?')
hi()
hi()

def hi(imie):
    if imie == 'Bianka':
        print('Hej Bianka!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')
hi('Bianka')


def hi(imie):
    print('Hej' + "Rachel" + '!')
hi("Rachel")

def hi(imie):
    print('Witaj' + imie + '!')
dziewczyny = ['Ania', 'Zosia', 'Tosia', 'Franek', 'Basia']   
for imie2 in dziewczyny:
    hi(imie2)
    print('Kolejna dziewczyna')
for i in range(1, 10):
    print(i)


