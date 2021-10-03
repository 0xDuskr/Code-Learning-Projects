class Conta:

# Função Construtora
    def __init__(self, numero, titular, saldo, limite):  # self é a referência ao objeto criado
        self.__numero = numero  # Atributos
        self.__titular = titular  # __ o torna privado, não acessível sem uso de um método (encapsulamento)
        self.__saldo = saldo
        self.__limite = limite

# Métodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):  # Método privado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor): # Se for True, proceder, senão Else
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property # Método representa uma propriedade (sem necessidade de usar os ())
    def limite(self): # Getter
        return self.__limite

    @limite.setter # Atributo
    def limite(self, limite): # Setter
        self.__limite = limite

    @staticmethod  # Método estático (da classe, não precisa do objeto)
    def codigo_banco(): # Usar com cautela, pois foge da proposta da OO
        return "001"
    # Conta.codigo_banco()

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}  # Dicionário
    # codigos = Conta.codigos_bancos()
    # codigos['Caixa']


# Testes de criação de objeto e extração de dados
# from conta import Conta
# conta1 = Conta(1, "User", 50.0, 1000.0)
# conta2 = Conta(2, "Teste", 130.0, 1000.0)
# conta1.extrato()
# conta1.transfere(10.0, conta2)
# conta1.get.limite() (método inicial, sem o @)
# conta1.set.limite(1500.0) (método inicial, sem o @)
# conta1.limite (método com @property)
# conta1.limite = 1500.0 (método com @limite.setter)
