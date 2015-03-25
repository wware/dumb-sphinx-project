Figuring out what Sphinx is all about
====

Afaik, Sphinx is the preferred way to document Python code. So let's
give it a try.

* http://sphinx-doc.org/contents.html

An earlier attempt with Sphinx didn't work out too well because, following an
online tutorial, I tried to set up my project with `sphinx-quickstart`. If
you're documenting code, you really want to start with `sphinx-apidoc`, something
like this.

```bash
sphinx-apidoc -A wware -F -o . hack
```

The difference between the two commands is that `sphinx-apidoc` will dig thru
your code and set up doc stubs which you can expand upon. These could be added
to the framework created by `sphinx-quickstart`, but if you're a Sphinx noob,
you might not need to know you need to do that, and whatever random online
tutorial you stumble across might not mention it.
