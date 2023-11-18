def make_judge(grade="D", points=[10, 15, 20, 30, 40, 50, 60, 70, 80, 100]):
    a = [x for x in points if x < 10]
    b = [x for x in points if x <= 30]

    if len(a) > 0:
        judge = 3
    elif len(b) >= 3:
        judge = 2
    else:
        judge = 1

    if "A" == grade or "B" == grade or "C" == grade:
        judge = 1
    elif "D" == grade:
        judge = 2
    elif "E" == grade:
        judge = 3

    return judge
