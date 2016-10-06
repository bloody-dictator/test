import pytest


def my_code(x):
    deep = 0
    my_code1(x, deep)


def my_code1(x, deep):
    for key in x.keys():
        print("\t" * deep + key + ":")
        value = x.get(key)
        if isinstance(value, dict):
            deep += 1
            deep = my_code1(value, deep)
            deep -= 1
        else:
            print("\t" + "\t" * deep + x.get(key))
    return deep


obj = {
    'first': 'first_value',
    'second': 'second_value'

}
# my_code(obj)

obj = {
    '1': {
        'child': '1/child/value'
    },
    '2': '1/value'
}
# my_code(obj)


obj = {
    '1': {
        'child': {
            'child2': {
                'child3': {
                    'child4': '1/child/value'
                }
            }
        },
        'child1': 'test'
    },
    '2': '1/value'
}

my_code(obj)

def test_my_code(capfd):
    obj = {
        'first': 'first_value',
        'second': 'second_value'
    }
    my_code(obj)

    out, err = capfd.readouterr()
    assert out == "first:\n\tfirst_value\nsecond:\n\tsecond_value\n"


def test_my_code_2(capfd):
    obj = {
        '1': {
            'child': '1/child/value'
        },
        '2': '1/value'
    }
    my_code(obj)

    out, err = capfd.readouterr()
    assert out == "1:\n\tchild:\n\t\t1/child/value\n2:\n\t1/value\n"


def test_my_code_3(capfd):
    obj = {
        '1': {
            'child': {
                'child2': {
                    'child3': {
                        'child4': '1/child/value'
                    }
                }
            }
        },
        '2': '1/value'
    }
    my_code(obj)

    out, err = capfd.readouterr()
    assert out == "1:\n\tchild:\n\t\tchild2:\n\t\t\tchild3:\n\t\t\t\tchild4:\n\t\t\t\t\t1/child/value\n2:\n\t1/value\n"


def test_my_code_4(capfd):
    obj = {
        '1': {
            'child': {
                'child2': {
                    'child3': {
                        'child4': '1/child/value'
                    }
                }
            },
            'child1': 'test'
        },
        '2': '1/value'
    }
    my_code(obj)

    out, err = capfd.readouterr()
    assert out == "1:\n\tchild:\n\t\tchild2:\n\t\t\tchild3:\n\t\t\t\tchild4:\n\t\t\t\t\t1/child/value\n\tchild1:\n\t\ttest\n2:\n\t1/value\n"
