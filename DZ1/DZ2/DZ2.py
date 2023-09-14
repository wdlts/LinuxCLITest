import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # Test1
    assert checkout("cd /home/user/test; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # Test2
    assert checkout("cd /home/user/out; 7z e arx2.7z -o/home/wdlts/folder1 -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    # Test3
    assert checkout("cd /home/user/out; 7z e arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # Test4
    assert checkout("cd /home/user/out; 7z l arx2.7z", "Name\n----"), "test4 FAIL"


def test_step5():
    # Test5
    assert checkout("cd /home/user/out; 7z x arx2.7z -o/home/wdlts/folderx -y", "Everything is Ok"), "test5 FAIL"
