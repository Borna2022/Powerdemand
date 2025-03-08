import numpy as np
import pandas as pd
from scipy.integrate import simps

# خواندن داده‌ها از فایل اکسل
data = pd.read_excel('new_data.xlsx')
data.columns = ['min', 'power', 'group']

# تبدیل ستون‌ها به نوع عددی
data['min'] = pd.to_numeric(data['min'], errors='coerce')
data['power'] = pd.to_numeric(data['power'], errors='coerce')

# حذف ردیف‌های دارای مقدار نامعتبر (NaN)
data.dropna(inplace=True)

# حذف مقادیر صفر از ستون 'power'
data = data[data['power'] != 0]

# محاسبه انتگرال، متوسط و تعداد ردیف‌ها برای هر گروه
grouped_data = data.groupby('group')
integrals = grouped_data.apply(lambda x: simps(x['power'], x['min']))
averages = grouped_data['power'].mean()
counts = grouped_data.size()  # محاسبه تعداد ردیف‌های هر گروه

# ساخت یک DataFrame جدید برای ذخیره نتایج
output_data = pd.DataFrame({
    'group': integrals.index,
    'integral': integrals.values,
    'average': averages.values,
    'count': counts.values
})

# نوشتن DataFrame جدید در یک فایل اکسل جدید
output_data.to_excel('output.xlsx', index=False)

print("نتایج به فایل output.xlsx نوشته شدند.")

# گرد کردن و نمایش انتگرال، متوسط و تعداد ردیف‌های هر گروه
for group, integral in integrals.items():
    avg = averages[group]
    count = counts[group]
    print(f"Group {group}: Count = {count}, Integral = {round(integral, 1)}, Average = {round(avg, 1)}")
