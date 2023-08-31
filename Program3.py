# Vi ska skriva ett program (konsolapplikation) som frågar användaren om:
# Namn
# Ålder
# Antal djur som den äger
# Adress
# Bruttolön

# Programmet ska sedan skriva ut:
# Hej på dig <Namn>
# Du är <Ålder> och om 10 år kommer du vara <ålder + 10>
# Att du har djur är <True, False>
# Du bor på <Adress>
# Och efter skatt tjänar du <Bruttolön * 0.31>

namn = input('Skriv ditt namn: ')
age = input('Skriv in din ålder: ')
antal_djur = input('Skriv in antal djur du har: ')
adress = input('Skriv in din adress: ')
lön = input('Skriv in din lön: ')

print('Hej på dig ' + namn)
age_10 = int(age) + 10
print('Du är '+ age +' och om 10 år kommer du vara ', int(age)+10)
# print('Du är '+ age +' och om 10 år kommer du vara ', age_10)
# print(f'Du är {age} och om 10 år kommer du vara {int(age) + 10}')
# print('Du är {} och om 10 år kommer du vara {}'.format(age, int(age)+10))
print('Att du har djur är ', int(antal_djur) > 0)
print('Du bor på', adress)
print('Och efter skatt tjänar du', int(lön)*0.69)
