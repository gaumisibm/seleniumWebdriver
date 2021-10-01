def getDate(d, m):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = ['January', 'February',
             'March', 'April',
             'May', 'June',
             'July', 'August',
             'September', 'October',
             'November', 'December']
    cnt = 183
    cur_month = month.index(m)
    cur_date = d
    while (1):
        while (cnt > 0 and cur_date <= days[cur_month]):
            cnt -= 1
            cur_date += 1
        if (cnt == 0):
            break
        cur_month = (cur_month + 1) % 12
        cur_date = 1

    return (cur_date, month[cur_month])


D = int(input())
M = input()

cur_date, month = getDate(D, M)
print("{} {} -> Date 183 days after his purchase".format(cur_date, month))
