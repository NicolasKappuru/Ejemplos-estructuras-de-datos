from colas.cola import Cola
from pilas.pila import Pila


def main() -> None:
	cola = Cola[str]()

	cola.encolar("Juan")
	cola.encolar("Pedro")
	cola.encolar("Maria")
	cola.encolar("Ana")

	print(f"Tamaño: {cola.tamanio()}")
	print(f"¿Está vacía?: {cola.esta_vacia()}")
	print(f"Próximo elemento de la cola: {cola.consultar_primero()}")

	pila = Pila[str]()
	pila.apilar("Juan")
	pila.apilar("Pedro")

	print(f"Próximo elemento de la pila: {pila.consultar_tope()}")
	print(f"Desencolando: {cola.desencolar()}")
	print(f"Desencolando: {cola.desencolar()}")
	print(f"Desapilando: {pila.desapilar()}")
	print(f"Tamaño de la cola después de retirar: {cola.tamanio()}")


if __name__ == "__main__":
	main()
