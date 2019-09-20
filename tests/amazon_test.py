import pytest
from .context import pipelines
from pipelines.jobs import amazon
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

class Test_amazon(object):
    def mock_extract():
        data = [("A1","B1"), ("A2","B2")]
        return spark.createDataFrame(data, ["col1", "col2"])

    def test_transform_Amazon_newColumn(self):
        df = Test_amazon.mock_extract()
        df = amazon.transform_Amazon(df)
        assert "meta_timestamp" in df.columns
