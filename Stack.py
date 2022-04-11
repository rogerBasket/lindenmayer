class Stack:

	def __init__(self):
		self.lista = []

	def push(self, angulo, posicion):
		self.lista.append((angulo, posicion))

	def pop(self):
		return self.lista.pop()

	def size(self):
		return self.len(lista)