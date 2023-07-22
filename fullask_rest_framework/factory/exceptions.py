class FullaskFactoryError(Exception):
    pass


class ConfigNotSetError(FullaskFactoryError):
    pass


class ExtensionError(FullaskFactoryError):
    pass
