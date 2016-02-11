"""Main entry point into app."""


import asyncio
import logging
import os

import zope.interface.adapter

import sqlalchemy as sa

import arstecnica.sqlalchemy.async as sa_async

import fmc.interfaces as ifs
import fmc.users.models as models
import fmc.users.tables as tables


LOGGER = logging.getLogger(__name__)


async def go(loop):
    logging.basicConfig(level='DEBUG')
    dsn = 'postgres://postgres:{}@db/postgres'.format(
        os.environ.get('DB_PASSWORD', ''),
    )
    metadata = sa.MetaData()
    engine = sa_async.create_engine(dsn, loop=loop)
    async with await engine.connect() as conn:
        register(metadata, conn)
        apollov = models.User(name='apollov')
        result = await apollov.register()
        print(result.inserted_primary_key)


def register(metadata, connection):
    """Fill the registry with adapters."""
    for requirements, interface, name, obj in [
        ([ifs.IUser], ifs.IConnection, '', connection),
        ([ifs.IFMCObject], ifs.ITableFactory, '', sa.Table),
        ([ifs.IFMCObject], ifs.IColumnFactory, '', sa.Column),
        ([ifs.IFMCObject], ifs.IIntegerFactory, '', sa.Integer),
        ([ifs.IFMCObject], ifs.IStringFactory, '', sa.String),
        ([ifs.IFMCObject], ifs.IMetadata, '', metadata),
    ]:
        LOGGER.debug('requirements: %s', requirements)
        LOGGER.debug('interface: %s', interface)
        LOGGER.debug('name: %s', name)
        LOGGER.debug('obj: %s', obj)
        ifs.REGISTRY.register(requirements, interface, name, obj)
    # tables.Tables() must be resolved after other things, because it
    # uses some of the interfaces described earlier
    ifs.REGISTRY.register([ifs.IUser], ifs.ITable, '', tables.Tables().users)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go(loop))
