from zhixuewang import Zhixuewang
user = input('user:')
password = input('psword:')
zxw = Zhixuewang(user, password)


def get_mark(subject):
    resScore = 0
    subjectName = subject.subjectName
    score = subject.score
    if(subjectName == '语文' or subjectName == '数学' or subjectName == '英语'):
        resScore += score
    if(subjectName == '政治' or subjectName == '历史'):
        if(score >= 85):
            resScore = 10
        elif(score >= 70):
            resScore += 8
        elif(score >= 60):
            resScore += 6
        else:
            resScore += 4
    if(subjectName == '物理'):
        resScore += score*0.9
    if(subjectName == '化学'):
        resScore += score*0.6
    print('科目:', subjectName, '班级最高分:',
          subject.classRank.highScore, '年段最高分', subject.gradeRank.highScore)
    print('成绩:', score)
    print('班级排名:', subject.classRank.rank)
    return resScore


score = zxw.get_mark_with_weight(get_mark)
print('当前综合分为:', score)
# print(list(grades[0]))#['subjectName'])
