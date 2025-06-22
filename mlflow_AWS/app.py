import os
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
from mlflow.models.signature import infer_signature
import mlflow.sklearn

import logging

os.environ["MLFLOW_TRACKING_URI"]="http://ec2-13-203-223-225.ap-south-1.compute.amazonaws.com:5000/"

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

def eval_metrics(actual,pred):
    rmse = np.sqrt(mean_squared_error(actual,pred))
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse,mae,r2

if __name__ == "__main__":

    ## data ingestion-Read the data from the csv file-wine quality dataset
    csv_url = "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
    try:
        data=pd.read_csv(csv_url,sep=";")
    except Exception as e:
        logger.exception("unable to download the dataset")

    ## split the data into training and test sets
    train,test=train_test_split(data)

    ## set the target variable to predict
    train_x=train.drop("quality",axis=1)
    test_x=test.drop("quality",axis=1)
    train_y=train["quality"]
    test_y=test["quality"]

    alpha=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
    l1_ratio=float(sys.argv[2]) if len(sys.argv)>2 else 0.5

    with mlflow.start_run():
        lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=42)
        lr.fit(train_x,train_y)

        predicted_qualities=lr.predict(test_x)
        rmse,mae,r2=eval_metrics(test_y,predicted_qualities)

        print(f"Elasticnet model (alpha={alpha},l1_ratio={l1_ratio}):")
        print(f"RMSE: {rmse}")
        print(f"MAE: {mae}")
        print(f"R2: {r2}")

        mlflow.log_param("alpha",alpha)
        mlflow.log_param("l1_ratio",l1_ratio)

        mlflow.log_metric("rmse",rmse)
        mlflow.log_metric("mae",mae)
        mlflow.log_metric("r2",r2)

        ## for the remote server we need to use the following code

        remote_server_uri="http://ec2-13-203-223-225.ap-south-1.compute.amazonaws.com:5000/"
        mlflow.set_tracking_uri(remote_server_uri)

        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(lr,"model",registered_model_name="ElasticnetWineModel")
        else:
            mlflow.sklearn.log_model(lr,"model")
            