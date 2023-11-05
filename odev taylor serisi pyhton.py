import numpy 

x=numpy.pi/5

asil_cos_x = numpy.cos(x)
print(f"asil cos({x}): {asil_cos_x}")

taylor_tek_terim=1
taylor_iki_terim=1-(x**2)/2

print(f"tek terimlik yaklasim(cos({x}))~{taylor_tek_terim}")
print(f"iki terimlik yaklasim (cos({x}))~{taylor_iki_terim}")

kesme_hatasi1= abs(asil_cos_x - taylor_tek_terim)
kesme_hatasi2 = abs(asil_cos_x - taylor_iki_terim)

print(f"cosx tek terimli acilimindaki Kesme Hatası: {kesme_hatasi1}")
print(f"cosx iki terimli acilimindaki Kesme Hatası: {kesme_hatasi2}")