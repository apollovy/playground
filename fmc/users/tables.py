"""Tables declarations for users app."""
import logging

import zope.interface.adapter

import fmc.interfaces as ifs


LOGGER = logging.getLogger(__name__)


class Tables:
    """Incapsulation of tables creation."""

    def __init__(self):
        self._metadata = ifs.lookup1(ifs.IMetadata)
        self._table_factory = ifs.lookup1(ifs.ITableFactory)
        self._column_factory = ifs.lookup1(ifs.IColumnFactory)
        self._integer_factory = ifs.lookup1(ifs.IIntegerFactory)
        self._string_factory = ifs.lookup1(ifs.IStringFactory)
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
