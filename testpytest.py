def f(name):
    print("hello {}".format(name))


def test_f(capfd):
    f("Tom")

    out, err = capfd.readouterr()
    assert out == "hello Tom\n"
