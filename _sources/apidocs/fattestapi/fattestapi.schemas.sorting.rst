:py:mod:`fattestapi.schemas.sorting`
====================================

.. py:module:: fattestapi.schemas.sorting

.. autodoc2-docstring:: fattestapi.schemas.sorting
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SortingRequestSchema <fattestapi.schemas.sorting.SortingRequestSchema>`
     - .. autodoc2-docstring:: fattestapi.schemas.sorting.SortingRequestSchema
          :summary:

API
~~~

.. py:class:: SortingRequestSchema
   :canonical: fattestapi.schemas.sorting.SortingRequestSchema

   Bases: :py:obj:`flask_marshmallow.Schema`

   .. autodoc2-docstring:: fattestapi.schemas.sorting.SortingRequestSchema

   .. py:attribute:: sort_by
      :canonical: fattestapi.schemas.sorting.SortingRequestSchema.sort_by
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.sorting.SortingRequestSchema.sort_by

   .. py:method:: to_entity(data, **kwargs) -> fattestapi.httptypes.sorting.SortingRequest
      :canonical: fattestapi.schemas.sorting.SortingRequestSchema.to_entity

      .. autodoc2-docstring:: fattestapi.schemas.sorting.SortingRequestSchema.to_entity
