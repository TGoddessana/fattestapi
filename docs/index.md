-------------------------------
title: FattestAPI Documentation
-------------------------------

```{image} ./_static/full_logo.svg
:width: 500px
```

# FattestAPI Documentation
**The fattest way to develop REST APIs. based on FastAPI.**

## About FattestAPI

### What is it and why was it developed?

The FattestAPI package is built on top of the excellent Python web framework, FastAPI, and the widely-used
object-relational mapper, SQLAlchemy. It was developed with the goal of providing the "fattest way" to build REST APIs
by offering commonly used boilerplate code.

In fact, I was an avid fan of the Flask web framework, and I still love it. In fact, the initial name of this package
was Fullask-REST-framework, and it was developed with the intention of extending the micro web framework Flask with
batteries included.

However, while developing REST APIs using Flask, I encountered difficulties in documenting the APIs using Swagger. Of
course, you can achieve documentation using excellent frameworks like:

- [Flask-Smorest](https://github.com/marshmallow-code/flask-smorest), which supports OpenAPI 3.0 with Flask and marshmallow
- [Flask-RESTx](https://github.com/python-restx/flask-restx), which supports OpenAPI 3.0 also.  with their own framework

And it's **definitely not**  that these packages are inadequate. But I wanted a framework that takes an even better
approach
to documentation, and that's when I came across the fantastic package, FastAPI. So, I decided to migrate the existing
framework based on FastAPI.
It was inspired by the excellent and widely-used web frameworks such as Django and Django REST Framework, Spring and
Spring Data Projects, and NestJS.

### Goals of FattestAPI

FattestAPI aims to achieve the following:

* Provide pre-built boilerplate code for commonly performed CRUD (Create, Read, Update, Delete) operations, making it
  easy for developers to handle them.
* Support Layered Architecture by officially supporting Controller, Service, and Repository, making it easier for
  developers to achieve separation of concerns.
* Support an authentication system.
* Provide commonly used utility codes.

```{toctree}
:hidden:
:caption: 📚 Guides

guide/installation.rst
guide/usage.md
```

```{toctree}
:hidden:
:caption: 🧑🏻‍🤝‍🧑🏻 Contributing

contributing/contributing.md
contributing/authors.md
```

```{toctree}
:hidden:
:caption: 📖 API Reference

../apidocs/index.md
```
