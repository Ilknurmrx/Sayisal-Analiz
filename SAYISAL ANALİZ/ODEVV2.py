x=2
max_iterasyon=4
for i in range(max_iterasyon):
    h=1e-5
    slope=(4*(2.71**(-0.5*(x+h)))-(4*(2.71**(-0.5*(x-h))))-2*h)/(2*h)
    x=x-((4*(2,71**(-0.5*x))-x)/slope)
print("cozum:", x)