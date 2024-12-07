Django-Driven API Performance and Scalability with AWS EC2
Project Overview
This project demonstrates the development of a scalable and high-performance REST API for managing car data using Django REST Framework, with deployment on AWS EC2. The focus is on leveraging Django's capabilities to create robust endpoints while ensuring scalability and performance optimization using cloud-based solutions.

Features:
CRUD operations (Create, Read, Update, Delete) on car data stored in a CSV file.
RESTful API endpoints built with Django and Django REST Framework.
Deployment on AWS EC2 and Elastic Beanstalk for scalability and high availability.
Performance optimization to handle large volumes of requests.
Comprehensive testing with Postman, RapidAPI, and JMeter.
Integration with AWS CloudWatch for API monitoring and debugging.
Objectives
Car Data Management: Handle car details dynamically using CSV files.
API Development: Secure and efficient REST API endpoints for managing car data.
Deployment & Scalability: Cloud-based deployment on AWS EC2, supporting high traffic.
Testing & Optimization: Verify functionality and optimize performance using tools like Postman and JMeter.
Documentation: Provide user-friendly API documentation with usage examples.
Technologies Used
Backend Framework: Django REST Framework
Cloud Platform: AWS EC2, Elastic Beanstalk
Testing Tools: Postman, JMeter, RapidAPI
Storage: CSV file (future enhancements include transitioning to databases)
Monitoring: AWS CloudWatch
Version Control: GitHub
Frontend: React.js (for simple UI)
Deployment Steps
AWS EC2 Setup:
Launch an EC2 instance and configure security groups to allow HTTP traffic on port 8000.
Connect to the instance using SSH and install required packages.
Run the Django Server:
Deploy the project by running the Django development server on the EC2 instance.
Testing:
Use Postman to test all API endpoints.
Publish the API on RapidAPI for broader accessibility.
API Endpoints
1. Fetch All Cars
Endpoint: /cars/
Description: Retrieve all cars from the CSV file.

2. Filter Cars by Make and Year
Endpoint: /cars/search?make=Toyota&year=2020
Description: Filter car data using query parameters.

3. Add a Car
Endpoint: /cars/add
Description: Add new car details to the CSV file.

4. Update a Car
Endpoint: /cars/update/{id}
Description: Update details of an existing car by ID.

5. Delete a Car
Endpoint: /cars/delete/{id}
Description: Delete a car entry by ID.

Results
Successfully deployed on AWS EC2 with minimal latency.
API passed all functional tests, including edge cases.
Scalability validated through load testing.
Clear and user-friendly documentation provided for developers.
Future Enhancements
Transition from CSV to database storage for better scalability.
Implement advanced authentication mechanisms.
Add support for bulk operations and advanced filtering.
Integrate advanced monitoring and analytics tools.
References
RapidAPI Tutorials
Kaggle - US Cars Dataset
AWS EC2 Documentation
Postman Testing
This README provides a detailed overview for any developer or stakeholder to understand the project objectives, features, and deployment steps.
