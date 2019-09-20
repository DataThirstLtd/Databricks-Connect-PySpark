import pytest
from .context import pipelines
from pipelines.utils import configmanagement as cm

class Test_configmanagement(object):
    def test_isLocal(self):
        assert cm.isLocal() == True

   