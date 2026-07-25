import os
import sys

PROJECT_HOME = "/home/enginyasmun/LearningPortal"
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

os.environ.setdefault("SECRET_KEY", "REPLACE_WITH_A_LONG_RANDOM_SECRET")

from app import app as application
