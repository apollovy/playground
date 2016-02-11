"""Interfaces for FMC project."""
import zope.interface.adapter


class IFMCObject(zope.interface.Interface):
    """An object of FMC app."""


class IUser(IFMCObject):
    """A User of an application."""

    name = zope.interface.Attribute("""A name of a User""")


class IRegistrable(zope.interface.Interface):
    """Something that can be registered."""

    def register():
        """Perform registration in system."""


class ITable(zope.interface.Interface):
    """A table in the database declaration."""

    def insert():
        """Perform insertion into database."""


class ITableFactory(zope.interface.Interface):
    """A factory for `ITable` objects."""

    def __call__(name, imetadata, *columns):
        """Create a `ITable` object."""


class IColumnFactory(zope.interface.Interface):
    """A factory to produce Columns."""

    def __call__(name, type_, **kwargs):
        """Create a Column."""


class IConnection(zope.interface.Interface):
    """A connection to the database."""

    def execute(statement):
        """Execute a `statement` against database."""


class IMetadata(zope.interface.Interface):
    """A metadata object to keep `ITable`s and links between them."""


class IDBFieldTypeFactory(zope.interface.Interface):
    """A factory for DB field type."""


class IIntegerFactory(IDBFieldTypeFactory):
    """A factory for Integer DB type."""


class IStringFactory(IDBFieldTypeFactory):
    """A factory for String DB type."""


REGISTRY = zope.interface.adapter.AdapterRegistry()


def lookup1(interface):
    """Lookup adapter inside REGISTRY for IFMCObject and interface."""
    return REGISTRY.lookup1(IFMCObject, interface)
