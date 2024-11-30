import sys

def test_myoutput(capsys):
    print("hello")
    sys.stderr.write("world\n")

    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"

    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

def test_disabling_capturing(capsys):
    print("this output is captured")
    print("this output is captured 2")
    with capsys.disabled():
        print("output not captured, going directly to sys.stdout1")
        print("output not captured, going directly to sys.stdout2")
        print("output not captured, going directly to sys.stdout3")

    print("this output is also captured")

    assert False
