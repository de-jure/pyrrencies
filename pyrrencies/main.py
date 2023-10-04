from typing import Literal
import urllib.request
import json

Currency = Literal[
    'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
    'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
    'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
    'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD',
    'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP',
    'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
    'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
    'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD',
    'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA',
    'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR',
    'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN',
    'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF',
    'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS',
    'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP',
    'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS',
    'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER',
    'ZAR', 'ZMW', 'ZWL',
]

class CurrencyAmount:
    cents: int
    currency: Currency

    def __init__(self, cents: int, currency: Currency):
        self.cents = cents
        self.currency = currency

    def to(self, currency: Currency):
        rate = CurrencyRates.get_rate(self.currency, currency)
        return CurrencyAmount(int(self.cents * rate), currency)

    def __repr__(self):
        return f"CurrencyAmount(cents={self.cents}, currency='{self.currency}')"

    def __str__(self):
        return f'{self.currency} {self.cents / 100}'

    def __add__(self, other):
        if isinstance(other, int):
            return CurrencyAmount(self.cents + other, self.currency)
        if isinstance(other, CurrencyAmount):
            if self.currency != other.currency:
                raise ValueError('Currencies must be the same')
            return CurrencyAmount(self.cents + other.cents, self.currency)
        raise ValueError('Can only add int or CurrencyAmount')

    def __sub__(self, other):
        if isinstance(other, int):
            return CurrencyAmount(self.cents - other, self.currency)
        if isinstance(other, CurrencyAmount):
            if self.currency != other.currency:
                raise ValueError('Currencies must be the same')
            return CurrencyAmount(self.cents - other.cents, self.currency)
        raise ValueError('Can only subtract int or CurrencyAmount')

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return CurrencyAmount(self.cents * other, self.currency)
        raise ValueError('Can only multiply by int or float')

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return CurrencyAmount(self.cents / other, self.currency)
        raise ValueError('Can only divide by int or float')

    def __eq__(self, other):
        return self.cents == other.cents and self.currency == other.currency

    def __ne__(self, other):
        return self.cents != other.cents or self.currency != other.currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError('Currencies must be the same')
        return self.cents < other.cents

    def __le__(self, other):
        if self.currency != other.currency:
            raise ValueError('Currencies must be the same')
        return self.cents <= other.cents

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError('Currencies must be the same')
        return self.cents > other.cents

    def __ge__(self, other):
        if self.currency != other.currency:
            raise ValueError('Currencies must be the same')
        return self.cents >= other.cents

    def __bool__(self):
        return bool(self.cents)



class CurrencyRates:
    _instance = None
    _exchange_rates = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrencyRates, cls).__new__(cls)
        return cls._instance

    @classmethod
    def set_rates(cls, base_currency, rates):
        cls._exchange_rates[base_currency] = rates

    @classmethod
    def get_rate(cls, base_currency, target_currency):
        if base_currency not in cls._exchange_rates:
            with urllib.request.urlopen(f'http://open.er-api.com/v6/latest/{base_currency}') as response:
                data = json.loads(response.read().decode('utf-8'))
                cls.set_rates(base_currency, data['rates'])

        return cls._exchange_rates[base_currency].get(target_currency, None)

    @classmethod
    def get_all_rates(cls):
        return cls._exchange_rates
