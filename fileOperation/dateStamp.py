import datetime
date_stamp = str(datetime.datetime.now()).split('.')[0]
print(date_stamp)
date_stamp=date_stamp.replace(" ","_").replace("-","_").replace(":","_")
print(date_stamp)
date_stamp=date_stamp+".png"
print(date_stamp)