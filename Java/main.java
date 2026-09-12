import colas.Cola;
import pilas.Pila;

public class main {

 public static void main(String[] args) {

     Cola<String> cola = new Cola<>();

     cola.encolar("Juan");
     cola.encolar("Pedro");
     cola.encolar("Maria");
     cola.encolar("Ana");

     System.out.println("Tamaño: " + cola.tamanio());
     System.out.println("¿Está vacía?: " + cola.estaVacia());

     System.out.println("Próximo elemento de la cola: " +
             cola.consultarPrimero());

     Pila<String> pila = new Pila<>();
     pila.apilar("Juan");
     pila.apilar("Pedro");

     System.out.println("Próximo elemento de la pila: " +
             pila.consultarTope());

     System.out.println("Desencolando: " + cola.desencolar());
     System.out.println("Desencolando: " + cola.desencolar());

     System.out.println("Tamaño después de desencolar: " +
             cola.tamanio());
 }
}