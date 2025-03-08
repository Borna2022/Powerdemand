import pandas as pd
import numpy as np
from scipy.integrate import simps

# خواندن دیتا از فایل اکسل
data = pd.read_excel('C:/Users/smc-developer/Desktop/Powerdemand_Optimization/new_data.xlsx')

# تبدیل ستون‌های Time و Power به عدد
data['Time'] = pd.to_numeric(data['Time'], errors='coerce')
data['Power'] = pd.to_numeric(data['Power'], errors='coerce')

# حذف ردیف‌هایی که مقادیر نامعتبر دارند
data.dropna(subset=['Time', 'Power'], inplace=True)

# تابع برای محاسبه انتگرال هر گروه
def calculate_integral(group_data):
    if len(group_data) < 2:
        return np.nan  # اگر گروه فقط یک نقطه داده داشته باشد، انتگرال را محاسبه نمی‌کنیم
    integral = simps(group_data['Power'], group_data['Time'])
    return integral

# محاسبه انتگرال هر گروه و ذخیره در یک دیکشنری
integrals = {}
for group in data['Group'].unique():
    group_data = data[data['Group'] == group]
    integrals[group] = calculate_integral(group_data)

# ذخیره کردن انتگرال هر گروه در فایل جدید
with open('C:/Users/smc-developer/Desktop/Powerdemand_Optimization/integrals.txt', 'w') as f:
    for group, integral in integrals.items():
        f.write(f"Group {group}: Integral = {integral}\n")

# نمایش انتگرال هر گروه در ترمینال
for group, integral in integrals.items():
    print(f"Group {group}: Integral = {integral}")

# ذخیره کردن دیتا با گروه‌ها در فایل جدید اکسل
data.to_excel('C:/Users/smc-developer/Desktop/Powerdemand_Optimization/new_data_with_integrals.xlsx', index=False)
