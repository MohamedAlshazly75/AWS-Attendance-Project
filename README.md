# AWS-Attendance-Project
Simple AWS-based attendance system using Lambda and DynamoDB. Checks if a student has already registered today before saving attendance.
# AWS Attendance System

This project is a **Serverless Attendance Tracking System** built using:
- **AWS Lambda** (Python)
- **Amazon API Gateway**
- **Amazon DynamoDB**
- **Postman** for testing
- **AWS IAM** for permissions

It records student attendance and prevents duplicate check-ins on the same day.

## 📌 Features
- Add a new attendance record with **student_id** and **date**.
- Prevents duplicate attendance for the same student on the same date.
- Serverless architecture with AWS services.
- Can be tested via **Postman** or connected to a frontend.

## 📂 Project Structure
.
├── lambda_function.py       # Lambda backend code
├── aws_attendance_diagram.png  # AWS architecture diagram
└── README.md                # Documentation


**Flow:**
1. **Postman / Frontend** sends a POST request with `student_id` and `date`.
2. **API Gateway** forwards the request to **AWS Lambda**.
3. **Lambda** checks **DynamoDB** to see if the student has already checked in today.
4. If not found, a new record is stored in **DynamoDB**.
5. Response is returned to the client.

## 🗄 DynamoDB Table Structure
**Table Name:** `Attendance`  
**Primary Key (Composite):**
- **Partition Key:** `student_id` (String)
- **Sort Key:** `date` (String, format: YYYY-MM-DD)

**Attributes:**
- `student_id` (String)
- `student_name` (String)
- `date` (String)
- `status` (String: "Present")

## 💻 Lambda Function (Python)
See [lambda_function.py](lambda_function.py)

## 🔐 IAM Role Permissions
Attach this policy to the **Lambda execution role**:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:PutItem"
            ],
            "Resource": "arn:aws:dynamodb:YOUR_REGION:YOUR_ACCOUNT_ID:table/Attendance"
        }
    ]
}
```

## 🧪 Testing with Postman
1. Open Postman.
2. Create a **POST request** to your **API Gateway Invoke URL**.
3. Set **Headers**:
   ```
   Content-Type: application/json
   ```
4. Set **Body** → `raw` → `JSON`:
   ```json
   {
       "student_id": "John Doe",
       "date": "2025-08-10"
   }
   ```
5. Click **Send** and check the response.

## 🚀 Deployment Steps
1. Create DynamoDB table `Attendance` with:
   - Partition key: `student_id` (String)
   - Sort key: `date` (String)
2. Create a Lambda function in Python and upload `lambda_function.py`.
3. Assign an IAM Role with **GetItem** and **PutItem** permissions for DynamoDB.
4. Create an API Gateway REST API and integrate it with Lambda.
5. Enable **CORS** for API Gateway.
6. Deploy the API and test with Postman.

## 📌 Future Enhancements
- Add a frontend web page for attendance marking.
- Email/SMS notifications when attendance is recorded.
- Admin dashboard for attendance reports.
