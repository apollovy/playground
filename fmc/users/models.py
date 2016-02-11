"""Models for users application."""
import zope.interface

import fmc.interfaces


@zope.interface.implementer(fmc.interfaces.IUser, fmc.interfaces.IRegistrable)
class User(object):
    def __init__(self, name):
        self.name = name
        self.table = fmc.interfaces.REGISTRY.lookup(
            [fmc.interfaces.IUser],
            fmc.interfaces.ITable,
        )
        self.connection = fmc.interfaces.REGISTRY.lookup(
            [fmc.interfaces.IUser],
            fmc.interfaces.IConnection,
        )

    async def register(self):
        statement = self.table.insert().values(name=self.name)
        return await self.connection.execute(statement)
