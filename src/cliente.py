class Cliente:

    def __init__(self, nome, cpf, email, telefone):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    def alterar_email(self, novo_email):
        if novo_email and "@" in novo_email:
            self._email = novo_email
        else:
            print("Informe um e-mail válido!")
    
    def alterar_telefone(self, novo_telefone):
        if novo_telefone:
            self._telefone = novo_telefone
        else:
            print("Informe um número válido!")

    def valida_cpf(self):
        return len(self._cpf == 11)

    def __str__(self) -> str:
        details = {
            "Nome":self._nome,
            "CPF":self._cpf,
            "E-mail": self._cpf,
            "Telefone": self._telefone
        }
        return details

    