:py:mod:`fattestapi.factory.factory`
====================================

.. py:module:: fattestapi.factory.factory

.. autodoc2-docstring:: fattestapi.factory.factory
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Config <fattestapi.factory.factory.Config>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.Config
          :summary:
   * - :py:obj:`Container <fattestapi.factory.factory.Container>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.Container
          :summary:
   * - :py:obj:`Container2 <fattestapi.factory.factory.Container2>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.Container2
          :summary:
   * - :py:obj:`Factory <fattestapi.factory.factory.Factory>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.Factory
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`fa <fattestapi.factory.factory.fa>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.fa
          :summary:
   * - :py:obj:`app <fattestapi.factory.factory.app>`
     - .. autodoc2-docstring:: fattestapi.factory.factory.app
          :summary:

API
~~~

.. py:class:: Config
   :canonical: fattestapi.factory.factory.Config

   .. autodoc2-docstring:: fattestapi.factory.factory.Config

   .. py:attribute:: API_TITLE
      :canonical: fattestapi.factory.factory.Config.API_TITLE
      :value: <Multiline-String>

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.API_TITLE

   .. py:attribute:: API_VERSION
      :canonical: fattestapi.factory.factory.Config.API_VERSION
      :value: <Multiline-String>

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.API_VERSION

   .. py:attribute:: OPENAPI_VERSION
      :canonical: fattestapi.factory.factory.Config.OPENAPI_VERSION
      :value: '3.0.0'

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.OPENAPI_VERSION

   .. py:attribute:: OPENAPI_URL_PREFIX
      :canonical: fattestapi.factory.factory.Config.OPENAPI_URL_PREFIX
      :value: '/'

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.OPENAPI_URL_PREFIX

   .. py:attribute:: OPENAPI_SWAGGER_UI_PATH
      :canonical: fattestapi.factory.factory.Config.OPENAPI_SWAGGER_UI_PATH
      :value: '/'

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.OPENAPI_SWAGGER_UI_PATH

   .. py:attribute:: OPENAPI_SWAGGER_UI_URL
      :canonical: fattestapi.factory.factory.Config.OPENAPI_SWAGGER_UI_URL
      :value: 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.OPENAPI_SWAGGER_UI_URL

   .. py:attribute:: SQLALCHEMY_DATABASE_URI
      :canonical: fattestapi.factory.factory.Config.SQLALCHEMY_DATABASE_URI
      :value: 'sqlite:///:memory:'

      .. autodoc2-docstring:: fattestapi.factory.factory.Config.SQLALCHEMY_DATABASE_URI

.. py:class:: Container
   :canonical: fattestapi.factory.factory.Container

   Bases: :py:obj:`dependency_injector.containers.DeclarativeContainer`

   .. autodoc2-docstring:: fattestapi.factory.factory.Container

   .. py:attribute:: string1
      :canonical: fattestapi.factory.factory.Container.string1
      :value: None

      .. autodoc2-docstring:: fattestapi.factory.factory.Container.string1

.. py:class:: Container2
   :canonical: fattestapi.factory.factory.Container2

   Bases: :py:obj:`dependency_injector.containers.DeclarativeContainer`

   .. autodoc2-docstring:: fattestapi.factory.factory.Container2

   .. py:attribute:: string2
      :canonical: fattestapi.factory.factory.Container2.string2
      :value: None

      .. autodoc2-docstring:: fattestapi.factory.factory.Container2.string2

.. py:class:: Factory
   :canonical: fattestapi.factory.factory.Factory

   .. autodoc2-docstring:: fattestapi.factory.factory.Factory

   .. py:attribute:: BASE_DIR
      :canonical: fattestapi.factory.factory.Factory.BASE_DIR
      :value: None

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory.BASE_DIR

   .. py:attribute:: FASTAPI_CLS
      :canonical: fattestapi.factory.factory.Factory.FASTAPI_CLS
      :type: type[fastapi.FastAPI]
      :value: None

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory.FASTAPI_CLS

   .. py:attribute:: DI_CONTAINERS
      :canonical: fattestapi.factory.factory.Factory.DI_CONTAINERS
      :type: typing.Sequence[typing.Type[dependency_injector.containers.DeclarativeContainer | dependency_injector.containers.DynamicContainer]]
      :value: None

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory.DI_CONTAINERS

   .. py:method:: create_app(environment: str) -> fastapi.FastAPI
      :canonical: fattestapi.factory.factory.Factory.create_app

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory.create_app

   .. py:method:: _create_fastapi() -> fastapi.FastAPI
      :canonical: fattestapi.factory.factory.Factory._create_fastapi

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory._create_fastapi

   .. py:method:: _route(_app: fastapi.FastAPI) -> None
      :canonical: fattestapi.factory.factory.Factory._route

      .. autodoc2-docstring:: fattestapi.factory.factory.Factory._route

.. py:data:: fa
   :canonical: fattestapi.factory.factory.fa
   :value: None

   .. autodoc2-docstring:: fattestapi.factory.factory.fa

.. py:data:: app
   :canonical: fattestapi.factory.factory.app
   :value: None

   .. autodoc2-docstring:: fattestapi.factory.factory.app
