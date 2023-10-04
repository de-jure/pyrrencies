# Pyrrencies Python Library

## Overview

The `Pyrrencies` library provides a convenient way to handle currency conversion and arithmetic operations in Python. It supports a wide range of currencies and allows for easy conversion between them.

## Installation

```bash
pip install Pyrrencies
```

## Usage

### Initialization

```python
amount_usd = CurrencyAmount(1000, 'USD')  # USD 10.0
amount_uah = CurrencyAmount(10000, 'UAH')  # UAH 100.0
```

### Accessing Properties

```python
print(amount_usd.cents)  # 1000
print(amount_usd.currency)  # USD
```

### Display

```python
print(amount_usd)  # USD 10.0
```

### Currency Conversion

```python
print(amount_usd.to('UAH'))  # UAH 367.44
print(amount_usd.to('EUR'))  # EUR 9.55
```

### Arithmetic Operations

```python
print(amount_usd + 50)  # USD 10.5
print(amount_usd + amount_uah)  # ValueError: Currencies must be the same
```

### Comparison

```python
print(amount_usd == amount_uah)  # False
print(amount_usd != amount_uah)  # True
```

### Supported Currencies

AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, FOK, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLE, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VES, VND, VUV, WST, XAF, XCD, XDR, XOF, XPF, YER, ZAR, ZMW, ZWL
