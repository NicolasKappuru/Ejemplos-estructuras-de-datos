
from nodos.nodo import Nodo

class Pila[Elemento]:
	def __init__(self) -> None:
		self.__tope: Nodo[Elemento] | None = None
		self.__tamanio = 0

	def apilar(self, elemento: Elemento) -> None:
		nuevo = Nodo(elemento)

		if self.esta_vacia():
			self.__tope = nuevo
		else:
			nuevo.set_siguiente(self.__tope)
			self.__tope = nuevo

		self.__tamanio += 1

	def desapilar(self) -> Elemento | None:
		if self.esta_vacia():
			return None

		elemento = self.__tope.get_elemento()
		self.__tope = self.__tope.get_siguiente()
		self.__tamanio -= 1

		return elemento

	def consultar_tope(self) -> Elemento | None:
		if self.esta_vacia():
			return None

		return self.__tope.get_elemento()

	def tamanio(self) -> int:
		return self.__tamanio

	def esta_vacia(self) -> bool:
		return self.__tope is None
