import os 
import pytest 

# pytestmark = pytest.mark.usefixtures("cleandir")

class TestDirectoryInit:
    def test_cwd_start_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w", encoding="utf-8") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []