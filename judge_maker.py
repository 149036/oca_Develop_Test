def make_judge(grade="A", points=[10, 15, 20, 30, 40, 50, 60, 70, 80, 100]):
    if grade == "A" or grade == "B" or grade == "C":
        judge = 1
    elif grade == "D":
        judge = 2
    elif grade == "E":
        judge = 3

    count = 0
    for i in points:
        if i < 10:
            judge = 3
            break
        elif i <= 30:
            count += 1

    if count >= 3:
        judge = 2

    return judge


print(make_judge())
