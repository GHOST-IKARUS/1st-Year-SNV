print("Saisir les paramètres a,b,c de votre polynome du second degré:")
a=float(input("Saisir la valeur de a="))
b=float(input("Saisir la valeur de b="))
c=float(input("Saisir la valeur de c="))

#calcul de delta
delta=b**2-4*a*c

#affichage
print("Résolution de l'équation ",a,"x² + ",b,"x + ",c)

# condition sur delta dans cet ordre >0 puis ==0 puis <0
if delta>0:
    x1=(-b-delta**0.5)/(2*a)
    x2=(-b+delta**0.5)/(2*a)
    print("Delta est positif donc il y a 2 solutions")
    print("x1 =",x1)
    print("x2 =",x2)
else:
    if delta==0:
        x0=-b/(2*a)
        print("Delta est nul donc il y a 1 solution unique")
        print("x0 =",x0)
    else:
        print("Pas de solution dans l'espace des réel")