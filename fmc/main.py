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


async def create_user(name):
    """Create a user."""
    user = ifs.IUser(name)
    registrator = ifs.IRegistrator(user)
    result = await registrator.register()
    print(result.inserted_primary_key)

    return user


async def go(loop):
    logging.basicConfig(level='DEBUG')
    dsn = 'postgres://postgres:{}@db/postgres'.format(
        os.environ.get('DB_PASSWORD', ''),
    )
    engine = sa_async.create_engine(dsn, loop=loop)
    metadata = sa.MetaData(bind=engine)
    async with await engine.connect() as conn:
        register(metadata, conn)
        await create_user('apollov')


def register(metadata, connection):
    """Fill the registry with adapters."""
    gsm = zcomp.getGlobalSiteManager()
    gsm.registerAdapter(models.User, [str], ifs.IUser),
    gsm.registerAdapter(models.UserRegistrator)

    for interface, obj in [
        (ifs.IConnection, lambda x: connection),
        (ifs.ITableFactory, lambda x: sa.Table),
        (ifs.IColumnFactory, lambda x: sa.Column),
        (ifs.IIntegerFactory, lambda x: sa.Integer),
        (ifs.IStringFactory, lambda x: sa.String),
        (ifs.IMetadata, lambda x: metadata),
    ]:
        LOGGER.debug('interface: %s', interface)
        LOGGER.debug('obj: %s', obj)
        gsm.registerAdapter(obj, [ifs.IFMCObject], interface)
    # tables.Tables() must be resolved after other things, because it
    # uses some of the interfaces described earlier
    gsm.registerAdapter(
        lambda x: tables.Tables().users, [ifs.IRegistrator], ifs.ITable,
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go(loop))
