# pythai-scb-unofficial

## Description
PyThaiSCB is an unofficial python library to pull bank account balances data from SCB (Siam Commercial Bank) Easy Net website using Selenium webdriver. Using web crawling under the hood, the function call is slow as it depends solely on the performance of SCB Easy Net website.

### Available features:

1. Get the list of all the bank accounts and their relevant information: account type, account number, account nickname and outstanding balance
2. Feel free to reach out to me to request for more features !

## Disclaimer
This is a non-profit project that was initiated to solve the pain of having no official open APIs made available from the bank. The library DOES NOT keep your credentials. Nevertheless, use it at your own risk.

## Installation
```bash
pip install pythai-scb
```

## Usage
```python
from pythai_scb import PyThaiSCB

scb_acc = PyThaiSCB(username='your_scbeasynet_username', password='your_scbeasynet_password')
bank_acc_df = scb_acc.get_account_bal_df()
```