import sys
from datetime import datetime, timedelta
import platform
import json
import asyncio

import aiohttp

class Data():
    CURRENCIES = 'USD', 'EUR'


def json_to_text(obj):
    filtered_currencies = list(filter(lambda x: x['currency'] in (Data.CURRENCIES), obj['exchangeRate']))
    formatted_currencies = [{obj['date']: {x['currency']: {'sale': x.get('saleRate'), 'purchase': x.get('purchaseRate')}}} for x in filtered_currencies]
    text = json.dumps(formatted_currencies, indent=4)
    return text


def get_days(days):
    return [(datetime.now() - timedelta(days=day)) .strftime('%d.%m.%Y') for day in range(int(days))]


async def get_currencies_from_api_pb(date):
    async with aiohttp.ClientSession() as session:
        params = {'json': '', 'date': date}
        try:
            async with session.get('https://api.privatbank.ua/p24api/exchange_rates', params=params, ssl=True) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"{response.status}")
        except aiohttp.ClientConnectionError as err:
            print(err)


async def async_tasks(dates):
    async with asyncio.TaskGroup() as tg:
        results = []
        for date in dates:
            task = tg.create_task(get_currencies_from_api_pb(date))
            results.append(task)
    return results


async def main(days):
    dates = get_days(days)
    results = await async_tasks(dates)
    for r in results:
        print(json_to_text(r.result()))


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        days_arg = int(sys.argv[1])
        days = min(days_arg, 10)
        asyncio.run(main(days))
    except TypeError as err:
        print(f' {sys.argv[1]} is not a valid integer {err}')
        exit(1)
    except IndexError as err:
        print(f'Try this way -->   main.py <days_count>')
        exit(1)