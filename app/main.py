"""Main entry point into app."""


import asyncio
import aiopg


DSN = 'dbname=postgres user=postgres password=2451 host=db'


async def go():
    pool = await aiopg.create_pool(DSN)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")
            ret = []
            async for row in cur:
                ret.append(row)
                assert ret == [(1,)]
            await cur.execute(
                """INSERT INTO users ("userName") VALUES ('apollov')"""
            )
            await cur.execute("SELECT * FROM users")
            ret = []
            async for row in cur:
                ret.append(row)
                try:
                    assert ret == [(1, 'apollov')]
                except AssertionError:
                    print(ret)


if __name__ == '__main__':
    print('start')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    print('finish')
