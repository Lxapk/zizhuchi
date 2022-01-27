from telethon import TelegramClient

try:
    from tg_config import api_id, api_hash, proxy
except:
    print("缺少配置,请在脚本同目录下添加配置")
    exit(3)


async def main():
    me = await client.get_me()
    print("当前用户昵称: {}".format(me.first_name))


if __name__ == '__main__':
    client = TelegramClient('tg_user', api_id, api_hash, proxy=proxy)
    with client:
        client.loop.run_until_complete(main())

