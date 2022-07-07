from datetime import datetime, timedelta



d1 = datetime.strptime('20/04/1987 20:20:00', '%d/%m/%Y %H:%M:%S' )
d2 = datetime.strptime('25/04/1987 20:21:00', '%d/%m/%Y %H:%M:%S' )

print(d1.time())
dif = d2 - d1

print(dif.seconds)



# data = data + timedelta(days=8000, seconds=6000)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

# data = datetime.strptime('20/04/2019', '%d/%m/%Y')
# print(data)
# data = datetime(2019,4,20,10,53,20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))