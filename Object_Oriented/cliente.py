
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property # Método representa uma propriedade (sem necessidade de usar os ())
    def nome(self): # Getter
        return self.__nome.title() # Title define a primeira letra como maiúscula
    # cliente.nome
    @nome.setter # Atributo
    def nome(self, nome): # Setter
        self.__nome = nome
    # cliente.nome = "Teste"
    
