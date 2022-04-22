import pytest


@pytest.mark.set1
def test_file1_method1 ():
	x = 5
	y = 6
	assert x + 1 == y, "kiểm tra không thành công"
	assert x == y, "kiểm tra không thành công"
def test_file1_method2 ():
	x = 5
	y = 6
	assert x + 1 == y, "kiểm tra không thành công"