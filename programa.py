print("CALCULE O VALOR FINAL DE UMA CONTA DE LUZ")
print("-----------------------------------------")
print("                                         ")

# Recebe os dados: 

kwh = float(input("kWh consumidos: "))

op = 0
print("Escolha uma bandeira")
if op != 6:
    print("=-"*15)
    print("Escolha uma bandeira")
    print("""    
    [ 1 ] Verde
    [ 2 ] Amarela
    [ 3 ] Vermelha 1
    [ 4 ] Vermelha 2
    [ 5 ] Escassez Hídrica
    """)
    print("=-" * 15)
    op = int(input(">>>> Bandeira: "))
    if op == 1:
        valorkwh = 0.618050
    elif op == 2:
        valorkwh = 0.636790
    if op == 3:
        valorkwh = 0.657760
    elif op == 4:
        valorkwh = 0.712970
    if op == 5:
       valorkwh = 0.760050

    elif op < 1 or op >= 6:
        print("Opção inválida. Tente Novamente")


# Calculando

valor_simples = kwh * valorkwh # Obtem os valores sem impostos

percentual = 34.11 / 100.0  # Define a porcentagem dos impostos

tarifa_com_imposto = valorkwh / (1 - percentual) # Calcula o valor dos impostos

valor_com_imposto = kwh * tarifa_com_imposto # Multiplica para obter o valor com impostos


percentual_luz = 15.0 / 100.0 # Define a taxa de iluminação publica

ilum = (percentual_luz * valor_com_imposto) #Valor com ilum. publica

valor_final = valor_com_imposto + ilum # Obtém o valor final

 



# Imprime na tela

print("Valor de cada kwh: ")
print("{:.6f}".format(valorkwh))

print("Valor sem impostos")
print("{:.2f}".format(valor_simples))

print("Valor com impostos: ")
print("{:.2f}".format(valor_com_imposto))


print("Valor ilum: ")
print("{:.2f}".format(ilum))

print("Valor final: ")
print("{:.2f}".format(valor_final))


# Escreve no arquivo TXT

Arquivo = open('conta-luz.txt', 'w')

Arquivo.write(" VALOR DE UMA CONTA DE LUZ \n")
Arquivo.write("--------------------------- \n")
Arquivo.write("             \n")

Arquivo.write(" Consumo: ")
Arquivo.write("{:.2f} kWh".format(kwh))
Arquivo.write(" \n") 
Arquivo.write("             \n") 

Arquivo.write(" Valor de cada kwh: ")
Arquivo.write("R$ {:.2f}".format(valorkwh)) 
Arquivo.write(" \n")
Arquivo.write("                \n")

Arquivo.write(" Taxa de Iluminacao Publica: ")
Arquivo.write("R$ {:.2f}".format(ilum))
Arquivo.write(" \n")
Arquivo.write("                \n")

Arquivo.write(" Valor com impostos: ")
Arquivo.write(" R$ {:.2f}".format(valor_com_imposto)) 
Arquivo.write(" \n")
Arquivo.write("                \n")

Arquivo.write(" Valor sem impostos: ")
Arquivo.write(" R$ {:.2f}".format(valor_simples))
Arquivo.write(" \n") 
Arquivo.write("             \n") 

Arquivo.write(" Valor final: ")
Arquivo.write("R$ {:.2f}".format(valor_final))



Arquivo.close()

