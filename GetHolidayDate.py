import datetime

def __append_to_file__(file, content):
  file.write(content + '\n')


# 2021年数据
special = {'2021-01-01': 1, '2021-01-02': 1, '2021-01-03': 1,
'2021-02-11': 1,'2021-02-12': 1,'2021-02-13': 1,'2021-02-14': 1,'2021-02-15': 1,'2021-02-16': 1,'2021-02-17': 1,
'2021-02-07': 0, '2021-02-20': 0,
'2021-04-03': 1,'2021-04-04': 1,'2021-04-05': 1,
'2021-05-01': 1,'2021-05-02': 1,'2021-05-03': 1,'2021-05-04': 1,'2021-05-05': 1,
'2021-04-25': 0,'2021-05-08': 0,
'2021-06-12': 1,'2021-06-13': 1,'2021-06-14': 1,
'2021-09-18': 0,'2021-09-19': 1,'2021-09-20': 1,'2021-09-21': 1,
'2021-10-01': 1,'2021-10-02': 1,'2021-10-03': 1,'2021-10-04': 1,'2021-10-05': 1,'2021-10-06': 1,'2021-10-07': 1,
'2021-09-26': 0,'2021-10-09': 0
}
# 每年的天数
daysOfYear = 365
# 指定年的第一天
start = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
file = open('HolidayData.sql', 'a+')
for i in range(0, daysOfYear):
  delta = datetime.timedelta(days=i)
  newDate = start + delta
  isHoliday = 0
  week = newDate.weekday()
  if week == 5 or week == 6:
    isHoliday = 1
  dateStr = newDate.strftime('%Y-%m-%d')
  if dateStr in special.keys():
    isHoliday = special[dateStr]
  content = "INSERT INTO `hxd_date`(`date`, `flag`) VALUES (\'" + dateStr + "\'," + str(isHoliday) + ");"
  print(content)
  # 需要写入则写入
  __append_to_file__(file, content)
file.close()
