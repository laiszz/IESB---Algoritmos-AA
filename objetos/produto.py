class Produto:
    def __init__(self, codigo: int, nome: str, ingredientes: str, categoria: str, preco: float, promocao: bool, preco_promocional: float, estoque: int):
        self.codigo = codigo
        self.nome = nome
        self.ingredientes = ingredientes
        self.categoria = categoria
        self.preco = preco
        self.promocao = promocao
        self.preco_promocional = preco_promocional
        self.estoque = estoque

    @property
    def codigo(self) -> int:
        return self._codigo

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def ingredientes(self) -> str:
        return self._ingredientes

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def preco(self) -> float:
        return self._preco

    @property
    def promocao(self) -> bool:
        return self._promocao

    @property
    def preco_promocional(self) -> float:
        return self._preco_promocional

    @property
    def estoque(self) -> int:
        return self._estoque

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @nome.setter
    def nome(self, value):
        self._nome = value

    @ingredientes.setter
    def ingredientes(self, value):
        self._ingredientes = value

    @preco.setter
    def preco(self, value):
        self._preco = value

    @promocao.setter
    def promocao(self, value):
        self._promocao = value

    @preco_promocional.setter
    def preco_promocional(self, value):
        self._preco_promocional = value

    @estoque.setter
    def estoque(self, value):
        self._estoque = value

    @categoria.setter
    def categoria(self, value):
        self._categoria = value