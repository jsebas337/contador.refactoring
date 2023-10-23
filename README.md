Jean Franco Gamboa Díaz. Codigo: 20231020074.
Linda Dayanna Niño Lasso. Codigo: 20231015106.
Juan Sebastian Hernandez Susatama. Codigo: 20231015062

En el codigo `ejemplo_refactoring.py` utilizamos las tecnicas de refactoring para unificar la logica en una sola clase utilizando la clase unica en `SistemaNumerico` para manejar todas las operaciones relacionadas con sistemas numéricos en lugar de tener clases separadas para cada sistema numérico.


 luego agregamos el Polimorfismo en el método `obtener_valor()`, se utiliza una estructura condicional (`if-elif-else`) para determinar el sistema numérico actual y realizar la conversión correspondiente.
 
 
 
Esto aprovecha el polimorfismo para que el método funcione de manera diferente según el sistema numérico seleccionado.
  
  
Tambien utilizamos Minimización de duplicación para eliminar la duplicación de código innecesaria al unificar las operaciones en una sola clase.Por ultimo se utilizó la  Interacción con el usuario mediante la entrada de sistemas numéricos y valores iniciales, luego muestra el contador en el sistema numérico elegido. 