class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # def define_data(dia, mes, ano):
    #     data = {"dia":dia, "mes":mes, "ano":ano}
    #     return data

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

        # print("{}/{}/{}".format(self.dia, self.mes,self.ano))

    # from datas import Data
    # d = Data(21,11,2007)
    # d.formatada()
