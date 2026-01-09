from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.NetworkSecurityException import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
import sys
import os
 


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Data Ingestion started")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)


    except Exception as e:
        raise NetworkSecurityException(error_message=str(e), error_details=sys)