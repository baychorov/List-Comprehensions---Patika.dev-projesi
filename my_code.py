# List-Comprehensions---Patika.dev-projesi
#patika dev akademi list comprehensions için oluşturulmuş hackerrank alıştırmasının çözümü

i = int(input("x = "))
j = int(input("y = "))
k = int(input("z = "))
n = i+j+k
#listler oluşturulurken bu değerler kullanılacak.
#bütün permütasyonları oluşturmak için input olarak aldığımız bütün sayıları döngüye sokarak listeler oluşturalım ve yalnızca geçerli koşuldakileri alalım.
valid_permutations = [[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if x+y+z != n]
print(valid_permutations)
#bütün permütasyonlar içinden yalnızca elemanları toplamları n değerinden küçük olan listler alındı 
