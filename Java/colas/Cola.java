// Cola.java
package colas;

import nodos.Nodo;

public class Cola<T> {

    private Nodo<T> primero;
    private Nodo<T> ultimo;
    private int tamanio;

    public Cola() {
        primero = null;
        ultimo = null;
        tamanio = 0;
    }

    public void encolar(T elemento) {
        Nodo<T> nuevo = new Nodo<>(elemento);

        if (estaVacia()) {
            primero = nuevo;
            ultimo = nuevo;
        } else {
            ultimo.setSiguiente(nuevo);
            ultimo = nuevo;
        }

        tamanio++;
    }

    public T desencolar() {
        if (estaVacia()) {
            return null;
        }

        T elemento = primero.getElemento();
        primero = primero.getSiguiente();

        tamanio--;

        if (tamanio == 0) {
            ultimo = null;
        }

        return elemento;
    }

    public T consultarPrimero() {
        if (estaVacia()) {
            return null;
        }

        return primero.getElemento();
    }

    public int tamanio() {
        return tamanio;
    }

    public boolean estaVacia() {
        return primero == null;
    }
}