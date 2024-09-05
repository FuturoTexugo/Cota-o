def decimal(numero):
    if numero == 0:
        return "0"
    binario = ""
   
    while numero >0:
        binario = str(numero%2) + binario
        numero = numero//2
    return binario

num_decimal = int(input("digite um numero decimal"))
binario = decimal(num_decimal)
print(f"O numero decimal {num_decimal} em binário é {binario}")