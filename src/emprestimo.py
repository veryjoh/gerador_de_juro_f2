class Emprestimo:

    def __init__(self, cliente, valor_solicitado: int, dias_p_devolucao: int):
        self._id = (id(self))
        self._cliente = cliente
        self._juros_base = 0.6
        self._valor_solicitado = int(valor_solicitado)
        self._dias_p_devolucao = int(dias_p_devolucao)

    @property
    def valor_solicitado(self):
        return self._valor_solicitado

    @property
    def dias_p_devolucao(self):
        return self._dias_p_devolucao

    def acresce_juros(self):
        valor_com_juros = (
            self.valor_solicitado * self._juros_base
            ) + self.dias_p_devolucao
        return valor_com_juros

    def calcula_valor_final(self):
        total = self.acresce_juros() + self.valor_solicitado
        return total

    def emprestimo_pago(self):
        return True

    def _str__(self):

        resumo_do_emprestimo = {
            "Cliente": self._cliente.nome,
            "Valor emprestado": f"R$:{self.valor_solicitado} ",
            "Valor a pagar R$:": f"{self.calcula_valor_final()}",
            "Previsão devolução": f"{self.  dias_p_devolucao} dias"
        }

        return resumo_do_emprestimo
