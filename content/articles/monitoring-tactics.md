Title: Tácticas para monitorización
Date: 2022-07-10
Category: Monitoring
Tags: libros, tech, monitoring, practical monitoring,
Slug: tacticas-monitorizacion
Status: published
Summary: En esta segunda parte del resumen de *Practical Monitoring* nos centraremos más en que puntos de todo el sistema monitorizar, desde los diferentes puntos de vista de todas sus componentes: negocio, aplicaciones, infraestructura, seguridad...

En el [anterior artículo](principios-basicos-monitorizacion.html) hice un resumen sobre cuales son los principios básicos para monitorizar tus aplicaciones: la importancia que tiene y varios patrones y antipatrones a tener en cuenta. En esta segunda parte nos centraremos más en que puntos de todo el sistema monitorizar, desde los diferentes puntos de vista de todas sus componentes: negocio, aplicaciones, infraestructura, seguridad...

### Monitorizar el negocio

Uno de los puntos más importantes sobre el que tener métricas es el negocio. Es la forma más rápida de ver si el sistema está funcionando correctamente o el impacto que pueden tener nuevos desarrollos sobre todo el sistema. Para poder saber que testear correctamente, es importante definir unos buenos KPIs (key performance indicator) y relacionar estos KPI con elementos de nuestro sistema.

Hay varios KPI comunes en las empresas: ingresos recurrentes mensuales, los ingresos por empleado, el [NPS](https://es.wikipedia.org/wiki/Net_Promoter_Score), el *customer lifetime value*, el coste de adquisición de usuario, el margen de beneficios... Trata de buscar cómo impacta la plataforma en estos valores y agrega métricas para detectar comportamientos extraños lo antes posible. Ejemplos pueden ser el número total de usuarios activos o los productos/servicios contratados (por los que se paga dinero).

### Monitorizar el frontend

Una de las cosas a las que menos atención se le presta es a las métricas de los diferentes clientes en nuestro sistema. A la hora de obtener métricas en front hay dos tipos de aproximaciones: monitorización de usuarios reales (RUM) y de usuarios sintéticos (creando falsas peticiones bajo diferentes condiciones).

Una herramienta muy común para monitorizar fronts es Google Analytics, una herramienta tipo RUM que analiza cómo interacciona el usuario con el cliente.

A la hora de monitorizar el front, es importante controlar el tiempo de carga de las diferentes páginas usando el [API *PerformanceNavigationTiming*](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming) (utiliza los eventos `domComplete - navigationStart` y `domInteractive - navigationStart`). También es bueno almacenar logs (y no volcarlos por `console.log()`) y enviar los errores de JavScript.

Cualquier métrica relacionada con los tiempos de carga puede ser integrada en tu flujo de CI para asegurar que se mantienen unos tiempos adecuados, y también hay soluciones para configurar

### Monitorizar el backend

Para monitorizar tu aplicación backend es recomendable controlar los servicios clave. Para ello se puede controlar tanto llamadas exitosas/fallidas, duración de cada llamada, etc. Cualquier dato que sea relevante para tu negocio. Para controlar estas métricas existen herramientas como [StatsD](https://github.com/statsd/statsd).

Estas métricas generadas son muy útiles para controlar las releases, tanto para analizar el uso de nuevas funcionalidad desplegadas como para detectar posibles errores introducidos.

También es importante generar logs en tu aplicación. Ten cuidado con los logs que generas, ya que es fácil generar logs en exceso (o en defecto). Una buena forma de saber que logear es responder a las preguntas que te harías en caso de que algo falle.

Otro patrón muy útil en la monitorización es el endpoint de *health*, que se utiliza para conocer de un vistazo el estado de la aplicación.

En el caso de que tu aplicación esté basada en lambdas o microservicios es importante tener trazabilidad de las peticiones entre diferentes piezas, pudiendo analizar el origen y por dónde ha pasado cada petición.

### Monitorizar el servidor

El propio sistema operativo del servidor es capaz de proporcionar métricas útiles: CPU, memoria (RAM, cachés...), estado de red, discos duros, carga del procesador... También es importante controlar otras cosas cómo los certificados SSL, el estado de los servidores web o si los *crons* se han ejecutado.

Dentro de tu servidor puede haber otros componentes que controlar cómo balanceadores de carga, colas de mensajes, la base de datos, cachés, DNS... En caso de estar dentro de una infraestructura corporativa asegúrate también de monitorizar los diferentes elementos dentro de la misma.

### Monitorizar la red

Monitorizar el correcto funcionamiento de la red es una tarea complicada. Existe un protocolo llamado [SNMP](https://es.wikipedia.org/wiki/Protocolo_simple_de_administraci%C3%B3n_de_red) que se encarga de almacenar y gestionar múltiple métricas, pero su implementación es muy dependiente del fabricante de los equipos. Entre las métricas más comunes está la latencia, el ancho de banda, la capacidad, los errores o el *jitter* (fluctuaciones de red)

Intenta almacenar el historial de configuraciones y de notificar cuando se producen cambios.

En caso de tener servicios de streaming de voz o video, necesitarás agregar métricas para controlar que ofreces un buen servicio de codificación a tus usuarios.

### Monitorizar la seguridad

Es muy probable que tu sistema tenga que cumplir unas certificaciones de seguridad. Monitorizar estos requisitos (origen de las conexiones, usuarios que las realizan, ejecución de antivirus...) es una forma eficiente de controlar el cumplimiento de los mismos de cara a auditorias.

Otro punto a controlar son las conexiones SSH efectuadas o las ejecuciones a nivel de superusuario. Puedes usar herramientas como [*auditd*](https://www.man7.org/linux/man-pages/man8/auditd.8.html) para ayudarte con esta tarea. También es importante controlar los *syslog*.

Una vez dentro de tu sistema, hay que controlar dos frentes usando *Host Intrusion Detection Systems* (HIDS) y *Network Intrusion Detection Systems* (NIDS). Para el primero es útil usar [*rkhunter*](http://rkhunter.sourceforge.net/) para ayudarte a detectar rootkits. Para ayudarte a analizar el trafico de red dentro de tu infraestructura puedes usar *network taps*, que interceptan todo el tráfico y lo envían a otro sistema para su análisis.
