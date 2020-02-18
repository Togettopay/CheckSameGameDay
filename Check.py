#创建周一到周五的课表，0表示在上课，1表示在寝室
LYcoureses=[[1,1,0,0,0],\
           [1,0,0,0,0],\
           [0,0,1,1,1],\
           [1,0,1,0,1],\
           [1,1,0,0,1]]

JDcourses=[[1,1,1,0,0],\
           [1,1,0,0,0],\
           [1,1,1,1,1],\
           [1,1,0,0,0],\
           [1,1,0,0,1]]

WLcourses=[[1,0,1,0,0],\
           [0,1,1,0,0],\
           [1,0,1,1,1],\
           [1,0,1,1,1],\
           [1,1,1,1,1]]

#查询时段(day_time表示一天中的某个时间，day表示星期几，number表示查重（1）还是查不同（0）)
def CheckWhen(day_time,day,number):
    if number==1:
        s=""
        if day_time==1:
            s = "星期{}上午一二节都没课".format(day)
        elif day_time==2:
            s = "星期{}上午三四节都没课".format(day)
        elif day_time==3:
            s = "星期{}下午五六节都没课".format(day)
        elif day_time==4:
            s = "星期{}下午七八节都没课".format(day)
        else:
            s = "星期{}晚上都没课".format(day)
        if s=="":
            s="没有能一起游戏的时间"
    else:
        s = ""
        if day_time == 1:
            s = "星期{}上午一二节就他没课".format(day)
        elif day_time == 2:
            s = "星期{}上午三四节就他没课".format(day)
        elif day_time == 3:
            s = "星期{}下午五六节就他没课".format(day)
        elif day_time == 4:
            s = "星期{}下午七八节就他没课".format(day)
        else:
            s = "星期{}晚上就他没课".format(day)
        if s=="":
            s="他没课课的时候有人也没课"
    return s

#查询一天并输入
def CheckADay(day):
    for i in range(5):
        if LYcoureses[day][i]==1 and JDcourses[day][i]==1 and WLcourses[day][i]==1:
            print(CheckWhen(i+1,day+1,1))

#查询一星期
def CheckSameGameDay():
    for i in range(5):
        CheckADay(i)

#查询不同（1表示LY,2表示JD,3表示WL，查询的内容为该成员不在上课，其他成员在上课）
def CheckDifferent(DormMember):
    if DormMember==1:
        for i in range(5):
            for n in range(5):
                if LYcoureses[i][n] == 1 and JDcourses[i][n] == 0 and WLcourses[i][n] == 0:
                    print(CheckWhen(n + 1, i + 1,0))
    elif DormMember==2:
        for i in range(5):
            for n in range(5):
                if LYcoureses[i][n] == 0 and JDcourses[i][n] == 1 and WLcourses[i][n] == 0:
                    print(CheckWhen(n + 1, i + 1,0))
    else:
        for i in range(5):
            for n in range(5):
                if LYcoureses[i][n] == 0 and JDcourses[i][n] == 0 and WLcourses[i][n] == 1:
                    print(CheckWhen(n + 1, i + 1,0))

def judgeMEM():
    a = eval(input("请输入您想要进行的判断\n"))
    if a == 1:
        CheckSameGameDay()
    if a == 2:
        s = eval(input("请问您想要查询哪个成员(1为LY，2为JD，3为WL)\n"))
        CheckDifferent(s)

def main():
    print("本程序用于对课程查重或不同的判断,输入1为查询什么时候都没课，输入2查询什么时候单个成员没课")
    judgeMEM()

if __name__ == '__main__':
    main()