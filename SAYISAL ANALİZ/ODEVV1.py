a=1
b=2
tolerans = 1e-6
max_iterasyonlar=4
iterasyon_sonucu=(a+b)/2
for _ in range(max_iterasyonlar):
    c=(a+b)/2
denklem_sonucu_c=c**3 - 4*c**2 - 10 
if denklem_sonucu_c ==0:
    iterasyon_sonucu=c
   
elif denklem_sonucu_c*(a**3-4*a**2 -10):
    b=c
else:
    a=c
iterasyon_sonucu=(a+b)/2
print(f"cozum:{iterasyon_sonucu}")