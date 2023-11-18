from judge_maker import make_judge


def test_make_judge_no1():
    """マトリックスNo1
    10点より下の点数がある場合
    """

    result = make_judge("E", [9, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3


def test_make_judge_no2():
    """マトリックスNo2
    30点以下の回数3回以上
    """

    result = make_judge("D", [29, 29, 30, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no3():
    """マトリックスNo3
    30点以下の回数0~2
    成績A~C
    """

    result = make_judge("A", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1

    result = make_judge("B", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1

    result = make_judge("C", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1


def test_make_judge_no4():
    """マトリックスNo4
    30点以下の回数0~2
    成績D
    """

    result = make_judge("D", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no5():
    """マトリックスNo5
    30点以下の回数0~2
    成績E
    """

    result = make_judge("E", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3


def test_make_judge_exception_no1():
    try:
        grade = "F"
        points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        make_judge(grade, points)
    except Exception as e:
        assert e.args[0] == "gradeにA~E以外の文字が入力されています"


def test_make_judge_exception_no2():
    try:
        grade = "A"
        points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 100, 100, 100, 100]
        make_judge(grade, points)
    except Exception as e:
        assert e.args[0] == "pointsの要素数が10ではありません"


def test_make_judge_exception_no3():
    try:
        grade = "A"
        points = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        make_judge(grade, points)
    except Exception as e:
        assert e.args[0] == "pointsに整数以外が含まれています"


def test_make_judge_exception_no4():
    try:
        grade = "A"
        points = [10001, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        make_judge(grade, points)
    except Exception as e:
        assert e.args[0] == "pointsに101以上の数値が含まれています"
