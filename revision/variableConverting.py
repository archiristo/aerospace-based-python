##Değişken çevirme
fuel_remaining = 24.8
oxygen_level = 45

print(int(fuel_remaining))
print(float(oxygen_level))

#Bir dizilimde veri gösterimi
name = "Samira"
numbers = [1, 2, 3, 4, 5]

print(numbers[2])
print(name[3])

sliced_numbers = numbers[2:]
print(sliced_numbers)

#2 boyutlu veri dizisinde veri gösterimi
twod_array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

value1 = twod_array[0][1]
value2 = twod_array[2][2]
print(value1, value2)

#Listede veri değiştirme
num = [1, 2, 3, 4, 5]
num[1] = 9
print(num)

#Listeden veri çıkarma
n = [1, 2, 3, 4, 5]
del(n[3])
print(n)

#Listeye veri ekleme
nmb = [1, 2, 3, 4, 5]
nmb.append(6)
print(nmb)

#Listenin tersini alma
nmbr = [1, 2, 3, 4, 5]
cnv = nmbr[::-1]
print(cnv)

##Deneme
ary = [1, 2, 3, 4, 5]
# 4, 3, 8, 1, 5, 9 olacak. 
del(ary[4])
ary[1] = 8
reverse_ary = ary[::-1]
reverse_ary.append(5)
reverse_ary.append(9)
print(reverse_ary)

#input
isim = input("enter your name: ")
print("hi", isim)