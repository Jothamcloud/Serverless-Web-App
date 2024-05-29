# Serverless Web Application

This is a serverless web application hosted on AWS using the following services:
- Amazon S3
- Amazon CloudFront
- AWS Route 53
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SNS

## Architecture

The architecture of this serverless web application is as follows:

1. *Route 53*:
   - *Domain Management*: AWS Route 53 is used to manage your domain names and DNS settings, ensuring that your web application can be accessed via a user-friendly URL.

2. *CloudFront*:
   - *Content Delivery Network (CDN)*: Amazon CloudFront is used to distribute your web content globally with low latency and high transfer speeds. It caches the content stored in S3 and serves it to users.

3. *S3 (Simple Storage Service)*:
   - *Static Content Hosting*: Amazon S3 is used to host your static web content (HTML, CSS, JavaScript, images, etc.). CloudFront fetches this content from S3 to deliver it to users.

4. *API Gateway*:
   - *API Endpoint Management*: Amazon API Gateway acts as the entry point for your application's backend. It handles all the API calls from the client, invoking Lambda functions to process these requests.

5. *Lambda*:
   - *Serverless Compute*: AWS Lambda is used to run your backend code without provisioning or managing servers. When a user submits the form, API Gateway triggers a Lambda function to process the form data.

6. *DynamoDB*:
   - *Database*: Amazon DynamoDB is used to store the form data. The Lambda function inserts the user-submitted data into a DynamoDB table for persistent storage.

7. *SNS (Simple Notification Service)*:
   - *Notifications*: Amazon SNS is used to send email notifications. The Lambda function publishes a message to an SNS topic when a user submits the form, triggering an email notification to the admin.

### Architectural Flow:
1. *User Request*:
   - The user accesses the web application via a custom domain managed by Route 53.
   
2. *Content Delivery*:
   - The user's request is routed through CloudFront, which serves static content from S3.

3. *Form Submission*:
   - When the user submits a form, the browser sends a request to API Gateway.

4. *API Gateway*:
   - API Gateway receives the form submission and invokes a Lambda function.

5. *Lambda Function*:
   - The Lambda function processes the form data. It saves the data to DynamoDB.
   - The Lambda function also publishes a message to an SNS topic.

6. *SNS Notification*:
   - SNS sends an email notification to the admin based on the message published by the Lambda function.

Here’s a visual representation of this architecture:

![Architecture Diagram](https://github.com/Jothamcloud/Serverless-Web-App/blob/master/Screenshot%202024-05-29%20093156.png)
### Textual Representation of the Architecture


User

 ➡
 
Route 53 (Custom Domain)

 ➡
 
CloudFront (CDN)

➡ 

S3 (Static Web Content)

 ➡
 
API Gateway (API Management)
 
 ➡
 
Lambda (Backend Logic)

 ➡
 
DynamoDB (Data Storage)   SNS (Notifications)
                        
                         ➡
                         
                 Admin Email Notification


## Getting Started

### Prerequisites

- Node.js and npm
- AWS Management Console access
- Serverless Framework installed globally (npm install -g serverless)

### Deployment Steps

#### 1. Set Up S3 for Static Hosting

1. Open the AWS Management Console.
2. Navigate to *S3*.
3. Create a new bucket (e.g., your-website-bucket).
4. Enable static website hosting in the properties of the bucket.
5. Upload index.html and form.html to the bucket.

#### 2. Set Up CloudFront

1. Navigate to *CloudFront* in the AWS Management Console.
2. Create a new distribution.
3. Set the origin domain to your S3 bucket.
4. Configure the distribution settings as needed.
5. Use AWS Certificate Manager (ACM) to create a certificate for your domain and attach it to the CloudFront distribution.

#### 3. Set Up Route 53

1. Navigate to *Route 53* in the AWS Management Console.
2. Create a hosted zone for your domain.
3. Add a record set to point to the CloudFront distribution.

#### 4. Set Up API Gateway

1. Navigate to *API Gateway* in the AWS Management Console.
2. Create a new REST API.
3. Create a new resource and method (e.g., POST /submit).
4. Integrate the method with a Lambda function.

#### 5. Set Up Lambda

1. Navigate to *Lambda* in the AWS Management Console.
2. Create a new function with Python 3.9 runtime.
3. Copy and paste the content from lambda\handler.py into the function editor.
4. Set up the necessary IAM roles and permissions for the Lambda function to access DynamoDB and SNS.

#### 6. Set Up DynamoDB

1. Navigate to *DynamoDB* in the AWS Management Console.
2. Create a new table (e.g., UserSubmissions) with id as the primary key.

#### 7. Set Up SNS

1. Navigate to *SNS* in the AWS Management Console.
2. Create a new topic (e.g., FormSubmissionTopic).
3. Subscribe your email to the topic.


   sh
   npm install
   



By following this order and structure, you can create a scalable and efficient serverless web application using AWS services.
```
