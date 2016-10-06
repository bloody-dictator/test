import pytest
test = {
1: [2, 3],
2: [3, 4],
4: [1]
}
data = {
1: [2, 3],
2: [4]
}

def my_code(data, entry):
    list1 = []
    my_code1(data, entry, list1)

def my_code1(data, entry, list1):
    list1.append(entry)
    print (entry)
    nodes = data.get(entry)
    if nodes is not None:
        for i in nodes:
            if i not in list1:
                my_code1(data, i, list1)


my_code(test,1)

my_code(test,1)
#my_code(data, 1)


def test_my_code(capfd):
    data = {1: [2, 3], 2: [4]}
    my_code(data, 1)
    out, err = capfd.readouterr()
    assert out == "1\n" or out == "1\n2\n" or out == "1\n2\n4\n" or out == "1\n2\n4\n3\n"