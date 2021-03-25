import datetime
from datetime import date


class Manipula_data:

    def __init__(self):
        self._data_atual = date.today().strftime("%d/%m/%Y")

    def separa_data(self):
        data_separada = self._data_atual.split("/")
        return data_separada

    @property
    def data_atual(self):
        return int(self._data_atual)

    @property
    def extrai_dia(self):
        dia_atual = self.separa_data()
        return int(dia_atual[0])

    @ property
    def extrai_mes(self):
        mes_atual = self.separa_data()
        return int(mes_atual[1])

    @ property
    def extrai_ano(self):
        ano_atual = self.separa_data()
        return int(ano_atual[2])

    def subtrai_datas(self, dia, mes, ano=date.today().year):
        data1 = datetime.date(
            day=self.extrai_dia,
            month=self.extrai_mes,
            year=self.extrai_ano
        )

        data2 = datetime.date(day=dia, month=mes, year=ano)
        result = data2-data1.days
        return result
