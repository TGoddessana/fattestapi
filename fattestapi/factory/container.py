import typing as t

from dependency_injector import providers
from dependency_injector.containers import (
    Container,
    DeclarativeContainer,
    DynamicContainer,
)


class Something:
    pass


class Container1(DeclarativeContainer):
    string1 = providers.Factory(Something)


class Container2(DeclarativeContainer):
    string2 = providers.Factory(Something)


class AppContainers(list):
    def __init__(
        self,
        *containers: t.Optional[t.Union[DeclarativeContainer, DynamicContainer]],
    ):
        super().__init__()
        for container in containers:
            assert isinstance(container, (DynamicContainer, DeclarativeContainer))
            self.append(container)
            print(container.__class__)

    def __repr__(self) -> str:
        return f"<AppContainers {super().__repr__()}>"

    def unwire_all(self) -> None:
        pass

    def unwire(self, container_name: t.Optional[str]) -> None:
        pass


container1 = Container1()
container2 = Container2()

app_container = AppContainers(container1, container2)
print(app_container)
