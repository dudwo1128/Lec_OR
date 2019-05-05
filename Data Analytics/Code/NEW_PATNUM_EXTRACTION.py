with open("C:/Users/dudwo/Desktop/19년 1학기/DA/개인과제/데이터/AI_IPC.csv", "r") as IPC:
    ilines = IPC.readlines()
    PAT = open("C:/Users/dudwo/Desktop/19년 1학기/DA/개인과제/데이터/전체_IPC_PATNUM.csv", "r")
    plines = PAT.readlines()
    w = open("C:/Users/dudwo/Desktop/19년 1학기/DA/개인과제/데이터/NEWAI_IPC_PATNUM.csv", "a")
    for iline in ilines:
        for pline in plines:
            if iline[0:11] == pline[0:11]:
                # print("YES")
                print(pline)
                w.writelines(pline)
    w.close
    PAT.close
