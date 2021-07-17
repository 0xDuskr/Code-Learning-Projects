
def inicio():
  nome = input("\nNome: ")
  profissional = "x"
  while profissional != "s" and profissional != "n":
    profissional = input("\nProfissional da saúde? (s/n): ")
    profissional = profissional.lower()
    if profissional == "s":
      profissional_saude()
    elif profissional == "n":
      nao_profissional()
    else:
      print("\n[!] Favor responder com 's' ou 'n'")
      continue

def profissional_saude():
  funcao = input("\nInforme sua função (medico/enfermeiro/outros): ")
  funcao = funcao.lower()
  if funcao == "medico":
    print("\nPrimeira dose: 01/03/2021\nSegunda dose: 29/03/2021")
  elif funcao == "enfermeiro":
    print("\n> Primeira dose: 02/03/2021\n> Segunda dose: 30/03/2021")  
  else:
    print("\nPrimeira dose: 03/03/2021\nSegunda dose: 31/03/2021")

def nao_profissional():
  possui_comorbidade = input("\nPossui comorbidades? (s/n): ")
  if possui_comorbidade.lower() == "s":
    tipo_comorbidade = input("\nQual comorbidade? (Down | Renal | Cardiaca | Diabetes | Hipertensao): ")
    tipo_comorbidade = tipo_comorbidade.lower()
    if tipo_comorbidade == "down":
      print("\nPrimeira dose: 01/05/2021\nSegunda dose: 29/05/2021")
    if tipo_comorbidade == "renal":
      print("\nPrimeira dose: 08/05/2021\nSegunda dose: 05/06/2021")
    if tipo_comorbidade == "cardiaca":
      print("\nPrimeira dose: 15/05/2021\nSegunda dose: 12/06/2021")
    if tipo_comorbidade == "diabetes":
      print("\nPrimeira dose: 22/05/2021\nSegunda dose: 19/06/2021")
    if tipo_comorbidade == "hipertensao":
      print("\nPrimeira dose: 29/05/2021\nSegunda dose: 26/06/2021")
    else:  
      print("\n[!] Comorbidade não identificada")
  else:
    nascimento()

def nascimento():
      ano_nascimento = int(input("\nAno de nascimento: "))
      if ano_nascimento < 1942:
        print("\nPrimeira dose: 04/03/2021\nSegunda dose: 01/04/2021")
      elif ano_nascimento < 1947:
        print("\nPrimeira dose: 11/03/2021\nSegunda dose: 08/04/2021")
      elif ano_nascimento < 1952:
        print("\nPrimeira dose: 18/03/2021\nSegunda dose: 15/04/2021")  
      elif ano_nascimento < 1957:
        print("\nPrimeira dose: 25/03/2021\nSegunda dose: 22/04/2021")
      elif ano_nascimento < 1962:
        print("\nPrimeira dose: 10/04/2021\nSegunda dose: 08/05/2021")
      else:
        print("\nPrimeira dose: 01/06/2021\nSegunda dose: 29/06/2021")  

inicio()