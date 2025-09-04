nota = float(input("digite a nota "))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))
nota4 = float(input("digite a quarta nota"))
media = (nota + nota2 + nota3 + nota4)/4
print(media)
if media >=7.0:
    print("aprovado")
elif media>= 5.0 and 7.0:
    print("recuperação")  
else:
    print("reprovado")      