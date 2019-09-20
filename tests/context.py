# This file just sets the context for the test. Each test file calls this
# so that they do not all individually have to mnodify path

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pipelines