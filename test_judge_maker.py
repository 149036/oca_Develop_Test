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

    result = make_judge("D", [29, 29, 29, 100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no3():
    """マトリックスNo3
    30点以下の回数0~2
    成績A~C
    """

    result = make_judge("A", [100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1

    result = make_judge("B", [100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1

    result = make_judge("C", [100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1


def test_make_judge_no4():
    """マトリックスNo4
    30点以下の回数0~2
    成績D
    """

    result = make_judge("D", [100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2


def test_make_judge_no5():
    """マトリックスNo5
    30点以下の回数0~2
    成績E
    """

    result = make_judge("E", [100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3
