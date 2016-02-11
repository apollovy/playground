"""Main entry point into app."""


import asyncio
import logging
import os

import zope.component as zcomp

import sqlalchemy as sa

import arstecnica.sqlalchemy.async as sa_async

import fmc.interfaces as ifs
import fmc.users.models as models
import fmc.users.tables as tables


LOGGER = logging.getLogger(__name__)


class App:
    """Incapsulates logic."""

    def __init__(self, loop):
        """Init with event loop."""
        self.loop = loop
        self.gsm = zcomp.getGlobalSiteManager()
        self.register()

    async def create_user(self, name):
        """Create a user."""
        user = ifs.IUser(name)
        registrator = ifs.IRegistrator(user)
        result = await registrator.register()
        print(result.inserted_primary_key)

        return user

    async def go(self):
        logging.basicConfig(level='DEBUG')
        dsn = 'postgres://postgres:{}@db/postgres'.format(
            os.environ.get('DB_PASSWORD', ''),
        )
        engine = sa_async.create_engine(dsn, loop=self.loop)
        metadata = sa.MetaData(bind=engine)
        async with await engine.connect() as conn:
            self.post_register(metadata, conn)
            await self.create_user('apollov')

    def register(self):
        """Fill the registry with adapters."""
        self.gsm.registerAdapter(models.User, [str], ifs.IUser),
        self.gsm.registerAdapter(models.UserRegistrator)

        for interface, obj in [
            (ifs.ITableFactory, lambda x: sa.Table),
            (ifs.IColumnFactory, lambda x: sa.Column),
            (ifs.IIntegerFactory, lambda x: sa.Integer),
            (ifs.IStringFactory, lambda x: sa.String),
            (ifs.ILoggerFactory, lambda x: logging),
        ]:
            LOGGER.debug('interface: %s', interface)
            LOGGER.debug('obj: %s', obj)
            self.gsm.registerAdapter(obj, [ifs.IFMCObject], interface)

    def post_register(self, metadata, connection):
        """Register what cannot be registered initially."""
        self.gsm.registerAdapter(
            lambda x: metadata, [ifs.IFMCObject], ifs.IMetadata,
        )
        self.gsm.registerAdapter(
            lambda x: connection, [ifs.IFMCObject], ifs.IConnection,
        )
        # tables.Tables() must be resolved after other things, because it
        # uses some of the interfaces described earlier
        self.gsm.registerAdapter(
            lambda x: tables.Tables().users, [ifs.IRegistrator], ifs.ITable,
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = App(loop)
    loop.run_until_complete(app.go())
