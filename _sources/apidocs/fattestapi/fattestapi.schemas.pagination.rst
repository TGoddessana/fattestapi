:py:mod:`fattestapi.schemas.pagination`
=======================================

.. py:module:: fattestapi.schemas.pagination

.. autodoc2-docstring:: fattestapi.schemas.pagination
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PaginationRequestSchema <fattestapi.schemas.pagination.PaginationRequestSchema>`
     - .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationRequestSchema
          :summary:
   * - :py:obj:`PaginationResponseSchema <fattestapi.schemas.pagination.PaginationResponseSchema>`
     - .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema
          :summary:

API
~~~

.. py:class:: PaginationRequestSchema
   :canonical: fattestapi.schemas.pagination.PaginationRequestSchema

   Bases: :py:obj:`marshmallow.Schema`

   .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationRequestSchema

   .. py:attribute:: page
      :canonical: fattestapi.schemas.pagination.PaginationRequestSchema.page
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationRequestSchema.page

   .. py:attribute:: per_page
      :canonical: fattestapi.schemas.pagination.PaginationRequestSchema.per_page
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationRequestSchema.per_page

   .. py:method:: to_entity(data, **kwargs) -> fattestapi.httptypes.pagination.PaginationRequest
      :canonical: fattestapi.schemas.pagination.PaginationRequestSchema.to_entity

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationRequestSchema.to_entity

.. py:class:: PaginationResponseSchema
   :canonical: fattestapi.schemas.pagination.PaginationResponseSchema

   Bases: :py:obj:`marshmallow.Schema`

   .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema

   .. py:attribute:: count
      :canonical: fattestapi.schemas.pagination.PaginationResponseSchema.count
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema.count

   .. py:attribute:: next_page
      :canonical: fattestapi.schemas.pagination.PaginationResponseSchema.next_page
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema.next_page

   .. py:attribute:: previous_page
      :canonical: fattestapi.schemas.pagination.PaginationResponseSchema.previous_page
      :value: None

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema.previous_page

   .. py:method:: to_entity(data, **kwargs) -> fattestapi.httptypes.pagination.PaginationResponse
      :canonical: fattestapi.schemas.pagination.PaginationResponseSchema.to_entity

      .. autodoc2-docstring:: fattestapi.schemas.pagination.PaginationResponseSchema.to_entity
