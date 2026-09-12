from nodos.nodo import Nodo


class Cola[Elemento]:
	def __init__(self) -> None:
		self.__primero: Nodo[Elemento] | None = None
		self.__ultimo: Nodo[Elemento] | None = None
		self.__tamanio = 0

	def encolar(self, elemento: Elemento) -> None:
		nuevo = Nodo(elemento)

		if self.esta_vacia():
			self.__primero = nuevo
			self.__ultimo = nuevo
		else:
			self.__ultimo.set_siguiente(nuevo)
			self.__ultimo = nuevo

		self.__tamanio += 1

	def desencolar(self) -> Elemento | None:
		if self.esta_vacia():
			return None

		elemento = self.__primero.get_elemento()
		self.__primero = self.__primero.get_siguiente()
		self.__tamanio -= 1

		if self.__tamanio == 0:
			self.__ultimo = None

		return elemento

	def consultar_primero(self) -> Elemento | None:
		if self.esta_vacia():
			return None

		return self.__primero.get_elemento()

	def tamanio(self) -> int:
		return self.__tamanio

	def esta_vacia(self) -> bool:
		return self.__primero is None

