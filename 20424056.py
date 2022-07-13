# MSSV: 20424056 - Nguyễn Thế Ngọc

# nguồn tham khảo: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/

# tham khảo 2: https://towardsdatascience.com/z-score-for-anomaly-detection-d98b0006f510

# ví dụ demo: điểm 

import numpy as np
import random

data_with_day = {}

# tạo dữ liệu
for i in range(1, 366, 1): # 1 tới 365
    # tổng doanh thu của ngày đó
    revenue_of_the_day = random.randrange(400, 600, 20)

    # những ngày cách halloween khoảng 1 tháng
    if i > 280 and i < 302:
        revenue_of_the_day = random.randrange(1000, 2000, 20)
    if i > 304 and i < 320:
        revenue_of_the_day = random.randrange(1200, 2200, 20)

    data_with_day[i] = revenue_of_the_day

# những ngày gần và ngày halloween thì tổng bán được sẽ tăng đột biến vì nhu cầu
data_with_day[302] = 4850
data_with_day[303] = 5000
data_with_day[304] = 4920

data = list(data_with_day.values())

# trung tâm
mean = np.mean(data)
# độ lệch chuẩn
std = np.std(data)

# thường threshold sẽ là 2, 2.5, 3, hoặc 3.5
threshold = 2.5

# lưu các con số doanh thu bất thường
outlier = []

for item in data:
    z = (item-mean)/std
    if abs(z) > threshold:
        outlier.append(item)
print('Các con số doanh thu bất thường:', outlier)

# những ngày doanh thu bất thường
day_outlier = {}

for item in outlier:
    for day, revenue in data_with_day.items():
        if revenue == item:
            day_outlier[day] = revenue
            break

print('Các ngày có doanh thu bất thường trong năm:')
for key in day_outlier:
    print("ngày " + str(key) + ", doanh thu: " + str(day_outlier[key]))