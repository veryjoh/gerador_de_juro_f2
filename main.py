from src import emprestimo, cliente, data


c1 = cliente.Cliente("Cliente 1")
ep1 = emprestimo.Emprestimo(c1, 400, 12)


def carrega_emprestimos_abertos():
    pass


if __name__ == "__main__":

    carrega_emprestimos_abertos()
