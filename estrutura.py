class NoLista:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = None
        self.proximo = None

class ListaDuplamenteLigada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar(self, valor1, valor2):
        novo_no = NoLista(valor1, valor2)
        if self.cauda is None:  # Lista vazia
            self.cabeca = novo_no
            self.cauda = novo_no
        else:  # Adiciona ao final da lista
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda
            self.cauda = novo_no

    def listar(self):
        valores = []
        no_atual = self.cabeca
        while no_atual:
            valores.append((no_atual.valor1, no_atual.valor2))
            no_atual = no_atual.proximo
        return valores

    def remover(self, valor1, valor2):
        no_atual = self.cabeca
        while no_atual:
            if no_atual.valor1 == valor1 and no_atual.valor2 == valor2:
                if no_atual.anterior:
                    no_atual.anterior.proximo = no_atual.proximo
                if no_atual.proximo:
                    no_atual.proximo.anterior = no_atual.anterior
                if no_atual == self.cabeca:
                    self.cabeca = no_atual.proximo
                if no_atual == self.cauda:
                    self.cauda = no_atual.anterior

                # Shift values
                proximo = no_atual.proximo
                while proximo:
                    no_atual.valor1, no_atual.valor2 = proximo.valor1, proximo.valor2
                    no_atual = proximo
                    proximo = proximo.proximo
                
                if no_atual.anterior:
                    no_atual.anterior.proximo = None
                else:
                    self.cabeca = None
                break
            no_atual = no_atual.proximo

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def adicionar_vertice(self, valor):
        if valor not in self.vertices:
            self.vertices[valor] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)
            self.arestas.append((origem, destino))

class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz is None:
            self.raiz = NoArvore(valor)
        else:
            self._adicionar(self.raiz, valor)

    def _adicionar(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NoArvore(valor)
            else:
                self._adicionar(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = NoArvore(valor)
            else:
                self._adicionar(no.direita, valor)

    def em_ordem(self):
        return self._em_ordem(self.raiz)

    def _em_ordem(self, no):
        if no is not None:
            return self._em_ordem(no.esquerda) + [no.valor] + self._em_ordem(no.direita)
        return []

    def pre_ordem(self):
        return self._pre_ordem(self.raiz)

    def _pre_ordem(self, no):
        if no is not None:
            return [no.valor] + self._pre_ordem(no.esquerda) + self._pre_ordem(no.direita)
        return []

    def pos_ordem(self):
        return self._pos_ordem(self.raiz)

    def _pos_ordem(self, no):
        if no is not None:
            return self._pos_ordem(no.esquerda) + self._pos_ordem(no.direita) + [no.valor]
        return []
