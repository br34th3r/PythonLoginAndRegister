import sys
from setuptools import find_packages, setup
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))

def get_long_description() -> str:
      return (
            (CURRENT_DIR / "README.md").read_text(encoding="utf8")
      )

setup(name='PythonLoginAndRegister',
      version='0.1',
      description='Basic Login and Registration in Python',
      long_description=get_long_description(),
      url='https://github.com/coolhobo77/Python-Login-And-Register',
      author='coolhobo77',
      author_email='joshuaboddy1@gmail.com',
      license='MIT',
      packages=['PythonLoginAndRegister'],
      package_dir={"PythonLoginAndRegister": "src"},
      zip_safe=False)
