# Prueba-Veevart
## Ejercicio de la mochila. Programa : mochila.py
Para el ejercicio de la mochila se debe usar DP (Programación Dinamica) para lograr mejor optimización.
Para esto se debe plantear una función phi que es la función objetivo. Luego se debe definir la función recurrente phi. En DP se puede usar memorización o tabulación. Es preferible usar tabulación por el tema de la reducción de espacio.
Para esto se tiene que tener en cuenta dos cosas, si se agrega peso o no a la mochila y que no exceda su capacidad maxima y de ser así (de exceder su capacidad maxima sigue iterando)
1. Comprueba si es posible agregar un nuevo elemento a la mochila sin exceder su capacidad.
2. Comprueba que si al agregar un nuevo elemento actual excede el limite de la capacidad maxima de la mochila, en actualiza el valor de lo almacenado con su nuevo valor.
## Ejercicio de la mochila(Bonus: Implemented in Apex). Programa: mochila.apxc
Implementado en apex.
## Ejercicio de la mochila(Bonus: Items that are not saved and total value). Programa: mochila2.py
 Muestra los sub arreglos que no se tomaron para la optimización y su valor total.

## Ejercicio del ascensor. Programa: ascensor.py
Documentado en el mismo code. Con el funcionamiento que dice en el doc.

## Ejercicio del ascensor (Bonus: The user requests the elevator) Programa: ascensor2.py
Documentado en el mismo code.
El usuario puede ingresar al piso al que desea siempre que pasa por un piso. Por ejemplo, si un usuario entra en el piso 6, le pregunta a que piso desea ir (Como funciona en la vida real).
Si el usuario presiona enter se asume que no eligió ningun piso y el ascensor continua su camino.
