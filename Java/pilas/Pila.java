// Pila.java
package pilas;

import nodos.Nodo;

public class Pila<T> {

    private Nodo<T> tope;
    private int tamanio;

    public Pila() {
        tope = null;
        tamanio = 0;
    }

    public void apilar(T elemento) {
        Nodo<T> nuevo = new Nodo<>(elemento);

        if (estaVacia()) {
            tope = nuevo;
        } else {
            nuevo.setSiguiente(tope);
            tope = nuevo;
        }

        tamanio++;
    }

    public T desapilar() {
        if (estaVacia()) {
            return null;
        }

        T elemento = tope.getElemento();

        tope = tope.getSiguiente();

        tamanio--;

        return elemento;
    }

    public T consultarTope() {
        if (estaVacia()) {
            return null;
        }

        return tope.getElemento();
    }

    public int tamanio() {
        return tamanio;
    }

    public boolean estaVacia() {
        return tope == null;
    }
}