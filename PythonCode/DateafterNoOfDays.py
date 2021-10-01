def calDate(d,m,y,c):
    cnt = c
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    month = ['January', 'February','March', 'April','May', 'June','July', 'August','September', 'October',
             'November', 'December']
    year=y
    curr_date = d
    curr_month = month.index(m)
    while(1):
        while (cnt > 0 and curr_date < days[curr_month]):
            cnt -= 1
            curr_date += 1
        if cnt == 0:
            break
        print(curr_month)
        # if((curr_month+1) % 12 == 0):
        #     year +=1
        curr_month = (curr_month + 1) % 12
        if curr_month == 0:
            year +=1
        curr_date = 1

    return [curr_date,month[curr_month],year]


dd = int(input())
month = input()
year = int(input())
cnt = int(input())
l1 = calDate(dd,month,year,cnt)
print(l1)