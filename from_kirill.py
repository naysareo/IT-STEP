import random
import string
def srednee_arifmeticheskoe_list(*srednee):
    srednee_sum = 0
    simvoli = 0
    for i in srednee:
      srednee_sum += i
      simvoli += 1
    return srednee_sum/simvoli
def srednee_arifmeticheskoe_dict(*srednee):
    print(type(srednee),srednee)
    for i in srednee:
        print(i)
        for j in i:
            print(j)
    srednee_sum = 0
    simvoli = 0
 
dict_srednee = {random.choice(string.ascii_letters):random.randrange(100) for i in range(random.randrange(100))}
print(srednee_arifmeticheskoe_dict(dict_srednee))
list_srednee = [random.randrange(100) for i in range(random.randrange(100))]
print(f'{srednee_arifmeticheskoe_list(*list_srednee):.2f}')

'''
#задача
def gipotenuza2pifagor(katet_one,katet_two):
    return (katet_one**2) + (katet_two**2)
    
def vvod_vivod(vvod_one):
    dict_izmereniya = {'mm':1,'cm':10,'m':10000}
    index = dict_izmereniya.get(vvod_one)
    return index   
            
vvod_system_izmerenya = str(input('Enter system izmereniya \'cm\',\'mm\' or \'m\'\n'))

one_katet = int(input('Enter katet one in cm'))
two_katet = int(input('Enter katet two in cm'))
print(gipotenuza2pifagor(one_katet,two_katet) * vvod_vivod(vvod_system_izmerenya))
'''
