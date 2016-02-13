"""Interfaces for FMC project."""
# pylint:disable=inherit-non-class
# pylint:disable=no-self-argument
# pylint:disable=no-method-argument
import zope.interface as zif


class IFMCObject(zif.Interface):
    """An object of FMC app."""


class IUser(IFMCObject):
    """A User of an application."""

    name = zif.Attribute("""A name of a User""")


class IRegistrator(IFMCObject):
    """Something that registers another one."""

    async def register(obj):
        """Register `obj`."""


class ITable(zif.Interface):
    """A table in the database declaration."""

    def insert():
        """Perform insertion into database."""


class ITableFactory(zif.Interface):
    """A factory for `ITable` objects."""

    def __call__(name, imetadata, *columns):
        """Create a `ITable` object."""


class IColumnFactory(zif.Interface):
    """A factory to produce Columns."""

    def __call__(name, type_, **kwargs):
        """Create a Column."""


class IConnection(zif.Interface):
    """A connection to the database."""

    async def execute(statement):
        """Execute a `statement` against database."""


class IMetadata(zif.Interface):
    """A metadata object to keep `ITable`s and links between them."""


class IDBFieldTypeFactory(zif.Interface):
    """A factory for DB field type."""


class IIntegerFactory(IDBFieldTypeFactory):
    """A factory for Integer DB type."""


class IStringFactory(IDBFieldTypeFactory):
    """A factory for String DB type."""


class ILoggerFactory(zif.Interface):
    """Something that creates loggers."""

    def getLogger(name):  # pylint:disable=invalid-name
        """Return `ILogger` object."""


class ILogger(zif.Interface):
    """Object that can log."""

    def debug(message, *args, **kwargs):
        """Send debug message."""

    def info(message, *args, **kwargs):
        """Send info message."""

    def warning(message, *args, **kwargs):
        """Send warning message."""

    def exception(message, *args, **kwargs):
        """Send exception message."""

    def error(message, *args, **kwargs):
        """Send error message."""

    def critical(message, *args, **kwargs):
        """Send critical message."""

    def fatal(message, *args, **kwargs):
        """Send fatal message."""
