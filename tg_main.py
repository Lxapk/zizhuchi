"""
cron: * * * * 1
new Env('互助池自动上车');
"""
import asyncio
import re

from telethon import TelegramClient
from ql_api import get_crons, get_crons_log

try:
    from tg_config import api_id, api_hash, proxy
except:
    print("缺少配置,请在脚本同目录下添加配置")
    exit(3)


def get_code():
    pattern_code = r'/[a-z]+\s.*'
    result, data = get_crons("获取互助码")
    if not result or len(data) == 0:
        print("任务[获取互助码],不存在")
        return []
    result, data = get_crons_log(data[0]['id'])
    if not result:
        print("任务[获取互助码],日志获取失败")
        return []
    re_list = re.findall(pattern_code, data)
    return re_list


async def main():
    client = TelegramClient('tg_user', api_id, api_hash, proxy=proxy)
    await client.connect()
    if not await client.is_user_authorized():
        print('你还未登录,请登录后使用')
        return
    code_list = get_code()
    print("共获取到{}条数据".format(len(code_list)))
    for code in code_list:
        await client.send_message("@JDShareCodebot", code)
    print("发送完成")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
