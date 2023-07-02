# kawazanyo
[![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue?style=plastic%26logo%3Dappveyor)](https://www.python.org/)
[![license](https://img.shields.io/badge/license-MIT-purple?style=plastic%26logo%3Dappveyor)](https://github.com/yu10kami/kawazanyo/blob/main/LICENSE)

**A library of calculating the profit and loss of Japanese stock.**

# Usage
The library has two functions.
## income
This function calculates the current profit/loss based on the purchase price and the number of shares held.
### Inputs (required) 
* `ticker (str)` - ticker code
* `purchase_info (list_2d)` - the purchase price and the number of shares held.
### Returns
* `date (str)` - Date of calculation for target
* `diff (list)` - Result of profit/loss calculation
* `p_and_l (float)` - Total profit/loss calculation result

### Example
```python
from kawazanyo import income

ticker='7203'
purchase_info = [[200, 1929.50],
                 [100, 2099.50],
                 [200, 2377.50],
                 [300, 1805.00]]

date, diff, p_and_l = income(ticker, purchase_info)
# returns
# date      : 20230612
# diff      : [-163000.0, 0.0, 460900.0, 547500.0]
# p_and_l   : 845400.0
```

## kawazanyo
The function calculates the future profit/loss based on the purchase price, the number of shares held, and the expected stock price.  
The function is a **"Don't count your chickens before they are hatched."** function.
### Inputs (required) 
* `future_price (float)` - future price
* `purchase_info (list_2d)` - the purchase price and the number of shares held.
### Returns
* `diff (list)` - Result of profit/loss calculation
* `p_and_l (float)` - Total profit/loss calculation result

### Example
```python
from kawazanyo import kawazanyo

purchase_info = [[200, 1929.50],
                 [100, 2099.50],
                 [200, 2377.50],
                 [300, 1805.00]]
future_price = 3000.00
diff, p_and_l = kawazanyo(purchase_info, future_price)
# returns
# diff      : [-163000.0, 0.0, 460900.0, 547500.0]
# p_and_l   : 845400.0
```

# Requirements
* yfinance>=0.2.20
* pandas>=2.0.2
* pandas-datareader>=0.10.0
* typing_extensions>=4.6.3
* numpy>=1.24.3

# Installing kawazanyo
```
$ pip install git+https://github.com/yu10kami/kawazanyo
```

# Support
Bugs may be reported at https://github.com/yu10kami/kawazanyo/issues

