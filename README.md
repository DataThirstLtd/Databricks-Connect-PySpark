[![Build Status](https://dev.azure.com/datathirst/Public-Demos/_apis/build/status/DataThirstLtd.Databricks-Connect-PySpark?branchName=master)](https://dev.azure.com/datathirst/Public-Demos/_build/latest?definitionId=37&branchName=master)

# Developing with Databricks-Connect & Azure DevOps
A guide of how to build good Data Pipelines with Databricks Connect using best practices.
Details: https://datathirst.net/blog/2019/9/20/series-developing-a-pyspark-application

## About
This is a sample Databricks-Connect PySpark application that is designed as a template for best practice and useability.

The project is designed for:
* Python local development in an IDE (VSCode) using Databricks-Connect
* Well structured PySpark application 
* Simple data pipelines with reusable code
* Unit Testing with Pytest
* Build into a Python Wheel
* CI Build with Test results published
* Automated deployments/promotions

## Setup

Create a Conda Environment (open Conda prompt):
```
conda create --name dbconnectappdemo python=3.5
```

Activate the environment:
```
conda activate dbconnectappdemo
```

IMPORTANT: Open the requirements.txt in the root folder and ensure the version of databrick-connect matches your cluster runtime.

Install the requirements into your environments:
```
pip install -r requirements.txt
```

If you need to setup databricks-connect then run:
```
databricks-connect configure
```
More help [here](https://datathirst.net/blog/2019/4/20/setup-databricks-connect-on-windows) & [here](https://datathirst.net/blog/2019/3/7/databricks-connect-finally)

## Setup Deployment
If you would like to deploy from your local PC to Databricks create a file in the root called MyBearerToken.txt and paste in a bearer token from the Databricks UI.


Copyright Data Thirst Ltd (2019)
