import requests
from bs4 import BeautifulSoup

def personnel(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find('div', class_ = 'loses-item-title').find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find('div', class_ = 'loses-item-title').find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def tanks(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[1].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[1].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def bbm(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[2].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[2].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def artillery(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[3].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[3].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def AFV(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[4].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[4].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def air_defense(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[5].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[5].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def planes(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[6].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[6].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def helicopters(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[7].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[7].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def vehicles(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[8].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[8].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def warships(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[9].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[9].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def UAV(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[10].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[10].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def special_military_equip(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[11].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[11].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def ATGM_SRBM_systems(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[12].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[12].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error
    
def cruise_missiles(item):
    url = 'https://russianwarship.rip/'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    if item == 'total':
        total = bs.find_all('div', class_ = 'loses-item-title')[13].find_all('span')[0].text.strip()
        return total
    elif item == 'quantity':
        quantity = bs.find_all('div', class_ = 'loses-item-title')[13].find_all('span')[1].text.replace('За добу', '').replace('(', '').replace(')', '').strip()
        if '+' not in quantity:
            quantity = '--'
        return quantity
    else:
        error = 'error: invalid argument'
        return error

def date_func():
    url2 = 'https://www.calendardate.com/todays.htm'
    r2 = requests.get(url2)
    bs = BeautifulSoup(r2.text, 'html.parser')
    date_ = bs.find_all('tr', id = 'indtod')[3].find_all('td')[1].text.replace('-', '.').strip()
    return date_