import configmanagement
import pytest

class configmanagement_tests:

    def getMockSecret_validSecret_Test():
        secret = configmanagement.getMockSecret("UnitTests","Test2")
        assert secret == "Value2"

    def getMockSecret_invalidSecret_Test():
        with pytest.raises(KeyError):
            assert configmanagement.getMockSecret("UnitTests","Test3") == "Value2"

    def getMockSecret_invalidScope_Test():
        with pytest.raises(IndexError):
            assert configmanagement.getMockSecret("UnitTestsXX","Test3") == "Value2"

   