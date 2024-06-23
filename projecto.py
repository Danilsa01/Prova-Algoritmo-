
#INTERFACE GRAFCA

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QWidget, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt
from estrutura import ArvoreBinaria,ListaDuplamenteLigada, Grafo # type: ignore

class ListaDuplamenteWindow(QWidget):
    def __init__(self, switch_window_callback):
        super().__init__()

        self.setStyleSheet("background-color: #2C2C2C;")
        self.lista = ListaDuplamenteLigada()

        self.layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Valor 1")
        self.input1.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Valor 2")
        self.input2.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.input2)

        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.adicionar_no)
        self.add_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover")
        self.remove_button.clicked.connect(self.remover_no)
        self.remove_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.remove_button)

        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(switch_window_callback)
        self.back_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.back_button)

        self.reset_button = QPushButton("Refazer Estrutura")
        self.reset_button.clicked.connect(self.reset_estrutura)
        self.reset_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.reset_button)

        self.end_button = QPushButton("Fim da Operação")
        self.end_button.clicked.connect(self.close)
        self.end_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.end_button)

        self.layout.addLayout(self.input_layout)

        self.graphics_view = QGraphicsView()
        self.graphics_scene = QGraphicsScene()
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

    def adicionar_no(self):
        valor1 = self.input1.text()
        valor2 = self.input2.text()
        if valor1.isdigit() and valor2.isdigit():
            valor1, valor2 = int(valor1), int(valor2)
            self.lista.adicionar(valor1, valor2)
            self.update_graphics()
            self.input1.clear()
            self.input2.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira números válidos.")

    def remover_no(self):
        valor1 = self.input1.text()
        valor2 = self.input2.text()
        if valor1.isdigit() and valor2.isdigit():
            valor1, valor2 = int(valor1), int(valor2)
            self.lista.remover(valor1, valor2)
            self.update_graphics()
            self.input1.clear()
            self.input2.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira números válidos.")

    def update_graphics(self):
        self.graphics_scene.clear()
        valores = self.lista.listar()

        x = 0
        y = 0
        largura = 60
        altura = 30
        espacamento = 20

        for i, (valor1, valor2) in enumerate(valores):
            retangulo = self.graphics_scene.addRect(x, y, largura, altura, QPen(Qt.white))
            retangulo.setBrush(Qt.gray)
            texto = self.graphics_scene.addText(f"{valor1} {valor2}")
            texto.setDefaultTextColor(Qt.white)
            texto.setPos(x + 10, y + 5)

            if i > 0:
                linha = self.graphics_scene.addLine(x - espacamento, y + altura / 2, x, y + altura / 2, QPen(Qt.white))
            
            x += largura + espacamento

    def reset_estrutura(self):
        self.lista = ListaDuplamenteLigada()
        self.update_graphics()

class GrafoWindow(QWidget):
    def __init__(self, switch_window_callback):
        super().__init__()

        self.setStyleSheet("background-color: #2C2C2C;")
        self.grafo = Grafo()

        self.layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.vertice_input = QLineEdit()
        self.vertice_input.setPlaceholderText("Vértice")
        self.vertice_input.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.vertice_input)

        self.add_vertice_button = QPushButton("Adicionar Vértice")
        self.add_vertice_button.clicked.connect(self.adicionar_vertice)
        self.add_vertice_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.add_vertice_button)

        self.origem_input = QLineEdit()
        self.origem_input.setPlaceholderText("Origem")
        self.origem_input.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.origem_input)

        self.destino_input = QLineEdit()
        self.destino_input.setPlaceholderText("Destino")
        self.destino_input.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.destino_input)

        self.add_aresta_button = QPushButton("Adicionar Aresta")
        self.add_aresta_button.clicked.connect(self.adicionar_aresta)
        self.add_aresta_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.add_aresta_button)

        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(switch_window_callback)
        self.back_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.back_button)

        self.reset_button = QPushButton("Refazer Estrutura")
        self.reset_button.clicked.connect(self.reset_estrutura)
        self.reset_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.reset_button)

        self.end_button = QPushButton("Fim da Operação")
        self.end_button.clicked.connect(self.close)
        self.end_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.end_button)

        self.layout.addLayout(self.input_layout)

        self.graphics_view = QGraphicsView()
        self.graphics_scene = QGraphicsScene()
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

    def adicionar_vertice(self):
        vertice = self.vertice_input.text()
        if vertice:
            self.grafo.adicionar_vertice(vertice)
            self.update_graphics()
            self.vertice_input.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira um vértice válido.")

    def adicionar_aresta(self):
        origem = self.origem_input.text()
        destino = self.destino_input.text()
        if origem and destino:
            self.grafo.adicionar_aresta(origem, destino)
            self.update_graphics()
            self.origem_input.clear()
            self.destino_input.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira vértices válidos.")

    def update_graphics(self):
        self.graphics_scene.clear()

        # Draw vertices
        vertice_positions = {}
        x = 50
        y = 50
        espacamento = 100
        for vertice in self.grafo.vertices:
            retangulo = self.graphics_scene.addRect(x, y, 50, 50, QPen(Qt.white))
            retangulo.setBrush(Qt.gray)
            texto = self.graphics_scene.addText(f"{vertice}")
            texto.setDefaultTextColor(Qt.white)
            texto.setPos(x + 15, y + 15)
            vertice_positions[vertice] = (x + 25, y + 25)
            y += espacamento

        # Draw edges
        for origem, destino in self.grafo.arestas:
            origem_pos = vertice_positions[origem]
            destino_pos = vertice_positions[destino]
            linha = self.graphics_scene.addLine(origem_pos[0], origem_pos[1], destino_pos[0], destino_pos[1], QPen(Qt.white))

    def reset_estrutura(self):
        self.grafo = Grafo()
        self.update_graphics()

class ArvoreBinariaWindow(QWidget):
    def __init__(self, switch_window_callback):
        super().__init__()

        self.setStyleSheet("background-color: #2C2C2C;")
        self.arvore = ArvoreBinaria()

        self.layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Valor")
        self.input.setStyleSheet("background-color: #333333; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.input)

        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.adicionar_no)
        self.add_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.add_button)

        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(switch_window_callback)
        self.back_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.back_button)

        self.reset_button = QPushButton("Refazer Estrutura")
        self.reset_button.clicked.connect(self.reset_estrutura)
        self.reset_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.reset_button)

        self.end_button = QPushButton("Fim da Operação")
        self.end_button.clicked.connect(self.close)
        self.end_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 14px;")
        self.input_layout.addWidget(self.end_button)

        self.layout.addLayout(self.input_layout)

        self.graphics_view = QGraphicsView()
        self.graphics_scene = QGraphicsScene()
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

    def adicionar_no(self):
        valor = self.input.text()
        if valor.isdigit():
            valor = int(valor)
            self.arvore.adicionar(valor)
            self.update_graphics()
            self.input.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

    def update_graphics(self):
        self.graphics_scene.clear()
        if self.arvore.raiz:
            self._draw_node(self.arvore.raiz, 400, 50, 200)

    def _draw_node(self, node, x, y, spacing):
        if node:
            retangulo = self.graphics_scene.addRect(x - 15, y - 15, 30, 30, QPen(Qt.white))
            retangulo.setBrush(Qt.gray)
            texto = self.graphics_scene.addText(f"{node.valor}")
            texto.setDefaultTextColor(Qt.white)
            texto.setPos(x - 10, y - 10)

            if node.esquerda:
                linha = self.graphics_scene.addLine(x, y + 15, x - spacing, y + 100 - 15, QPen(Qt.white))
                self._draw_node(node.esquerda, x - spacing, y + 100, spacing // 2)

            if node.direita:
                linha = self.graphics_scene.addLine(x, y + 15, x + spacing, y + 100 - 15, QPen(Qt.white))
                self._draw_node(node.direita, x + spacing, y + 100, spacing // 2)

    def reset_estrutura(self):
        self.arvore = ArvoreBinaria()
        self.update_graphics()

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #2C2C2C;")

        layout = QVBoxLayout()

        self.setWindowTitle('Escolha a Estrutura de Dados')
        self.setGeometry(100, 100, 800, 600)

        self.lista_button = QPushButton('Lista Duplamente Ligada', self)
        self.lista_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 18px;")
        self.lista_button.clicked.connect(self.show_lista_duplamente_window)
        layout.addWidget(self.lista_button)

        self.grafo_button = QPushButton('Grafo', self)
        self.grafo_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 18px;")
        self.grafo_button.clicked.connect(self.show_grafo_window)
        layout.addWidget(self.grafo_button)

        self.arvore_button = QPushButton('Árvore Binária', self)
        self.arvore_button.setStyleSheet("background-color: #A9A9A9; color: white; font-size: 18px;")
        self.arvore_button.clicked.connect(self.show_arvore_binaria_window)
        layout.addWidget(self.arvore_button)

        self.setLayout(layout)

    def show_lista_duplamente_window(self):
        self.lista_duplamente_window = ListaDuplamenteWindow(self.show)
        self.lista_duplamente_window.show()
        self.hide()

    def show_grafo_window(self):
        self.grafo_window = GrafoWindow(self.show)
        self.grafo_window.show()
        self.hide()

    def show_arvore_binaria_window(self):
        self.arvore_binaria_window = ArvoreBinariaWindow(self.show)
        self.arvore_binaria_window.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = MainMenu()
    mainMenu.show()
    sys.exit(app.exec_())

