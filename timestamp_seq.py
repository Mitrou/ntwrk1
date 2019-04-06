import datetime
import uuid
import json

dt = datetime.datetime(2019, 4, 8, 0, 0, 0)
step = datetime.timedelta(seconds=180)
one_sec = datetime.timedelta(seconds=1)
unique_filename = str('freeze_vid_tst_'+str(uuid.uuid4()))



result = []
# for i in range(11):
#     result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
#     dt += step
#     if i>=1:
#         start_time = result[i-1]
#         end_time = result[i]
#         print(start_time, end_time)
#         print('query1_'+'item_'+str(i)+'_'+unique_filename)

for i in range(100):
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += step
    result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
    dt += one_sec
    start_time = result[i*2]
    end_time = result[i*2+1]
    print(start_time, end_time)
    print('query1_' + 'item_' + str(i+1) + '_' + unique_filename)





print(result)
print(len(result))
print(unique_filename)