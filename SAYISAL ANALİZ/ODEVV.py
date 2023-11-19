a=2
b=4
tolerans = 1e-6
max_iterasyonlar=4
iterasyon_sonucu=(a+b)/2
for _ in range(max_iterasyonlar):
    c=(a+b)/2
denklem_sonucu_c=c**3 - 2*c**2 - 5 
if denklem_sonucu_c < tolerans:
    iterasyon_sonucu=c
   
elif denklem_sonucu_c*(a**3-2*a**2-5)<0:
    b=c
else:
    a=c
iterasyon_sonucu=(a+b)/2
print(f"cozum:{iterasyon_sonucu}")