A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

score = float(input("enter the test score: "))

if score >= A_SCORE:
    print("your grade is A.")
else:
    if score >= B_SCORE:
        print("your grade is B.")
    else:
        if score >= C_SCORE:
            print("your grade is C.")
        else:
            if score >= D_SCORE:
                print("your grade is D.")
            else:
                print("your grade is F.")
