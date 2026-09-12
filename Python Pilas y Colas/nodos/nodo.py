from __future__ import annotations # Para la referenciación a sí mismo

class Nodo[Elemento]:
	def __init__(self, elemento: Elemento) -> None:
		self.__elemento = elemento
		self.__siguiente: Nodo[Elemento] | None = None

	def get_elemento(self) -> Elemento:
		return self.__elemento

	def set_elemento(self, elemento: Elemento) -> None:
		self.__elemento = elemento

	def get_siguiente(self) -> Nodo[Elemento] | None:
		return self.__siguiente

	def set_siguiente(self, siguiente: Nodo[Elemento] | None) -> None:
		self.__siguiente = siguiente



