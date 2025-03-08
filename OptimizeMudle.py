import numpy as np
from scipy.optimize import minimize

# پارامترها
num_furnaces = 8
total_time = 1440
Pmax = 450
P = 110

# زمان سیکل کاری
start_time_min = 70
start_time_max = 90
stop_time_min = 10
stop_time_max = 15
start_time = (start_time_min + start_time_max) / 2
stop_time = (stop_time_min + stop_time_max) / 2
cycle_time = start_time + stop_time

# تابع هدف
def objective(vars):
    return -np.sum(vars)

# قیود
def constraint1(vars):
    return Pmax - np.sum(vars)

# تعریف حدود متغیرها (0 تا توان اختصاصی هر کوره)
bounds = [(0, P) for _ in range(num_furnaces)]

# مقدار اولیه
x0 = [P/2 for _ in range(num_furnaces)]

# قیود مسئله
con1 = {'type': 'ineq', 'fun': constraint1}
constraints = [con1]

# حل مسئله
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x = solution.x

# نمایش نتایج
print("توان تخصیصی به هر کوره:")
for i in range(num_furnaces):
    print(f"کوره {i+1}: {x[i]} مگاوات")

print("مجموع توان مصرفی:", np.sum(x))
