import ConfigParser
import os
from webdriver import init_env

init_env()
print os.environ['FOO']
