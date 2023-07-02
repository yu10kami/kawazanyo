#coding:utf-8
from kawazanyo import income

ticker='7203'
purchase_info = [[200, 1929.50],
                 [100, 2099.50],
                 [200, 2377.50],
                 [300, 1805.00]]
date, diff, p_and_l = income(ticker, purchase_info)
print(date)
print(diff)
print(p_and_l)

from kawazanyo import kawazanyo
future_price = 3000.00
diff, p_and_l = kawazanyo(purchase_info, future_price)
print(diff)
print(p_and_l)