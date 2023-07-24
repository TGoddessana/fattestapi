:py:mod:`fattestapi.db.sqlalchemy.mixins`
=========================================

.. py:module:: fattestapi.db.sqlalchemy.mixins

.. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BaseMixin <fattestapi.db.sqlalchemy.mixins.BaseMixin>`
     - .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.BaseMixin
          :summary:
   * - :py:obj:`TimeStampedMixin <fattestapi.db.sqlalchemy.mixins.TimeStampedMixin>`
     - .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin
          :summary:
   * - :py:obj:`UUIDMixin <fattestapi.db.sqlalchemy.mixins.UUIDMixin>`
     - .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.UUIDMixin
          :summary:

API
~~~

.. py:class:: BaseMixin(*args, **kwargs)
   :canonical: fattestapi.db.sqlalchemy.mixins.BaseMixin

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.BaseMixin

   .. rubric:: Initialization

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.BaseMixin.__init__

.. py:class:: TimeStampedMixin(*args, **kwargs)
   :canonical: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin

   Bases: :py:obj:`fattestapi.db.sqlalchemy.mixins.BaseMixin`

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin

   .. rubric:: Initialization

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin.__init__

   .. py:attribute:: created_at
      :canonical: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin.created_at
      :value: None

      .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin.created_at

   .. py:attribute:: updated_at
      :canonical: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin.updated_at
      :value: None

      .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.TimeStampedMixin.updated_at

.. py:class:: UUIDMixin(*args, **kwargs)
   :canonical: fattestapi.db.sqlalchemy.mixins.UUIDMixin

   Bases: :py:obj:`fattestapi.db.sqlalchemy.mixins.BaseMixin`

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.UUIDMixin

   .. rubric:: Initialization

   .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.UUIDMixin.__init__

   .. py:attribute:: uuid
      :canonical: fattestapi.db.sqlalchemy.mixins.UUIDMixin.uuid
      :value: None

      .. autodoc2-docstring:: fattestapi.db.sqlalchemy.mixins.UUIDMixin.uuid
