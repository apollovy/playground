"""Models for users application."""
import zope.component as zcomp
import zope.interface as zif

import fmc.interfaces as ifs


@zif.implementer(ifs.IUser)
class User:
    def __init__(self, name):
        self.name = name


@zif.implementer(ifs.IRegistrator)
@zcomp.adapter(ifs.IUser)
class UserRegistrator:
    def __init__(self, user):
        self.user = user
        self.table = ifs.ITable(self)
        self.connection = ifs.IConnection(self)

    async def register(self):
        statement = self.table.insert().values(name=self.user.name)
        return await self.connection.execute(statement)
