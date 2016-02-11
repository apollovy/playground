"""Tables declarations for users app."""
import logging

import zope.component as zcomp
import zope.interface as zif

import fmc.interfaces as ifs


LOGGER = logging.getLogger(__name__)


@zif.implementer(ifs.IFMCObject)
class Tables:
    """Incapsulation of tables creation."""

    def __init__(self):
        self.gsm = zcomp.getGlobalSiteManager()
        self._metadata = ifs.IMetadata(self)
        self._table_factory = ifs.ITableFactory(self)
        self._column_factory = ifs.IColumnFactory(self)
        self._integer_factory = ifs.IIntegerFactory(self)
        self._string_factory = ifs.IStringFactory(self)
        LOGGER.debug(
            'self._metadata: %s', self._metadata,
        )
        LOGGER.debug(
            'self._table_factory: %s', self._table_factory,
        )
        LOGGER.debug(
            'self._column_factory: %s', self._column_factory,
        )
        LOGGER.debug(
            'self._integer_factory: %s', self._integer_factory,
        )
        LOGGER.debug(
            'self._string_factory: %s', self._string_factory,
        )

    @property
    def users(self):
        return self._table_factory(
            'users', self._metadata,
            self._column_factory(
                'user_id', self._integer_factory, primary_key=True,
            ),
            self._column_factory('name', self._string_factory(50)),
        )
