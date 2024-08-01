soldado = (1, 2, 3)
capitao = (1, 2, 3, 4, 5 )
tenente = (2, 3, 5)
marinha = ()  

cargo = input("Insira seu cargo sem acentos e tudo minúsculo: ")
dia = int(input("Insira o dia da semana de 1 a 5 para segunda a sexta: "))

dias_permitidos = {
    "soldado": [1, 2, 3],  
    "tenente": [2, 4, 5], 
    "marinha": [] 
}
if cargo == "soldado" and dia in soldado:
    print("Acesso permitido!")
elif cargo == "capitao":
    print("Acesso permitido!")
elif cargo == "tenente" and dia in tenente:
    print("Acesso permitido!")
elif cargo == "marinha" and dia in marinha:
    print("Acesso permitido!")
else:
    print("SUMMAAAAAA DAQUIIIIII!")