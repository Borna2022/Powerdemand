import pandas as pd

# خواندن دیتا از فایل
data = pd.read_csv('C:/Users/smc-developer/Desktop/Powerdemand_Optimization/PDW.txt', delimiter='\t', header=None, names=['Time', 'Power'])

# تبدیل ستون Power به عدد
data['Power'] = pd.to_numeric(data['Power'], errors='coerce')

# تعریف متغیر برای ذخیره کانتر گروه‌ها
group_counter = 0
group_list = []
previous_value = None

# افزودن کانتر به هر رکورد
for power in data['Power']:
    if power != 0 and (previous_value == 0 or previous_value is None):
        group_counter += 1
    group_list.append(group_counter)
    previous_value = power

# افزودن ستون Group به دیتا
data['Group'] = group_list

# ذخیره کردن دیتا در فایل جدید اکسل
data.to_excel('C:/Users/smc-developer/Desktop/Powerdemand_Optimization/new_data.xlsx', index=False)
