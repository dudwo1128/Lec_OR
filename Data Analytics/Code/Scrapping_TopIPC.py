import pymysql

con = pymysql.connect(host=' ', user = ' ',password = ' ', db = ' ')

curs = con.cursor(pymysql.cursors.DictCursor)

file = open("IPC개수_10개이상.csv",'r',encoding='utf8')
lines = file.readlines()
for line in lines:
    write = open("IPC개수_10개이상_sort.csv",'a')
    sql = "select * FROM tp_class_da2019.ipc where 특허등록번호 = %s" %(line.strip('\ufeff'))
    curs.execute(sql)

    result = curs.fetchall()
    for row_data in result:
        PatentNum_IPC = [row_data['특허등록번호'],row_data['보유IPC전체코드']]
        print(PatentNum_IPC)
        write.writelines(PatentNum_IPC[0])
        write.writelines(',')
        write.writelines(PatentNum_IPC[1])
        write.writelines('\n')
    write.close()
file.close()
