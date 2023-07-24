:py:mod:`fattestapi.repositories.crud`
======================================

.. py:module:: fattestapi.repositories.crud

.. autodoc2-docstring:: fattestapi.repositories.crud
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CRUDRepositoryABC <fattestapi.repositories.crud.CRUDRepositoryABC>`
     - .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC
          :summary:

API
~~~

.. py:class:: CRUDRepositoryABC
   :canonical: fattestapi.repositories.crud.CRUDRepositoryABC

   Bases: :py:obj:`fattestapi.repositories.base.BaseRepository`, :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`fattestapi.repositories.base.T`\ ]

   .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC

   .. py:method:: save(entity: fattestapi.repositories.base.T) -> fattestapi.repositories.base.T
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.save
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.save

   .. py:method:: save_all(entities: typing.List[fattestapi.repositories.base.T]) -> typing.List[fattestapi.repositories.base.T]
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.save_all
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.save_all

   .. py:method:: read_by_id(id: int) -> typing.Optional[fattestapi.repositories.base.T]
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.read_by_id
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.read_by_id

   .. py:method:: is_exists_by_id(id) -> bool
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.is_exists_by_id
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.is_exists_by_id

   .. py:method:: read_all(sorting_request: fattestapi.httptypes.SortingRequest, filtering_request: fattestapi.httptypes.FilteringRequest) -> typing.List[typing.Optional[fattestapi.repositories.base.T]]
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.read_all
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.read_all

   .. py:method:: read_all_by_ids(ids: typing.List[int]) -> typing.List[typing.Optional[fattestapi.repositories.base.T]]
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.read_all_by_ids
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.read_all_by_ids

   .. py:method:: count() -> int
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.count
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.count

   .. py:method:: delete_by_id(id: int) -> None
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.delete_by_id
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.delete_by_id

   .. py:method:: delete(entity) -> None
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.delete
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.delete

   .. py:method:: delete_all_by_ids(ids: typing.List[int]) -> None
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.delete_all_by_ids
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.delete_all_by_ids

   .. py:method:: delete_all() -> None
      :canonical: fattestapi.repositories.crud.CRUDRepositoryABC.delete_all
      :abstractmethod:

      .. autodoc2-docstring:: fattestapi.repositories.crud.CRUDRepositoryABC.delete_all
