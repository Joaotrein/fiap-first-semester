TempoAnos = float(input("Digite o número de anos fumando: "))
ValorMaço = float(input("Digite o valor do maço do cigarro: "))
MaçosDiarios = float(input("Digite o número de maços fumados por dia: "))

if TempoAnos < 0 or ValorMaço < 0 or MaçosDiarios < 0:
     print("O valor dos dados precisam ser maiores que 0")
     
else: 
     montante = ValorMaço * MaçosDiarios * TempoAnos * 365  

     if montante < 20000:
      print("Com o valor R${}, você poderia ter dado entrada em um carro.".format(montante))
     elif 20000 <= montante < 50000:  
      print("Com o valor R${}, você poderia ter comprado um carro popular usado.".format(montante))
     elif montante >= 50000:
      print("Com o valor R${}, você poderia ter comprado um carro zero.".format(montante))

