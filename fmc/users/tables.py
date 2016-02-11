"""Tables declarations for users app."""
import zope.interface as zif

import fmc.interfaces as ifs


@zif.implementer(ifs.IFMCObject)
class Tables:
    """Incapsulation of tables creation."""

    def __init__(self):
        self.logger = ifs.ILoggerFactory(self).getLogger(__name__)
        self._metadata = ifs.IMetadata(self)
        self._table_factory = ifs.ITableFactory(self)
        self._column_factory = ifs.IColumnFactory(self)
        self._integer_factory = ifs.IIntegerFactory(self)
        self._string_factory = ifs.IStringFactory(self)
        self.logger.debug(
            'self._metadata: %s', self._metadata,
        )
        self.logger.debug(
            'self._table_factory: %s', self._table_factory,
        )
        self.logger.debug(
            'self._column_factory: %s', self._column_factory,
        )
        self.logger.debug(
            'self._integer_factory: %s', self._integer_factory,
        )
        self.logger.debug(
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
