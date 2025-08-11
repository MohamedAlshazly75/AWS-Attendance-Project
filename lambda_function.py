import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Attendance')

def lambda_handler(event, context):

    body = json.loads(event['body'])
    student_id = body.get('student_id')
    student_name = body.get('student_name')
    date_today = datetime.utcnow().strftime('%Y-%m-%d')

   
    response = table.get_item(
        Key={
            'student_id': student_id,
            'date': date_today
        }
    )

    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'تم تسجيل الحضور مسبقاً'})
        }

    
    table.put_item(
        Item={
            'student_id': student_id,
            'student_name': student_name,
            'date': date_today,
            'status': 'Present'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'تم التسجيل بنجاح'})
    }