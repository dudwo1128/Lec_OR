import pymysql

con = pymysql.connect(host='103.218.161.81', user = 'class_da2019',password = 'engineering403', db = 'tp_class_da2019')

curs = con.cursor(pymysql.cursors.DictCursor)

file = open("C:/Users/dudwo/Desktop/Practice.csv",'rt',encoding='utf8')
lines = file.readlines()
for line in lines:
    write = open("C:/Users/dudwo/Desktop/출원인_특허_초록.csv",'a',encoding='utf-8')

    sql = "select A.출원인소속, A.특허등록번호, B.특허초록텍스트 FROM tp_class_da2019.assignee as A left join tp_class_da2019.abstract as B  on B.특허등록번호 = A.특허등록번호  where A.특허등록번호 = %s" %(line.strip('\ufeff'))

    curs.execute(sql)

    result = curs.fetchall()
    for row_data in result:
        PatentNum_IPC = [row_data['출원인소속'].strip('\r'),row_data['특허초록텍스트']]
        write.writelines(str(PatentNum_IPC))
        write.writelines('\n')

        print(row_data['특허등록번호'])
    write.close()
file.close()