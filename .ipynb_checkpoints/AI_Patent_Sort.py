file = open("C:/Users/dudwo/Documents/Lecture/AI_PatentNum_IPC.csv",'r',encoding='utf8')
write = open("C:/Users/dudwo/Documents/Lecture/AI_PatentNum_IPC_Sort.csv",'a',encoding='utf8')
lines = file.readlines()
new = []
for line in lines:
    line.strip('\n')
    Pat_Num = line[0:6]
    IPC = line[8:-1]
    sort = [Pat_Num,IPC]
    if sort[0] not in new:
        write.writelines('\n')
        new.append(sort[0])
        print(sort[0])
        write.writelines(sort[0]+' ')
        new.append(sort[1])
        write.write(sort[1]+' ')
    elif sort[0] in new and sort[1] not in new:
        new.append(sort[1])
        write.write(sort[1]+' ')
print("Done!")
write.close()