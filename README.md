# Prueba-Veevart
## Ejercicio de la mochila
Para el ejercicio de la mochila se debe usar DP (Programación Dinamica) para lograr mejor optimización.
Para esto se debe plantear una función phi que es la función objetivo. Luego se debe definir la función recurrente phi. En DP se puede usar memorización o tabulación. Es preferible usar tabulación por el tema de la reducción de espacio.
Para esto se tiene que tener en cuenta dos cosas, si se agrega peso o no a la mochila y que no exceda su capacidad maxima y de ser así (de exceder su capacidad maxima sigue iterando)
1. Comprueba si es posible agregar un nuevo elemento a la mochila sin exceder su capacidad.
2. Comprueba que si al agregar un nuevo elemento actual excede el limite de la capacidad maxima de la mochila, en actualiza el valor de lo almacenado con su nuevo valor.
