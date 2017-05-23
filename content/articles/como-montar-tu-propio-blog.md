Title: Cómo montar tu propio blog
Date: 2017-05-23
Category: Tutoriales
Tags: tech, blog, pelican, travis, tutorial, CI, github, github pages
Slug: como-montar-tu-propio-blog
Summary: Después de mucho tiempo queriendo escribir algún artículo, finalmente me he decidido empezar por algo sencillo: un pequeño tutorial contando el proceso de creación del blog y su puesta a punto para publicar automáticamente los cambios realizados. 

Después de mucho tiempo queriendo escribir algún artículo, finalmente me he decidido empezar por algo sencillo: un pequeño tutorial contando el proceso de creación del blog y su puesta a punto para publicar automáticamente los cambios que realizados. Como ya mencioné anteriormente, este blog está montado usando [GitHub Pages](https://pages.github.com/), [Pelican](http://docs.getpelican.com/en/stable/) con [Flex-Theme](https://github.com/alexandrevicenzi/Flex) y [Travis CI](https://travis-ci.org/).

A lo largo de este (largo) artículo explicaré como he utilizado todas estas herramientas para crear y automatizar todo el funcionamiento del blog.

## Preparando el repositorio

El primer paso para montar el blog es crear un repositorio en el que subir el código. En mi blog he utilizado un repositorio de GitHub, ya que en combinación con GitHub Pages permite mostrar código HTML sin necesidad de montar nada más. Otros populares repositorios, como Gitlab o Bitbucket tienen soluciones similares, aunque hay pasos en el tutorial que pueden variar.

Para crear el repositorio, el único requisito es que su nombre siga el patrón *username.github.io*, donde *username* será tu nombre de usuario de Github (en mi caso, *darkrodry.github.io*). En este repositorio, todo el contenido de la rama *master* será lo que se muestre en el blog. Yo he creado además otra rama llamada *source* para subir el código utilizado para generar el blog.

También os recomiendo darle un vistazo al funcionamiento de [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), ya que lo utilizaremos más adelante para agregar algunas dependencias necesarias para la compilación.

## Iniciando Pelican

Como indican en su [web](http://docs.getpelican.com/en/stable/), Pelican es una herramienta escrita en Python que permite generar sitios web estáticos a partir de una serie de ficheros [Markdown](https://es.wikipedia.org/wiki/Markdown) o [reStructuredText](http://docutils.sourceforge.net/rst.html).

Para instalar Pelican en tu ordenador necesitas tener Python. Recomiendo usar la versión 3.5 o superior, ya que tuve algún problema usando la 2.7 (si queréis mantener ambas versiones probad [pyenv](https://github.com/pyenv/pyenv)). Pelican se encuentra dentro de *pip*, por lo que instalarlo es tan sencillo como ejecutar en tu terminal:

```bash
pip install pelican
```

Pelican proporciona un simple quickstart para generar el esqueleto del proyecto, así como los ficheros de configuración y un Makefile para ejecutar el mismo. Para ejecutar este quickstart (dentro de la rama elegida para subir el código al repositorio) escribe en tu terminal el siguiente comando y responde a las preguntas:

```bash
pelican-quickstart
```

En mi blog he usado en gran parte la configuración por defecto, a excepción de:

- nombre y autor del blog
- url: usad la que os debería haber generado GitHub
- cuando pregunte si queréis publicar vuestra web en GitHub Pages responded que sí, y confirmad la url.

No os preocupéis si configuráis algo mal, está configuración se puede modificar más adelante sin ningún problema.

<img style="display: block; margin-left: auto; margin-right: auto" src="images/pelican-quickstart-demo.png">

Una vez finalizado el quickstart, podrás observar que se han generado una serie de ficheros y carpetas. Los más importantes son:

- *content/*: en este directorio va todo el contenido del blog (artículos, imágenes...)
- *output/*: aquí se almacena el contenido autogenerado al usar Pelican. Es muy recomendable agregar este fichero a nuestro .gitignore
- *pelicanconf.py*: fichero de configuración principal con parámetros comunes y de despliegue local
- *publishconf.py*: fichero que sobreescribe parte de la configuración de *pelicanconf.py* con los parámetros necesarios a la hora de publicar

Antes de continuar, puedes comprobar que todo se ha generado correctamente con el siguiente comando:

```bash
make html && make serve
``` 

Una vez se haya generado el html y se levante el servidor, carga la url [http://localhost:8000/](http://localhost:8000/) en tu navegador para ver tus avances.

<img style="display: block; margin-left: auto; margin-right: auto" src="images/pelican-first-execution.png">

## Creando el primer post

Una vez llegados a este punto, es el momento de empezar a agregar contenido al blog. Pelican interpreta que cualquier fichero dentro del directorio *content/* es un artículo del blog, y los utilizará para generar el contenido del mismo. Hay una excepción a esto, ya que si creamos una carpeta *content/pages/* considerará el contenido de la misma como contenido estático del sitio, como puede ser las páginas con información sobre el autor, contacto o proyectos personales.

Para crear contenido en el blog, puedes utilizar dos formatos: [Markdown](https://es.wikipedia.org/wiki/Markdown) o [reStructuredText](http://docutils.sourceforge.net/rst.html). En mi caso he decidido utilizar Markdown ya que estoy más familiarizado con ello y lo uso con algo de frecuencia. 

Crear un artículo es tan sencillo como agregar un fichero a la carpeta *content/* y escribir dentro lo que quieras contar. Para que este artículo sea considerado como tal, hay que agregar antes un pequeño apartado con información sobre el mismo. El resultado de tu artículo 

```markdown
Title: Título del post (obligatorio)
Date: 2017-05-21 10:20 (obligatorio)
Modified: 2017-05-22 19:30
Category: Artículo
Tags: tutorial, blog, pelican
Slug: articulo-de-ejemplo
Authors: Rodrigo de Frutos
Summary: Resumen sobre el contenido del post

A partir de aquí, el contenido de tu nuevo artículo usando *Markdown*.
```

Una vez creado el artículo, prueba a generar de nuevo el blog y comprueba el resultado.

<img style="display: block; margin-left: auto; margin-right: auto" src="images/pelican-first-post.png">

Puedes ver más información sobre cómo crear artículos en [la documentación de Pelican](http://docs.getpelican.com/en/stable/content.html#file-metadata).

## Personalizando el blog

A estas alturas puede ser que estés empezando a dudar del estilo ofrecido por tu blog. Otro de los puntos fuertes de Pelican es que permite cambiar el tema del blog, poniendo a disposición de los usuarios un [gran catálogo de temas](http://www.pelicanthemes.com/), además de permitir [crear nuestros propios temas](http://docs.getpelican.com/en/stable/themes.html). Para mi blog, decidí empezar con la opción sencilla y utilizar un tema ya existente, eligiendo finalmente [Flex](https://github.com/alexandrevicenzi/Flex).

Para agregar este tema (o cualquier otro) al blog, hay que hacer dos pequeños cambios. Lo primero es descargar el código del tema. Yo he decidido importar el tema usando [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) con el siguiente comando:

```bash
git submodule add https://github.com/alexandrevicenzi/Flex.git theme-flex
```

Una vez tenemos el tema en nuestro repositorio, para que el tema se aplique en el blog hay que modificar el fichero de configuración. Abre el fichero *pelicanconf.py* y añade la siguiente línea (o modifícala en caso de que ya exista): `THEME = "theme-flex"`.

Pero esta personalización no acaba aquí. Al abrir el fichero de configuración habrás podido observar que hay otros campos que, o están vacíos o te indican que insertes tu información. Tanto Pelican como el tema que hayas elegido te permitirán personalizar mucha información que mostrará en el blog, como puede ser tu nombre, una biografía, tus redes sociales o agregar Google Analytics. En el caso de Flex, puedes consultar la sección de [custom settings](https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings) de su Wiki.

Para terminar, posiblemente quieras tener una bio un poco más extensa que la que te permite el tema (es muy breve, al estilo Twitter). Pelican interpreta que cualquier fichero dentro de *content/pages* es una página estática, sin formato artículo, a tu blog. Todos los ficheros que agregues en este directorio crearán una nueva entrada en el menú de tu blog.

## Actualización automática

La última tarea para dejar tu blog listo es delegar la tarea de la generación del mismo usando integración continua. Para esta tarea he elegido utilizar [Travis CI](https://travis-ci.org/), ya que es un servicio de integración gratuito y muy extendido (y que tenía ganas de probar, la verdad).

El primer paso de todos es crearte una cuenta en Travis CI asignada a tu usuario de GitHub. Para habilitar Travis CI en nuestro proyecto hay que agregar un fichero *.travis.yml* en tu repositorio con el siguiente contenido:

```yaml
language: python
python:
  - "3.5"
branches:
  only:
  - [rama con el código, source en mi caso]
before_install:
  - sudo apt-get update && sudo apt-get --reinstall install -qq language-pack-es
install:
  - pip install -r requirements.txt
script:
  - make publish github
env:
  global:
  - LANG=es_ES.UTF-8
  - LC_ALL=es_ES.UTF-8
  - secure: [Token de Travis Encriptado]
```

Como podrás observar, este fichero tiene un campo `secure:` con un token. ¿De dónde sale este token? Es el encargado de permitir a Travis subir a la rama master el resultado de la generación del blog. Este token se puede generar en la sección de ajustes de tu cuenta de GitHub, en la sección de [personal access tokens](https://github.com/settings/tokens). Crea tu nuevo token poniéndole un nombre representativo y con permisos completos para acceder a repositorios privados.

Para dar seguridad a este token, la gente de Travis CI tiene un cliente en Ruby con diferentes herramientas, y entre ellas una para cifrar estas claves. Para instalar estas herramientas necesitaremos tener Ruby en nuestro ordenador e instalar una nueva gema:

```bash
gem install travis
```

Una vez instalada, ejecuta el siguiente comando en la raíz de tu repositorio para agregar el token a tu fichero *.travis.yml*:

```bash
travis encrypt GH_TOKEN=<<token en bruto>> --add --override
```

También es necesario agregar un fichero *requirements.txt* a tu repositorio con aquellas dependencias necesarias para generar el blog. Para obtener este fichero basta con ejecutar el siguiente comando en tu repositorio:

```bash
pip freeze > requirements.txt
```

Por último, es necesario hacer un pequeño cambio en el *Makefile* para permitir subir el resultado de Travis a la rama master de nuestro repositorio de Github.

```yaml
github: publish
	ghp-import -b $(GITHUB_PAGES_BRANCH) -n $(OUTPUTDIR)
	@git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git $(GITHUB_PAGES_BRANCH) > /dev/null
```

Para hacer la última prueba, simplemente agrega los últimos cambios en un commit y sube los cambios al repositorio. Pasado uno o dos minutos, deberías ver el resultado de todo el tutorial desplegado en tu GitHub Pages personal. ¡Ahora solo te queda crear artículos y mantener actualizado tu blog!