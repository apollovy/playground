"""Play here carefully."""
import zope.interface.registry


class IUser1(zope.interface.Interface):
    """A User with forst attribute."""

    a1 = zope.interface.Attribute("""Attribute 1""")


class IUser2(zope.interface.Interface):
    """A User with second attribute."""

    a2 = zope.interface.Attribute("""Attribute 2""")


class ITool(zope.interface.Interface):
    """A tool."""


@zope.interface.implementer(IUser1)
class User1:
    def __init__(self, a1):
        self.a1 = a1


@zope.interface.implementer(IUser2)
class User2:
    def __init__(self, a2):
        self.a2 = a2


@zope.interface.implementer(IUser1, IUser2)
class User12:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2


def test_providedby():
    u1 = User1(1)
    u2 = User2(2)
    u12 = User12(1, 2)
    print(list(zope.interface.providedBy(u1)))
    print(list(zope.interface.providedBy(u2)))
    print(list(zope.interface.providedBy(u12)))


def test_registry():
    registry = zope.interface.registry.AdapterRegistry()
    registry.register([IUser1], ITool, '', 42)
    registry.register([], ITool, '', 12)
    print(registry.lookup([IUser1], ITool))
    print(registry.lookup([IUser1, IUser2], ITool))
    print(registry.lookup([], ITool))


def sync():
    print('I\'m not async!')


async def is_async():
    print('I\'m async!')


def test_call_from_sync():
    print('print(sync())')
    print(sync())
    print('print(is_async())')
    print(is_async())


async def test_call_from_async_no_await():
    print('print(sync())')
    print(sync())
    print('print(is_async())')
    print(is_async())


async def test_call_from_async_await():
    print('print(await sync())')
    print(await sync())
    print('print(await is_async())')
    print(await is_async())


if __name__ == '__main__':
    print('test_call_from_sync()')
    test_call_from_sync()
    print('test_call_from_async_await().send(None)')
    test_call_from_async_await().send(None)
    print('test_call_from_async_no_await().send(None)')
    test_call_from_async_no_await().send(None)
