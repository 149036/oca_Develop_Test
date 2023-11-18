def make_judge(grade="D", points=[10, 15, 20, 30, 40, 50, 60, 70, 80, 100]):
    abcde = ["A", "B", "C", "D", "E"]
    if grade not in abcde:
        raise Exception("gradeにA~E以外の文字が入力されています")

    if len(points) != 10:
        raise Exception("pointsの要素数が10ではありません")

    tmp1 = [x for x in points if not isinstance(x, int)]
    if 0 < len(tmp1):
        raise Exception("pointsに整数以外が含まれています")

    tmp2 = [x for x in points if x > 100]
    if 0 < len(tmp2):
        raise Exception("pointsに101以上の数値が含まれています")

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
