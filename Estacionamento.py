def inicio():
  veiculo = input("\n> Tipo de veículo (moto | carro | caminhonete): ")
  veiculo = veiculo.lower()
  estacionamento = input("\n> Estacionamento coberto? (s/n): ")
  estacionamento = estacionamento.lower() 
  tempo = input("\n> Calcular por horas ou dias? ")
  tempo = tempo.lower()

  if veiculo == "moto":
    if tempo == "horas":
      qt_horas = int(input("\n> Quantas horas? "))
      if qt_horas <= 1:
        valor = 1.80
      else:
        valor_parcial = (qt_horas - 1) * 1.80
        valor = (valor_parcial + 3)        
    elif tempo == "dias":
      qt_dias = int(input("\n> Quantos dias? "))
      valor = qt_dias * 15
      
  elif veiculo == "carro":
    if tempo == "horas":
      qt_horas = int(input("\n> Quantas horas? "))
      if qt_horas <= 1:
        valor = 5
      else:
        valor_parcial = (qt_horas - 1) * 3
        valor = (valor_parcial + 5)        
    elif tempo == "dias":
      qt_dias = int(input("\n> Quantos dias? "))
      valor = qt_dias * 25
      
  elif veiculo == "caminhonete":
    if tempo == "horas":
      qt_horas = int(input("\n> Quantas horas? "))
      if qt_horas <= 1:
        valor = 8
      else:
        valor_parcial = (qt_horas - 1) * 4.8
        valor = (valor_parcial + 8)        
    elif tempo == "dias":
      qt_dias = int(input("\n> Quantos dias? "))
      valor = qt_dias * 40
  
  return valor, estacionamento
  
def total(valor, estacionamento):  
  if estacionamento == "s":
    valor_total = valor * 0.8
  elif estacionamento == "n": 
    valor_total = valor
    
  print("\n[$] Valor total: R$ %.2f" % valor_total)
  
valor, estacionamento = inicio()
total(valor, estacionamento)