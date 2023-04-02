# darkrodry.github.io [![publish blog](https://github.com/darkrodry/darkrodry.github.io/actions/workflows/publish.yaml/badge.svg)](https://github.com/darkrodry/darkrodry.github.io/actions/workflows/publish.yaml)

Source files for my personal blog.

There is an article (in Spanish) describing the steps to create your personal blog inside my blog: [https://darkrodry.github.io/como-montar-tu-propio-blog.html](https://darkrodry.github.io/como-montar-tu-propio-blog.html)

Developed using [GitHub Pages](https://pages.github.com/), [Pelican](http://docs.getpelican.com/en/stable/) con [Flex-Theme](https://github.com/alexandrevicenzi/Flex) and [Travis CI](https://travis-ci.org/).

### How to run

I develop the blog in local using virtualenv. To create the environment and start it, just run:

```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you can generate the html and the server using:

```
make html
pelican --listen
```
