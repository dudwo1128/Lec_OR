c = open("AI_PatentNum_IPC.csv","r",encoding='utf8')
w = open("AI_PatentNum_IPC_Sort2.csv","a",encoding='utf8')
clines = c.readlines()
pat_ipc = []
for line in clines:
    list = []
    pat = line[0:7]
    ipc = line[8:-1]
    if pat not in pat_ipc:
        pat_ipc.append(pat)
        pat_ipc.append(ipc)
        w.write('\n')
        w.writelines(pat)
        w.write(',')
        w.writelines(ipc)
        w.write(',')
        print(pat)
    elif pat in pat_ipc:
        pat_ipc.append(ipc)
        w.writelines(ipc)
        w.write(',')
c.close()
w.close()
