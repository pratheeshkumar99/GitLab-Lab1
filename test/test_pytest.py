from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2
    assert calculator.fun1(2.5, 3.5) == 6.0


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0
    assert calculator.fun2(10, 3) == 7


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1
    assert calculator.fun3(2.5, 4) == 10.0


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98
    assert calculator.fun4(1, 2, 3) == 6


def test_fun5():
    assert calculator.fun5(10, 2) == 5.0
    assert calculator.fun5(15, 3) == 5.0
    assert calculator.fun5(-10, 2) == -5.0
    assert calculator.fun5(7, 2) == 3.5
    assert calculator.fun5(0, 5) == 0.0


def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 2) == 25
    assert calculator.fun6(2, 0) == 1
    assert calculator.fun6(4, -1) == 0.25
    assert calculator.fun6(9, 0.5) == 3.0


def test_fun7():
    assert calculator.fun7(0) == 1
    assert calculator.fun7(1) == 1
    assert calculator.fun7(3) == 6
    assert calculator.fun7(4) == 24
    assert calculator.fun7(5) == 120


def test_fun8():
    result1 = calculator.fun8([1, 2, 3, 4, 5])
    assert result1["mean"] == 3.0
    assert result1["median"] == 3.0
    assert result1["count"] == 5

    result2 = calculator.fun8([1, 2, 3, 4])
    assert result2["median"] == 2.5

    result3 = calculator.fun8([1, 2, 2, 3])
    assert result3["mode"] == 2


def test_fun9():
    assert calculator.fun9(1) == [0]
    assert calculator.fun9(2) == [0, 1]
    assert calculator.fun9(5) == [0, 1, 1, 2, 3]
    assert calculator.fun9(7) == [0, 1, 1, 2, 3, 5, 8]
    assert calculator.fun9(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fun10():
    assert calculator.fun10([1, 2], 3) == 7  # 1 + 2*3
    assert calculator.fun10([1, 2, 1], 2) == 9  # 1 + 2*2 + 1*4
    assert calculator.fun10([5], 10) == 5  # constant
    assert calculator.fun10([3, 2, 1], 0) == 3  # at x=0
    assert calculator.fun10([1, 1, 1], 1) == 3  # 1 + 1 + 1


def test_fun11():
    roots1 = calculator.fun11(1, -5, 6)
    assert len(roots1) == 2
    assert 2.0 in roots1 and 3.0 in roots1

    roots2 = calculator.fun11(1, -4, 4)
    assert len(roots2) == 1
    assert roots2[0] == 2.0

    roots3 = calculator.fun11(1, 0, 1)
    assert roots3 is None


def test_fun12():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    result = calculator.fun12(mat1, mat2)
    assert result == [[19, 22], [43, 50]]

    identity = [[1, 0], [0, 1]]
    result2 = calculator.fun12(mat1, identity)
    assert result2 == [[1, 2], [3, 4]]

    mat3 = [[1, 2, 3]]
    mat4 = [[4], [5], [6]]
    result3 = calculator.fun12(mat3, mat4)
    assert result3 == [[32]]
