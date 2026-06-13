# serverless-funcrion-AWS-Lambda
# Serverless Function Using AWS Lambda

## Project Overview

This project demonstrates the implementation of a serverless application using AWS cloud services. The application receives student information through an API endpoint, processes the request using AWS Lambda, and stores the data in Amazon DynamoDB. Amazon CloudWatch is used to monitor and log all Lambda executions.

The project showcases how multiple AWS services can be integrated to build a scalable, reliable, and cost-effective serverless solution without managing any servers.

---

## Problem Statement

Traditional applications require dedicated servers to process requests and store data. Managing servers increases operational complexity, maintenance effort, and infrastructure costs.

The objective of this project is to implement a serverless architecture that automatically processes incoming requests and stores data without requiring server management.

---

## Objectives

* Understand the concept of serverless computing.
* Create and configure AWS Lambda functions.
* Trigger Lambda functions using Amazon API Gateway.
* Store application data in Amazon DynamoDB.
* Monitor application execution using Amazon CloudWatch.
* Implement an end-to-end serverless workflow using AWS services.

---

## Technologies Used

| Service            | Purpose                                       |
| ------------------ | --------------------------------------------- |
| AWS Lambda         | Execute backend code without managing servers |
| Amazon API Gateway | Create and manage HTTP API endpoints          |
| Amazon DynamoDB    | Store student records in a NoSQL database     |
| Amazon CloudWatch  | Monitor and log Lambda executions             |
| AWS IAM            | Manage permissions and security               |
| Python 3.x         | Lambda function development                   |
| Postman            | API testing                                   |

---

## System Architecture

```text
Client / Postman
        │
        ▼
Amazon API Gateway
        │
        ▼
AWS Lambda (formprocessor)
        │
        ▼
Amazon DynamoDB (studentData)
        │
        ▼
Amazon CloudWatch Logs
```

---

## Project Workflow

### Step 1: Create DynamoDB Table

A DynamoDB table named **studentData** was created to store student records. The table serves as the backend database for the application.

### Step 2: Create Lambda Function

A Lambda function named **formprocessor** was developed using Python. The function receives requests from API Gateway and inserts records into DynamoDB.

### Step 3: Configure IAM Permissions

An IAM role was attached to the Lambda function, granting access to perform DynamoDB operations.

### Step 4: Configure API Gateway

An HTTP API was created using Amazon API Gateway. The API endpoint was integrated with the Lambda function.

### Step 5: Test the Application

The API endpoint was tested using Postman. Requests sent to the API successfully triggered the Lambda function.

### Step 6: Store Data in DynamoDB

The Lambda function processed the request and inserted records into the DynamoDB table.

### Step 7: Monitor Using CloudWatch

CloudWatch logs were used to verify successful execution and monitor Lambda performance.

---

## Lambda Function

The Lambda function performs the following operations:

* Receives requests from API Gateway
* Processes incoming student data
* Inserts records into DynamoDB
* Returns a success response
* Generates execution logs in CloudWatch

---

## API Endpoint

The application uses Amazon API Gateway to expose a REST endpoint that triggers the Lambda function.

### Request Flow

```text
POST Request
      │
      ▼
API Gateway
      │
      ▼
Lambda Function
      │
      ▼
DynamoDB
```

---

## Testing

The API was tested using Postman.

### Test Results

* Lambda function executed successfully.
* API Gateway correctly invoked Lambda.
* Records were inserted into DynamoDB.
* CloudWatch logs captured execution details.

---

## Output

The application successfully:

* Received requests through API Gateway.
* Triggered AWS Lambda execution.
* Stored records in DynamoDB.
* Generated CloudWatch logs.
* Returned successful responses to the client.

---

## Screenshots

The repository contains screenshots demonstrating:

* DynamoDB Table Configuration
* AWS Lambda Function
* Lambda Source Code
* API Gateway Configuration
* API Gateway Invoke URL
* Postman Testing
* DynamoDB Records
* CloudWatch Logs

All screenshots are available in the **screenshots** folder.

---

## Advantages of the Project

* No server management required.
* Automatic scaling.
* Pay-per-use pricing model.
* High availability and reliability.
* Easy deployment and maintenance.
* Fast response time.

---

## Conclusion

This project successfully demonstrates the implementation of a serverless architecture using AWS Lambda, API Gateway, DynamoDB, and CloudWatch.

The application processes incoming requests, stores data efficiently in DynamoDB, and provides monitoring through CloudWatch. The project highlights the benefits of serverless computing, including scalability, reduced infrastructure management, and cost efficiency.

---
