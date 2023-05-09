import requests

def losses_detaited(date):
    try:
        url = 'https://russianwarship.rip/api/v2/statistics/' + date
        r = requests.get(url).json()
        r2 = r["data"]["stats"]
        data = f'Станом на {r["data"]["date"].replace("-", ".")}, {r["data"]["day"]} день війни\nОсобовий склад: {r2["personnel_units"]}\nТанки: {r2["tanks"]}\nББМ: {r2["armoured_fighting_vehicles"]}\nЛітаки: {r2["planes"]}\nГелікоптери: {r2["helicopters"]}\nАртилерія: {r2["artillery_systems"]}\nКораблі: {r2["warships_cutters"]}'
        return data
    except Exception:
        error = 'error: invalid date'
        return error