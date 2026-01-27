A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

科目数 = 0
分数输入状态 = True
总分 = 0
print("分数输入中, 输入(n)停止继续输入.")
while 分数输入状态:
    try:
        score = input(f"输入测试分数 {科目数+1}: ")
        if score != "n":
            score = float(score)
    except:
        print("Error, 重新输入分数, 输入(n)停止继续输入.")
    else:
        if score == "n":
            分数输入状态 = False
        elif (0 <= score) and (score <= 100):
            总分 += score
            科目数 += 1
        else:
            print("重新输入分数, 输入(n)停止继续输入.")


average_score = 总分 / 科目数

print(f"你的平均分数是: {average_score:.2f}")

if average_score >= A_SCORE:
    print("你的成绩是 A.")
elif average_score >= B_SCORE:
    print("你的成绩是 B.")
elif average_score >= C_SCORE:
    print("你的成绩是 C.")
elif average_score >= D_SCORE:
    print("你的成绩是 D.")
else:
    print("你的成绩是 F.")
