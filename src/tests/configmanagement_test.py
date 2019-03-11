import pytest
from .context import pipelines
from pipelines.utils import configmanagement as cm

class Test_configmanagement(object):
    def test_getMockSecret_validSecret(self):
        secret = cm.getMockSecret("UnitTests","Test2")
        assert secret == "Value2"

    def test_getMockSecret_invalidSecret(self):
        with pytest.raises(KeyError):
            assert cm.getMockSecret("UnitTests","Test3") == "Value2"

    def test_getMockSecret_invalidScope(self):
        with pytest.raises(IndexError):
            assert cm.getMockSecret("UnitTestsXX","Test3") == "Value2"
