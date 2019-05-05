import pymysql

con = pymysql.connect(host=' ', user = ' ',password = ' ', db = ' ')

curs = con.cursor(pymysql.cursors.DictCursor)

file = open("C:/Users/dudwo/Desktop/Practice.csv",'rt',encoding='utf8')
lines = file.readlines()
for line in lines:
    write = open("C:/Users/dudwo/Desktop/Practice_Abstract.csv",'a',encoding='utf-8')
    sql = "select * FROM tp_class_da2019.abstract where 특허등록번호 = %s" %(line.strip('\ufeff'))
    curs.execute(sql)

    result = curs.fetchall()
    for row_data in result:
        PatentNum_IPC = [row_data['특허등록번호'],row_data['특허초록텍스트']]
        #print(row_data)
        print(PatentNum_IPC)
        write.writelines(PatentNum_IPC[0])
        write.writelines(',')
        write.writelines(PatentNum_IPC[1])
        write.writelines('\n')
    write.close()
file.close()