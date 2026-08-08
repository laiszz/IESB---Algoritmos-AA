class Pedido:
    def __init__(self, produtos: list, preco_total: float, cliente_cpf: str | None, cliente_fidelidade: bool | None, preco_total_promocional: float | None, pontos_acumulados: int | None):
        self.produtos = produtos
        self.preco_total = preco_total
        self.cliente_cpf = cliente_cpf
        self.cliente_fidelidade = cliente_fidelidade
        self.preco_total_promocional = preco_total_promocional
        self.pontos_acumulados = pontos_acumulados

    @property
    def produtos(self) -> list:
        return self._produtos

    @property
    def preco_total(self) -> float:
        return self._preco_total

    @property
    def cliente_cpf(self) -> str:
        return self._cliente_cpf

    @property
    def cliente_fidelidade(self) -> bool:
        return self._cliente_fidelidade

    @property
    def preco_total_promocional(self) -> float:
        return self._preco_total_promocional

    @property
    def pontos_acumulados(self) -> int:
        return self._pontos_acumulados

    @produtos.setter
    def produtos(self, value):
        self._produtos = value

    @preco_total.setter
    def preco_total(self, value):
        self._preco_total = value

    @cliente_cpf.setter
    def cliente_cpf(self, value):
        self._cliente_cpf = value

    @cliente_fidelidade.setter
    def cliente_fidelidade(self, value):
        self._cliente_fidelidade = value

    @preco_total_promocional.setter
    def preco_total_promocional(self, value):
        self._preco_total_promocional = value

    @pontos_acumulados.setter
    def pontos_acumulados(self, value):
        self._pontos_acumulados = value