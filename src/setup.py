from setuptools import setup

setup(name='pipelines',
      version='0.0.1',
      description='Sample PySpark Application for use with Databricks Connect',
      url='http://github.com/dataThirstLtd',
      author='Data Thirst Ltd',
      author_email='hello@datathirst.net',
      packages=['pipelines', 'pipelines.utils', 'pipelines.jobs'],
      zip_safe=False)
