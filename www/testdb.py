import orm
from models import User, Blog, Comment
import asyncio


async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root', db='awesome')

    # u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    # u = User(name='John', email='john@example.com', passwd='1234567890', image='about:blank')
    u = User(name='Admin', email='admin@example.com', passwd='1234567890', image='about:blank')
    await u.save()

# 获取EventLoop:
loop = asyncio.get_event_loop()

# 把协程丢到EventLoop中执行
loop.run_until_complete(test())
