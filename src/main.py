
# This script is executed in our Python Job (or Azure Data Factory Python Task)
# It can accept parameters
from pyspark.sql import SparkSession
import argparse
from importlib import import_module
from inspect import signature
import os
import sys

spark = SparkSession.builder.getOrCreate()

# Also adding the modules hint so that we can execute this script locally
try:
    dirname = os.path.dirname(__file__)
    sys.path.insert(0, (os.path.join(dirname, 'pipelines')))
except:
    print('nothing')

# Define the parameters for our job
parser = argparse.ArgumentParser()

parser.add_argument("etl", type=str, nargs='?', default="pipelines.jobs.amazon")
namespace, extra = parser.parse_known_args()
for arg in vars(namespace):
    etl = getattr(namespace, arg)

#import module based on first parameter passed in
mod = import_module(etl, "pipelines")
met = getattr(mod, "etl")

# Get the parameters (if any) for the ETL
p = signature(met)
for a, b in p.parameters.items():
    parser.add_argument(b.name, type=str, nargs='?')

args = parser.parse_args()

# Loop through the arguements and pass to ETL (try casting to int)
l = []
for arg in vars(args):
    print(arg, getattr(args, arg))
    if arg != "etl":
        try:
            l.append(int(getattr(args, arg)))
        except:
            l.append(getattr(args, arg))

# Execute ETL
met(*l)
