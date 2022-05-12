Title: The Pragmatic Programmer: mis notas
Date: 2022-05-12
Category: Libros
Tags: libros, tech
Slug: pragmatic-programmer-notas
Summary: Hace muchos años (en mis comienzos en el mundo del desarrollo) me leí el libro [The Pragmatic Programmer](https://www.amazon.es/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052), de David Thomas y Andrew Hunt. Hace poco un compañero me comentó que se lo estaba leyendo, ya que es un libro muy recomendado en el sector, y me ha dado por revisar las notas que tomé en su día sobre el libro. Con intención de recordarlas, y ya de paso pasarlas a limpio, he decidido subirlas aquí por si a alguien más le pueden interesar.
Status: draft

Hace muchos años (en mis comienzos en el mundo del desarrollo) me leí el libro The Pragmatic Programmer, de David Thomas y Andrew Hunt. Hace poco un compañero me comentó que se lo estaba leyendo, ya que es un libro muy recomendado en el sector, y me ha dado por revisar las notas que tomé en su día sobre el libro. Con intención de recordarlas, y ya de paso pasarlas a limpio, he decidido subirlas aquí por si a alguien más le pueden interesar.

**Tip 1: Care about your craft.** No hay otros puntos importantes en el desarrollo de software si no te preocupas por hacer las cosas bien.

**Tip 2: Think! about your work.** Piensa en lo que haces mientras no estás haciendo.

**Tip 3: Provide options, don't make lame excuses.** Tu papel es el de proporcionar soluciones, opciones, alternativas a los problemas. Si algo sale mal, no des una excusa y explica cómo puedes salvar la situación.

**Tip 4: Don't live with broken windows.** Para evitar que el software eche raíces, evita dejar "ventanas rotas" (malos diseños, malas decisiones, mal código) sin arreglar. Del mismo modo, evita romper ventanas cuando salga algún fuego, evitando sus posteriores consecuencias.

**Tip 5: Be a catalyst for change.** Si ves una solución obvia, impleméntala aún sin permiso y enséñasela a la gente, que terminará usándola/aceptándola. Es mejor pedir perdón que pedir permiso.

**Tip 6: Remember the big picture.** Comprueba todo lo que sucede a tu alrededor, no solo en lo que estás trabajando. Los cambios pequeños pueden hacer desmoronarse todo el sistema.

**Tip 7: Make quality a requirement issue.** El entorno y la calidad del software deberían ser incluidos en los requisitos del sistema. Muchos usuarios prefieren un software funcional hoy que vaya incluyendo mejoras y puliéndose en el tiempo que esperar un año a una versión completa. Haz software que sea "lo suficientemente bueno". También debes saber cuando parar de refinar y mejorar un programa, ya que el resultado puede no terminar siendo el deseado.

**Tip 8: Invest regularly in your knowledge portfolio.** Intenta ampliar tus conocimientos invirtiendo regularmente, aunque sea en pequeñas cantidades, diversificando con diferentes tecnologías y arriesgando en algunas de ellas (no todas), e investigando tecnologías emergentes (buy low sell high). Revisa y balancea tus inversiones periódicamente intentando encontrar un equilibrio entre ellas.

**Tip 9: Critically analyze what you read and hear.** No te dejes impresionar por los comerciales, el hype o falsos gurús. Analiza con ojo crítico todo e intenta comprobar cómo se adapta a tus proyectos o tu portfolio de conocimientos.

**Tip 10: It's both what you say and the way you say it.** Intenta comunicar tus ideas lo mejor posible para hacerlas entender a todas las personas. Analiza lo que quieres decir, conoce a tu audiencia y adapta tu discurso. Elige un momento apropiado y un estilo adecuado (documentación, email, charla...). Cuida la presentación y haz que luzca bien. Involucra a tu audiencia y devuelve lo que esta te ofrece, respondiendo preguntas o argumentando nuevas propuestas.

**Tip 11: Don't repeat yourself.** Toda representación de conocimiento debe tener una única no ambigua y autoritaria representación dentro del sistema. La repetición de código viene dada por 4 posibles factores: duplicación impuesta (por el lenguaje, documentación, entorno...), inadvertida (el desarrollador no es consciente), impaciente (se duplica código por ser la opción sencilla) o inter developer (varios desarrolladores duplican código dentro de un mismo proyecto sin conocer el del otro).

**Tip 12: Make it easy to reuse.** Aplicando DRY puedes conseguir un entorno donde es fácil encontrar y reutilizar funcionalidades antes que hacerlo de nuevo.

**Tip 13: Eliminate effects between unrelated things.** Se dice que un sistema es ortogonal cuando la variación de un elemento no afecta a otros. Eto hace que se gane productividad y se reduzcan riesgos. Que un sistema sea ortogonal depende de varios elementos: los equipos del proyecto (cuanto más se puedan separar sin causar problemas, más ortogonalidad), diseño, herramientas de diseño y librerías, código (desacoplado, sin usar datos globales y evitando duplicidad), testing (unitarios demuestra independencia) y documentación.

**Tip 14: There are no final decisions.** Intenta modularizar tu código de tal manera que luego pueda ser propenso a cambios (incluso radicales) sin necesitar alterar el sistema completo. Abstrae todos los módulos usando interfaces, automatizando el código o aplicando patrones.

**Tip 15: Use tracer bullets to find the target.** Intenta desarrollar un producto mínimo para empezar a ver resultados y obtener feedback, viendo así si tu propuesta y algoritmos se acercan al objetivo planteado.

**Tip 16: Prototype to learn.** Con un prototipo puedes ser capaz de ver la arquitectura, nuevas funcionalidades en un sistema existente, la estructura externa de los datos, analizar herramientas de terceros, el rendimiento o el diseño de las interfaces.

**Tip 17: Program close to the domain problem.** Intenta trabajar con expresiones relacionadas con el dominio (nombres de métodos, variables, ficheros...) reconocibles por cualquier usuario.

**Tip 18: Estimate to avoid surprises.** Estima antes de empezar, desde plazos a rendimiento o memoria. Para estimar correctamente debes comprender el problema, construir un modelo mental y separarlo en componentes, estimar el coste de cada uno de ellos y calcular la respuesta. Analiza tus estimaciones para aprender a hacer mejores estimaciones.

**Tip 19: Iterate the schedule with the code.** Es difícil estimar un proyecto desconocido (dominio, tecnología, equipo...), por lo que es recomendable iterar la planificación periódicamente: comprobar requisitos, analizar riesgos, diseñar implementar y validad con los usuarios.

**Tip 20: Keep knowledge in plain text.** El texto plano es entendible por todo el mundo, por lo que es una forma muy útil de mantener la información con el paso del tiempo, entendible y computable y fácil de testear y de ayuda al testeo. Es común de utilizar en diferentes ficheros de configuración.

**Tip 21: Use the power of command shells.** Conocer los comandos de la terminar da más posibilidades que usar la GUI, permitiendo además automatizar tareas mediante macros.

**Tip 22: Use a single editor well.** Conoce los atajos de teclado y las opciones que tu editor posee. El editor debe ser configurable (atajos, estilos, tamaños, ventanas...), extensible (agregar nuevos lenguajes) y programable (macros, snippets).

**Tip 23:  Always use source code control.** Esta herramienta te permite controlar el historial de un proyecto (sea de código o no), almacenar la información y trabajar en paralelo.

**Tip 24: Fix the problem, not the blame.** Los bugs no son un problema de una persona, son de todo el equipo. Localízalos y arréglalos, no pierdas el tiempo buscando a un culpable.

**Tip 25: Don't panic when debugging.** Antes de comenzar a debugear, piensa en las causas del bug. Analiza las condiciones bajo las que se produce y profundiza, no apliques un parche superficial. Las estrategias para debugear son analizar los datos utilizados (tipos, valores, etc), agregar trazas para ver el estado del sistema, contarle el flujo a un "patito de goma" y no culpar a terceros (librerías o sistemas operativos).

**Tip 26: "select" isn't broken.** El error probablemente esté en tu código, no en el de otros. Las librerías y el sistema operativo están suficientemente testeadas y probadas como para no haber notificado el fallo.

**Tip 27:  Don't assume it - prove it.** Prueba que tu código funcione con datos reales actuales y bajo ciertas condiciones para decir que el error no se encuentra en el. Una vez localizado, asegúrate de agregar test y todo lo necesario para que no vuelva a repetirse.

**Tip 28: Lear a text manipulation language.** Aprende a hacer scripts que trabajen con texto plano con lenguajes como Python o Perl, pudiendo producir otros documentos o automatizar tareas.

**Tip 29: Write code that writes code.** Aprende a construir generadores de código para automatizar tareas. Esto permite variar la especificación de los datos y autogenerar sus implementaciones (bases de datos, objetos, estructuras...) evitando duplicidades. Los generadores de código pueden ser pasivos (se utilizan para una sola tarea, cómo generar templates o traducir código) o activos (tareas repetitivas, cómo generar objetos a partir de la base de datos o una configuración inicial).

**Tip 30: You can't write perfect software.** Diseña tu código de forma que sea resistente a errores

**Tip 31: Design with contracts.** Haz código que cumpla exactamente lo especificado. Dadas unas precondiciones cambiar el estado en función de las mismas teniendo unas invariantes en el proceso.

**Tip 32: Crash early.** Si se detecta un fallo y no se puede arreglar, es mejor que el programa se detenga a que continue la ejecución modificando cosas críticas.

**Tip 33: If it can't happen, use assertions to ensure that it won't.** Nunca des por hecho que una circunstancia no se va a dar y usa assertions para validar valores en tu código.

**Tip 34: Use exceptions for exceptional problems.** No uses excepciones para controlar el flujo de la aplicación, solo para cosas excepcionales.

**Tip 35: Finish what you start.** Controla la creación y supresión de recursos de tus aplicaciones.

**Tip 36: Minimize coupling between modules.** Intenta proporcionarle a los constructores y métodos de toda la información necesaria directamente, eliminando el acoplamiento entre módulos. Aplica siempre la [Ley de Demeter](https://es.wikipedia.org/wiki/Ley_de_Demeter).

**Tip 37: Configure, don't integrate.** Intenta usar metadatos para permitir modificar el programa sin tener que modificar el código, asi como almacenar todas las configuraciones.

**Tip 38: Put abstractions in code, details in metadata.** Programa para el caso general y almacena las especificaciones y configuraciones fuera del código compilable.

**Tip 39: Analyze workflows to improve concurrency.** Usar diagramas de actividad permite ver como podemos maximizar el paralelismo.

**Tip 40: Design user services.** Crea pequeños servicios independientes que permitan realizar tareas de forma independiente en paralelo.

**Tip 41: Always design for concurrency.** Al diseñar objetos o módulos, piensa que estos se pueden ejecutar en paralelo, por lo que es recomendable intenta que se pueda acceder a su estad de forma segura. También intenta eliminar siempre estados globales.

**Tip 42: Separate views from models.** Separando la responsabilidad de los elementos respecto a sus vistas ganas flexibilidad. También es recomendable separar la vista del elemento que la controla (MVC, MVP...).

**Tip 43: Use blackboards to coordinate workflows.** De esta forma, tendrás un repositorio común de objetos que pueden ser fácilmente utilizados en función de los requisitos del programa, controlando además el flujo de la aplicación.

**Tip 44: Don't program by coincidence.** Las cosas no deben funcionar por casualidad. Documenta y escribe código que funcione y sea sencillo, testea, entiende el porqué de ese código o cámbialo, no programes a ciegas sin entender que está sucediendo por debajo.

**Tip 45: Estimate the order of your algorithms.** Mientras programas, estima la complejidad de tu código: si esta es elevada, replantéate el algoritmo y hazlo eficiente. Usa estas estimaciones: bucles simples `O(n)`, anidados `O(n^2)`, particionado binario `O(log(n))`, divide y vencerás `O(nlog(n))` y combinatorio `O(2^n)`.

**Tip 46: Test your estimates.** Prueba tanto en un entorno real como en uno de pruebas para entender mejor el funcionamiento de tus algoritmos.

**Tip 47: Refactor early, refactor often.** No esperes a que pase el tiempo para refactorizar y hazlo con frecuencia. Refactoriza para eliminar duplicidad, para mejorar la independencia de tus módulos, por cambios al mejorar tu conocimiento del problema o por rendimiento.

**Tip 48: Design to test.** A la hora de programar, diseña y plantea tanto el programa como los tests, viendo así condiciones que deben cumplir y posibles problemas. Esto te permite desarrollar una buena interfaz antes de darle contenido.

**Tip 49: Test your software, or your users will.** Crea test y prueba bien tu código, no dejes que sean los usuarios los que encuentren los fallos.

**Tip 50: Don't use wizard code you don't understand.** Si generas código base usando wizards, detente y piensa antes si comprendes lo que hacen. En caso contrario no los uses.

**Tip 51: Don't gather requirements - dig for them.** Muchas veces los clientes no saben concretar los requisitos. Haz preguntas, detalla y concreta el comportamiento. Los requisitos se ocultan bajo capas de supuestos, conceptos erróneos y políticas.

**Tip 52: Work with a user to thing like a user.** Trabaja con él, entiendo su trabajo, tareas, problemas... para poder hacer un software que se adapte a él.

**Tip 53: Abstraction live longer than details.** Desarrolla intentando abstraer datos genéricos o condiciones generales sobre concretos.

**Tip 54: Use a project glossary.** Ten un glosario de palabras relacionadas con la aplicación y documenta y programa en base a dicho glosario.

**Tip 55: Don't think outside the box - find the box.** Identifica todas las restricciones reales del problema, no solo las indicadas.

**Tip 56: Liste to nagging doubts - start when you are ready.** Tu experiencia te puede advertir de que algo no está bien diseñado antes de empezar: escúchala.

**Tip 57: Some things are better done than described.** Al desarrollar, puedes localizar cosas que pueden ser generalizadas, algoritmos o formas más óptimas de hacer algo, o problemas y limitaciones no documentadas.

**Tip 58: Don't be a slave to formal methods.** Antes de aplicar una técnica para formalizar el programa, ponla en el contexto del proyecto y analizar sus ventajas y desventajas, y su adaptación a las habilidades del equipo.

**Tip 59: Expensive tools do not produce better designs.** Usa herramientas para ayudarte a diseñar un programa, pero no bases tu programa en ellas. El coste de las herramientas no quita que las salidas estén mal detalladas o contengan errores.

**Tip 60: Organize around functionality, not job functions.** Los diferentes trabajos realizados dentro de un proyecto no tienen que trabajar de forma aislada. Es mejor tener equipos por funcionalidades que por tareas.

**Tip 61: Don't use manual procedures.** Automatiza todas las tareas manuales para evitar problemas de interpretación o saltos de pasos. Usa shell scripts o constantes.

**Tip 62: Test early, test often, test automatically.** Empieza haciendo test desde el principio, testeando todo el código producido. Ejecuta test automáticamente (por la noche, al hacer commits...).

**Tip 63: Coding ain't done until all test runs.** Ejecuta siempre los test antes de decir que algo está terminado y comprueba que todo tiene un test. Testea de forma unitaria, la integración de los componentes, la validación y verificación de los usuarios (no automatizable), los recursos necesarios para su ejecución así como errores y recuperación, la eficiencia y la usabilidad.

**Tip 64: Use saboteurs to test your testing.** Comprueba que los test que has escrito fallan al romper intencionadamente el código, verificando que el test funciona correctamente. Puedes designar un saboteador que desconozca los test para introducir bugs y comprobar el resultado.

**Tip 65: Test state coverage, not code coverage.** Las lineas cubiertas por un test son útiles, pero es mas importante asegurarse de que se testean los estados suficientes. Un test puede pasar por un fragmento de código, pero no testear todos los estados necesarios del mismo.

**Tip 66: Find bugs once.** Si encuentras un bug, crea un test para que no se vuelva a repetir

**Tip 67: Treat english as just another programming language.** Aplica todos los consejos aprendidos a tu documentación.

**Tip 68: Build documentation in, don't bolt it on.** Hay dos tipos de documentación: interna (código, diseño, test...) y externa (manuales de usuario...). La segunda suele estar desactualizada y no documenta todo lo que puede pasar.

**Tip 69: Gently exceed your users expectations.** Intenta no sobrepasar en exceso las expectativas de los usuarios y nunca te quedes por debajo.

**Tip 70: Sign your work.**
