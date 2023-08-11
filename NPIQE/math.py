# import matplotlib.pyplot as plt
# import random
# plt.title('Belarus')
# x = range(60)
# y1 = [random.uniform(35, 40) for i in x]  # uniform提供[35, 40)随机值
# y2 = [random.uniform(25, 30) for j in x]
#
# x = [2010, 2011, 2012, 2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]
# y = [2, 2, 3, 3,3,2,2,3,4,5,2,2,3,2,2,1,2,3,2,2,2,3,4]
# x1 = [2010, 2011, 2012, 2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
# y1 = [2, 2, 3,2,3,3,2,3,3,4,5,2,2]
# plt.plot(x, y, 'ro--',label='Predicted value')
# plt.plot(x1, y1, 'b',label='True value')
# plt.xlabel('Time')
# plt.ylabel('Social security level')
# plt.legend()  # 右上角显示各个曲线代表什么意思
# plt.show()

import matplotlib.pyplot as plt
import random
plt.title('Ukraine')
x = range(60)
y1 = [random.uniform(35, 40) for i in x]  # uniform提供[35, 40)随机值
y2 = [random.uniform(25, 30) for j in x]

x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010, 2011, 2012, 2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032]
y = [3,3,4,5,5,4,3,2,3,3,3, 2, 3, 3,3,2,2,3,4,5,4,5,4,4,4,3,2,3,2,2,2,3,4]
x1 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010, 2011, 2012, 2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
y1 = [3,3,4,5,5,4,3,2,3,2,3, 2, 3,2,3,3,2,3,3,4,5,4,5]
plt.plot(x, y, 'ro--',label='Predicted value')
plt.plot(x1, y1, 'b',label='True value')
plt.xlabel('Time')
plt.ylabel('Social security level')
plt.legend()  # 右上角显示各个曲线代表什么意思
plt.show()