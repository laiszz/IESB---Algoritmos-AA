class Cliente:
    def __init__(self, cpf: str, nome: str, fidelidade: bool, pontos: int, total_pedidos: int):
        self.cpf = cpf
        self.nome = nome
        self.fidelidade = fidelidade
        self.pontos = pontos
        self.total_pedidos = total_pedidos

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def fidelidade(self) -> bool:
        return self._fidelidade

    @property
    def pontos(self) -> int:
        return self._pontos

    @property
    def total_pedidos(self) -> int:
        return self._total_pedidos

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @nome.setter
    def nome(self, value):
        self._nome = value

    @fidelidade.setter
    def fidelidade(self, value):
        self._fidelidade = value

    @pontos.setter
    def pontos(self, value):
        self._pontos = value

    @total_pedidos.setter
    def total_pedidos(self, value):
        self._total_pedidos = value