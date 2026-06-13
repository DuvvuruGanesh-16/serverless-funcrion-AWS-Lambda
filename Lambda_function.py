import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):

    table.put_item(
        Item={
            'Id': '1',
            'name': 'Ganesh',
            'email': 'ganesh@gmail.com'
        }
    )

    table.put_item(
        Item={
            'Id': '2',
            'name': 'Rahul',
            'email': 'rahul@gmail.com'
        }
    )

    table.put_item(
        Item={
            'Id': '3',
            'name': 'Priya',
            'email': 'priya@gmail.com'
        }
    )

    table.put_item(
        Item={
            'Id': '4',
            'name': 'Anjali',
            'email': 'anjali@gmail.com'
        }
    )

    return {
        'statusCode': 200,
        'body': '4 records inserted successfully'
    }
