import boto3
import secrets
import datetime

db = boto3.client('dynamodb')

def handler(event, context):
  newURL = secrets.token_urlsafe(40)
  timestamp = str(datetime.datetime.now())
  data = db.put_item(
    TableName='lcos-dev-cfstack-createdb-myDynamoDBTable-12WJFULYOYUJK',
    Item={
        'lcos_masterlist_pk': {
          'S': newURL
        },
        'TimeStamp': {
          'S': timestamp
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': 'successfully created item!',
      'items' : {
        'URL' : newURL,
        'timestamp' : timestamp
      },
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response