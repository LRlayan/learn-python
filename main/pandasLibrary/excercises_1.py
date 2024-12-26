data_table = {
    "orderId":[101,102,103,104,105],
    "product":["laptop","smart phone","desk chair","monitor","book shelf"],
    "category":["electronic","electronics","furniture","electronic","furniture"],
    "qty":[2,5,10,4,2],
    "pricePerUnit":[1000,800,150,200,300],
    "region":["north","south","east","west","north"]
}

# you are the data analyst for a reatil company
# the company has provided you about table containg sales data.your task is to analyst sales data using python and pandas to answer some key business quections
# 1.calculate the total revenue for each order (add a new column total revenue to store the total revenue for each order)
# 2.identify the best any product find the product with the highest total sales revenue

import pandas as pd

# Answer 1
data_frame_3 = pd.DataFrame(data_table)
calculate_total_revenue = data_frame_3['qty']*data_frame_3['pricePerUnit']
print(calculate_total_revenue)

data_frame_3['totalRevenue'] = calculate_total_revenue
print(data_frame_3)

# Answer 2
best_sale = data_frame_3[data_frame_3['totalRevenue'] == max(data_frame_3['totalRevenue'])]
print(best_sale)
#    orderId      product     category  qty  pricePerUnit region  totalRevenue
# 1      102  smart phone  electronics    5           800  south          4000
