Title: Testing doubles
Date: 2022-04-12
Category: Testing
Tags: testing, tech
Slug: test-doubles
Summary: A la hora de testear es necesario falsear implementaciones de dependencias en nuestro código a testear. Para ello usaremos **test doubles**, que nos permitirán sustituir nuestras implementaciones por algo falso que tendremos bajo nuestro control.

A la hora de testear es necesario falsear implementaciones de dependencias en nuestro código a testear. Para ello usaremos ***test doubles***, que nos permitirán sustituir nuestras implementaciones por algo falso que tendremos bajo nuestro control. Existen varios tipos de *test doubles*:

- ***fake***: implementación funcional pero con valores generados aleatoriamente. Los *fake* se suelen generar utilizando un builder especial conocido como *objectMother*, que da valores aleatorios a todas las propiedades salvo a aquellas que queramos especificar para nuestro test.
- ***dummy***: implementa la interfaz pero todos sus métodos no tienen implementación. Suelen ser elementos que necesita nuestro test pero que no va a utilizar.
- ***stub***: es una especie de dummy pero en el que todos los valores están predefinidos, sin lógica. Se usan para falsear datos que necesita nuestro test pero de los cuales no nos importa el valor.
- ***spy***: permite observar si ha habido alguna interacción o llamada a la implementación, pero no modela la implementación (solo controla la entrada). Muy útiles para verificar que las llamadas a dependencias de nuestro test se hacen como esperamos.
- ***mock***: implementación pensada para validar los argumentos y, a diferencia de *spy*, modelar una implementación de salida. Se usa cuando necesitamos controlar la respuesta de nuestras dependencias externas.

Al final, a la hora de hacer los test acostumbramos a llamar a todos estos doubles de la misma forma (incluso alguna librería mezcla los nombres). Lo importante es saber que tenemos todas estas opciones en nuestra mano y saber cómo y cuándo utilizarlas para simplificar nuestros test.
