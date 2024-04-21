# Devices-Price-Classification-System-using-Python-and-Spring-Boot

A machine learning effort called the Devices Price Classification System makes use of device specs to forecast the price range of various devices. The Python project and the Spring Boot project are the two primary parts of the system.

Python Project: Manages model training, data preparation, and pricing range prediction based on device specs.

Spring Boot Project : can be called for predictions by using the RESTful API provided by the Spring Boot Project to handle incoming queries.

Project Structure

 The project consists of the following key components:

 python_project/: Contains the Python project, including the data preparation, model training, and prediction functions.

 spring_boot_project/: Contains the Spring Boot project, including the main application file, the model class, the controller, and other relevant components.

Setup

 To set up the project, follow these steps:

- Clone the repository: Clone the project repository from your source control system.

- Python Environment: Set up a Python environment and install the required libraries (e.g., scikit-learn, pandas).
  
- Spring Boot Environment: Ensure you have a Java development environment and Maven set up to build and run the Spring Boot application.

To run the application:
    
    mvn spring-boot:run

Python Model:

 train.py: Contains the code for data preparation and model training.

 predict.py: Contains the code for making predictions based on device specifications

 Spring Boot API

Based on the specs of the devices, the Spring Boot project offers a RESTful API for estimating the price range of certain devices. Important elements consist of:

The model class that represents device specs is called DeviceSpecs.java.
The RESTful API controller PricePredictionController.java manages requests and exchanges information with the Python project to make predictions.

Endpoints

The API's primary endpoint is this:

/api/predict: Provides the anticipated price range in response to a POST request with a JSON payload containing device specs.

Testing and Usage

Postman and Curl are two tools you can use to test the API. Provide a JSON object that represents the device requirements in POST queries to the /api/predict endpoint. Check to see if the API provides the anticipated pricing range.
