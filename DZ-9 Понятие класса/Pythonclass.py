{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Что сегодня сделаем\n",
    "Библиотеку для получения курсов валют в 2 строки"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from libs.exchange import Rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Rate().usd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "Rate('full').AZN()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задача\n",
    "Дана строка со значениями, которые разделены запятыми:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "line = '2019-07-01,organic,4293'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Напишите функцию column_count, которая возвращает число столбцов в такой строке"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len('2019-07-01,organic,4293'.split(','))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def line_count(line, count_empty_lines=True, sep=','):\n",
    "    if count_empty_lines:\n",
    "        return len(line.split(sep))\n",
    "    else:\n",
    "        if line:\n",
    "            return len(line.split(sep))\n",
    "        else:\n",
    "            return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line_count(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line_count('2019-07-01')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line_count('', count_empty_lines=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Классы\n",
    "Пример использования переменной в разных методах"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "class AnyName:\n",
    "    def method_1(self):\n",
    "        self.currency = 'usd'\n",
    "    \n",
    "    def method_2(self):\n",
    "        print(self.currency)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = AnyName()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "datetime.strptime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "a.method_1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'usd'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.currency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = AnyName()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'AnyName' object has no attribute 'currency'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-23-59f1720a6a7b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mb\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmethod_2\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-14-9c2240d258f9>\u001b[0m in \u001b[0;36mmethod_2\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mmethod_2\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrency\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'AnyName' object has no attribute 'currency'"
     ]
    }
   ],
   "source": [
    "b.method_2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'usd'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.currency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "usd\n"
     ]
    }
   ],
   "source": [
    "a.method_2()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Метод __init__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# метод __init__ выполняется при вызове класса\n",
    "\n",
    "class Rate:\n",
    "    def __init__(self):\n",
    "        self.format = 'value'\n",
    "        print(self.format)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value\n"
     ]
    }
   ],
   "source": [
    "r = Rate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'value'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.format"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Класс для курсов валют"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rate:\n",
    "    def __init__(self):\n",
    "        self.format = 'value'\n",
    "    \n",
    "    def show_current_format(self):\n",
    "        return self.format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = Rate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'value'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.show_current_format()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Пример инициализации со значением переменной"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rate:\n",
    "    def __init__(self, format_):\n",
    "        self.format = format_\n",
    "    \n",
    "    def show_current_format(self):\n",
    "        return self.format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = Rate(format_='value')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "r.show_current_format()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Или сразу со значением по умолчанию"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rate:\n",
    "    def __init__(self, format_='value'):\n",
    "        self.format = format_\n",
    "    \n",
    "    def show_current_format(self):\n",
    "        return self.format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'value'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r = Rate()\n",
    "r.show_current_format()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'full'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_full = Rate(format_='full')\n",
    "r_full.show_current_format()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'value'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'full_123'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# значения переменных класса можно менять\n",
    "\n",
    "r.format = 'full_123'\n",
    "r.show_current_format()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Задание\n",
    "Создайте класс сотрудника Employee. При инициализации класса задается имя сотрудника name и его текущая зарплата salary. Напишите следующие методы:\n",
    "1. Метод up, который увеличивает зарплату сотрудника на 100\n",
    "2. Метод print, который выводит на экран текущую зарплату сотрудника в формате \"Сотрудник Иван, зарплата 100\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee:\n",
    "    def __init__(self, name, salary):\n",
    "        self.name = name\n",
    "        self.salary = salary\n",
    "    \n",
    "    def up(self):\n",
    "        self.salary += 100\n",
    "    \n",
    "    def print_(self):\n",
    "        print('Сотрудник {}, зарплата {}'.format(self.name, self.salary))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "ivan = Employee(name='Иван', salary=50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ivan.salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Сотрудник Иван, зарплата 1350\n"
     ]
    }
   ],
   "source": [
    "ivan.up()\n",
    "ivan.print_()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "elena = Employee(name='Елена', salary=300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Сотрудник Елена, зарплата 1000\n"
     ]
    }
   ],
   "source": [
    "elena.up()\n",
    "elena.print_()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Полная версия класса"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rate:\n",
    "    def __init__(self, format_='value'):\n",
    "        self.format = format_\n",
    "    \n",
    "    def exchange_rates(self):\n",
    "        \"\"\"\n",
    "        Возвращает ответ сервиса с информацией о валютах в виде:\n",
    "        \n",
    "        {\n",
    "            'AMD': {\n",
    "                'CharCode': 'AMD',\n",
    "                'ID': 'R01060',\n",
    "                'Name': 'Армянских драмов',\n",
    "                'Nominal': 100,\n",
    "                'NumCode': '051',\n",
    "                'Previous': 14.103,\n",
    "                'Value': 14.0879\n",
    "                },\n",
    "            ...\n",
    "        }\n",
    "        \"\"\"\n",
    "        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')\n",
    "        return self.r.json()['Valute']\n",
    "    \n",
    "    def make_format(self, currency):\n",
    "        \"\"\"\n",
    "        Возвращает информацию о валюте currency в двух вариантах:\n",
    "        - полная информация о валюте при self.format = 'full':\n",
    "        Rate('full').make_format('EUR')\n",
    "        {\n",
    "            'CharCode': 'EUR',\n",
    "            'ID': 'R01239',\n",
    "            'Name': 'Евро',\n",
    "            'Nominal': 1,\n",
    "            'NumCode': '978',\n",
    "            'Previous': 79.6765,\n",
    "            'Value': 79.4966\n",
    "        }\n",
    "        \n",
    "        Rate('value').make_format('EUR')\n",
    "        79.4966\n",
    "        \"\"\"\n",
    "        response = self.exchange_rates()\n",
    "        \n",
    "        if currency in response:\n",
    "            if self.format == 'full':\n",
    "                return response[currency]\n",
    "            \n",
    "            if self.format == 'value':\n",
    "                return response[currency]['Value']\n",
    "        \n",
    "        return 'Error'\n",
    "    \n",
    "    def eur(self):\n",
    "        \"\"\"Возвращает курс евро на сегодня в формате self.format\"\"\"\n",
    "        return self.make_format('EUR')\n",
    "    \n",
    "    def usd(self):\n",
    "        \"\"\"Возвращает курс доллара на сегодня в формате self.format\"\"\"\n",
    "        return self.make_format('USD')\n",
    "    \n",
    "    def brl(self):\n",
    "        \"\"\"Возвращает курс бразильского реала на сегодня в формате self.format\"\"\"\n",
    "        return self.make_format('BRL')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = Rate(format_='full')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'AUD': {'ID': 'R01010',\n",
       "  'NumCode': '036',\n",
       "  'CharCode': 'AUD',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Австралийский доллар',\n",
       "  'Value': 47.7337,\n",
       "  'Previous': 47.8415},\n",
       " 'AZN': {'ID': 'R01020A',\n",
       "  'NumCode': '944',\n",
       "  'CharCode': 'AZN',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Азербайджанский манат',\n",
       "  'Value': 40.9491,\n",
       "  'Previous': 40.9759},\n",
       " 'GBP': {'ID': 'R01035',\n",
       "  'NumCode': '826',\n",
       "  'CharCode': 'GBP',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Фунт стерлингов Соединенного королевства',\n",
       "  'Value': 86.3951,\n",
       "  'Previous': 87.1687},\n",
       " 'AMD': {'ID': 'R01060',\n",
       "  'NumCode': '051',\n",
       "  'CharCode': 'AMD',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Армянских драмов',\n",
       "  'Value': 14.4762,\n",
       "  'Previous': 14.4436},\n",
       " 'BYN': {'ID': 'R01090B',\n",
       "  'NumCode': '933',\n",
       "  'CharCode': 'BYN',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Белорусский рубль',\n",
       "  'Value': 29.2617,\n",
       "  'Previous': 29.212},\n",
       " 'BGN': {'ID': 'R01100',\n",
       "  'NumCode': '975',\n",
       "  'CharCode': 'BGN',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Болгарский лев',\n",
       "  'Value': 39.8833,\n",
       "  'Previous': 40.0034},\n",
       " 'BRL': {'ID': 'R01115',\n",
       "  'NumCode': '986',\n",
       "  'CharCode': 'BRL',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Бразильский реал',\n",
       "  'Value': 12.9365,\n",
       "  'Previous': 13.3136},\n",
       " 'HUF': {'ID': 'R01135',\n",
       "  'NumCode': '348',\n",
       "  'CharCode': 'HUF',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Венгерских форинтов',\n",
       "  'Value': 22.5376,\n",
       "  'Previous': 22.6802},\n",
       " 'HKD': {'ID': 'R01200',\n",
       "  'NumCode': '344',\n",
       "  'CharCode': 'HKD',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Гонконгских долларов',\n",
       "  'Value': 89.7663,\n",
       "  'Previous': 89.8262},\n",
       " 'DKK': {'ID': 'R01215',\n",
       "  'NumCode': '208',\n",
       "  'CharCode': 'DKK',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Датская крона',\n",
       "  'Value': 10.4633,\n",
       "  'Previous': 10.4959},\n",
       " 'USD': {'ID': 'R01235',\n",
       "  'NumCode': '840',\n",
       "  'CharCode': 'USD',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Доллар США',\n",
       "  'Value': 69.5725,\n",
       "  'Previous': 69.618},\n",
       " 'EUR': {'ID': 'R01239',\n",
       "  'NumCode': '978',\n",
       "  'CharCode': 'EUR',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Евро',\n",
       "  'Value': 78.0047,\n",
       "  'Previous': 78.2924},\n",
       " 'INR': {'ID': 'R01270',\n",
       "  'NumCode': '356',\n",
       "  'CharCode': 'INR',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Индийских рупий',\n",
       "  'Value': 91.3115,\n",
       "  'Previous': 91.4391},\n",
       " 'KZT': {'ID': 'R01335',\n",
       "  'NumCode': '398',\n",
       "  'CharCode': 'KZT',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Казахстанских тенге',\n",
       "  'Value': 17.225,\n",
       "  'Previous': 17.164},\n",
       " 'CAD': {'ID': 'R01350',\n",
       "  'NumCode': '124',\n",
       "  'CharCode': 'CAD',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Канадский доллар',\n",
       "  'Value': 51.209,\n",
       "  'Previous': 51.3748},\n",
       " 'KGS': {'ID': 'R01370',\n",
       "  'NumCode': '417',\n",
       "  'CharCode': 'KGS',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Киргизских сомов',\n",
       "  'Value': 92.8919,\n",
       "  'Previous': 93.1286},\n",
       " 'CNY': {'ID': 'R01375',\n",
       "  'NumCode': '156',\n",
       "  'CharCode': 'CNY',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Китайских юаней',\n",
       "  'Value': 98.2898,\n",
       "  'Previous': 98.3166},\n",
       " 'MDL': {'ID': 'R01500',\n",
       "  'NumCode': '498',\n",
       "  'CharCode': 'MDL',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Молдавских леев',\n",
       "  'Value': 40.3319,\n",
       "  'Previous': 40.3583},\n",
       " 'NOK': {'ID': 'R01535',\n",
       "  'NumCode': '578',\n",
       "  'CharCode': 'NOK',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Норвежских крон',\n",
       "  'Value': 73.0458,\n",
       "  'Previous': 73.5174},\n",
       " 'PLN': {'ID': 'R01565',\n",
       "  'NumCode': '985',\n",
       "  'CharCode': 'PLN',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Польский злотый',\n",
       "  'Value': 17.5285,\n",
       "  'Previous': 17.5272},\n",
       " 'RON': {'ID': 'R01585F',\n",
       "  'NumCode': '946',\n",
       "  'CharCode': 'RON',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Румынский лей',\n",
       "  'Value': 16.1077,\n",
       "  'Previous': 16.1759},\n",
       " 'XDR': {'ID': 'R01589',\n",
       "  'NumCode': '960',\n",
       "  'CharCode': 'XDR',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'СДР (специальные права заимствования)',\n",
       "  'Value': 96.0372,\n",
       "  'Previous': 96.0631},\n",
       " 'SGD': {'ID': 'R01625',\n",
       "  'NumCode': '702',\n",
       "  'CharCode': 'SGD',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Сингапурский доллар',\n",
       "  'Value': 49.9121,\n",
       "  'Previous': 49.9986},\n",
       " 'TJS': {'ID': 'R01670',\n",
       "  'NumCode': '972',\n",
       "  'CharCode': 'TJS',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Таджикских сомони',\n",
       "  'Value': 67.497,\n",
       "  'Previous': 67.5411},\n",
       " 'TRY': {'ID': 'R01700J',\n",
       "  'NumCode': '949',\n",
       "  'CharCode': 'TRY',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Турецкая лира',\n",
       "  'Value': 10.1447,\n",
       "  'Previous': 10.1519},\n",
       " 'TMT': {'ID': 'R01710A',\n",
       "  'NumCode': '934',\n",
       "  'CharCode': 'TMT',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Новый туркменский манат',\n",
       "  'Value': 19.9063,\n",
       "  'Previous': 19.9193},\n",
       " 'UZS': {'ID': 'R01717',\n",
       "  'NumCode': '860',\n",
       "  'CharCode': 'UZS',\n",
       "  'Nominal': 10000,\n",
       "  'Name': 'Узбекских сумов',\n",
       "  'Value': 68.4095,\n",
       "  'Previous': 68.3803},\n",
       " 'UAH': {'ID': 'R01720',\n",
       "  'NumCode': '980',\n",
       "  'CharCode': 'UAH',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Украинских гривен',\n",
       "  'Value': 26.029,\n",
       "  'Previous': 25.9925},\n",
       " 'CZK': {'ID': 'R01760',\n",
       "  'NumCode': '203',\n",
       "  'CharCode': 'CZK',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Чешских крон',\n",
       "  'Value': 29.2469,\n",
       "  'Previous': 29.4206},\n",
       " 'SEK': {'ID': 'R01770',\n",
       "  'NumCode': '752',\n",
       "  'CharCode': 'SEK',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Шведских крон',\n",
       "  'Value': 73.9299,\n",
       "  'Previous': 74.5598},\n",
       " 'CHF': {'ID': 'R01775',\n",
       "  'NumCode': '756',\n",
       "  'CharCode': 'CHF',\n",
       "  'Nominal': 1,\n",
       "  'Name': 'Швейцарский франк',\n",
       "  'Value': 73.2034,\n",
       "  'Previous': 73.3439},\n",
       " 'ZAR': {'ID': 'R01810',\n",
       "  'NumCode': '710',\n",
       "  'CharCode': 'ZAR',\n",
       "  'Nominal': 10,\n",
       "  'Name': 'Южноафриканских рэндов',\n",
       "  'Value': 39.9679,\n",
       "  'Previous': 40.422},\n",
       " 'KRW': {'ID': 'R01815',\n",
       "  'NumCode': '410',\n",
       "  'CharCode': 'KRW',\n",
       "  'Nominal': 1000,\n",
       "  'Name': 'Вон Республики Корея',\n",
       "  'Value': 57.5869,\n",
       "  'Previous': 57.5294},\n",
       " 'JPY': {'ID': 'R01820',\n",
       "  'NumCode': '392',\n",
       "  'CharCode': 'JPY',\n",
       "  'Nominal': 100,\n",
       "  'Name': 'Японских иен',\n",
       "  'Value': 65.0545,\n",
       "  'Previous': 65.0666}}"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.exchange_rates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'ID': 'R01235',\n",
       " 'NumCode': '840',\n",
       " 'CharCode': 'USD',\n",
       " 'Nominal': 1,\n",
       " 'Name': 'Доллар США',\n",
       " 'Value': 69.5725,\n",
       " 'Previous': 69.618}"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.usd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = Rate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "69.5725"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.usd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "r.exchange_rates()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Документация необходима почти всем методам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "?r.exchange_rates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Наследование"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Разработчикам финансового департамента помимо курса надо работать с кодами валют. Как сохранить сохранить разработку класса Rate у нас, а полезные функции передать финансистам?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "class CurrencyCodes(Rate):\n",
    "    def __init__(self):\n",
    "        super().__init__(format_='full')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Теперь классу CurrencyCodes доступны все методы класса Rate. Можем продолжать разработку в нужном направлении."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "cc = CurrencyCodes()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'ID': 'R01235',\n",
       " 'NumCode': '840',\n",
       " 'CharCode': 'USD',\n",
       " 'Nominal': 1,\n",
       " 'Name': 'Доллар США',\n",
       " 'Value': 69.5725,\n",
       " 'Previous': 69.618}"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CurrencyCodes().usd()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Допишем в класс что-нибудь свое новенькое"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "class CurrencyCodes(Rate):\n",
    "    def __init__(self):\n",
    "        super().__init__(format_='full')\n",
    "    \n",
    "    def currency_id(self, currency):\n",
    "        \"\"\"Получение идентификатора валюты\"\"\"\n",
    "        return self.make_format(currency)['ID']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "currency = CurrencyCodes()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'R01235'"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "currency.currency_id('USD')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Система повышения сотрудников"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee:\n",
    "    def __init__(self, name, seniority):\n",
    "        self.name = name\n",
    "        self.seniority = seniority\n",
    "        \n",
    "        self.grade = 1\n",
    "    \n",
    "    def grade_up(self):\n",
    "        \"\"\"Повышает уровень сотрудника\"\"\"\n",
    "        self.grade += 1\n",
    "    \n",
    "    def publish_grade(self):\n",
    "        \"\"\"Публикация результатов аккредитации сотрудников\"\"\"\n",
    "        print(self.name, self.grade)\n",
    "    \n",
    "    def check_if_it_is_time_for_upgrade(self):\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Developer(Employee):\n",
    "    def __init__(self, name, seniority):\n",
    "        super().__init__(name, seniority)\n",
    "    \n",
    "    def check_if_it_is_time_for_upgrade(self):\n",
    "        # для каждой аккредитации увеличиваем счетчик на 1\n",
    "        # пока считаем, что все разработчики проходят аккредитацию\n",
    "        self.seniority += 1\n",
    "        \n",
    "        # условие повышения сотрудника из презентации\n",
    "        if self.seniority % 5 == 0:\n",
    "            self.grade_up()\n",
    "        \n",
    "        # публикация результатов\n",
    "        return self.publish_grade()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "# проверяем как работает система повышения сотрудников на примере отдела разработки\n",
    "\n",
    "# разработчик Александр только что пришел в компанию\n",
    "alex = Developer('Александр', 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Александр 1\n",
      "Александр 1\n",
      "Александр 1\n",
      "Александр 1\n",
      "Александр 2\n",
      "Александр 2\n",
      "Александр 2\n",
      "Александр 2\n",
      "Александр 2\n",
      "Александр 3\n",
      "Александр 3\n",
      "Александр 3\n",
      "Александр 3\n",
      "Александр 3\n",
      "Александр 4\n",
      "Александр 4\n",
      "Александр 4\n",
      "Александр 4\n",
      "Александр 4\n",
      "Александр 5\n"
     ]
    }
   ],
   "source": [
    "for i in range(20):\n",
    "    alex.check_if_it_is_time_for_upgrade()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Импорт классов и функций"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "from libs.exchange import my_sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_sum(1, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "from libs.exchange import Rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "40.9491"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Rate().AZN()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# такой способ импорта крайне не рекомендуется\n",
    "from libs.exchange import *"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Если библиотека лежит в произвольной папке"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['/Users/kbashevoy/Desktop/Нетология/Занятия/Записи/06. Классы в python',\n",
       " '/Users/kbashevoy/anaconda3/lib/python37.zip',\n",
       " '/Users/kbashevoy/anaconda3/lib/python3.7',\n",
       " '/Users/kbashevoy/anaconda3/lib/python3.7/lib-dynload',\n",
       " '',\n",
       " '/Users/kbashevoy/.local/lib/python3.7/site-packages',\n",
       " '/Users/kbashevoy/anaconda3/lib/python3.7/site-packages',\n",
       " '/Users/kbashevoy/anaconda3/lib/python3.7/site-packages/aeosa',\n",
       " '/Users/kbashevoy/anaconda3/lib/python3.7/site-packages/IPython/extensions',\n",
       " '/Users/kbashevoy/.ipython',\n",
       " '/Users/kbashevoy/Desktop/Нетология/Занятия/Записи/06. Классы в python/libs',\n",
       " 'адрес_папки_с_файлами',\n",
       " '/Users/kbashevoy/Desktop/Нетология/Занятия/Записи/06. Классы в python/libs']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sys\n",
    "sys.path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "# пример\n",
    "\n",
    "import sys\n",
    "sys.path.append('/Users/kbashevoy/Desktop/Нетология/Занятия/Записи/06. Классы в python/libs')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "from exchange import my_sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_sum(3, 3)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
