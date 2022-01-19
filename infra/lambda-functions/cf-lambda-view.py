import boto3
import secrets
import datetime
import json

db = boto3.client('dynamodb')

def handler(event, context):
  
  
  # print(event["postid"])
  # print(type(specific_item))

  # possibly...
  # database = db.Table('lcos-dev-cfstack-createdb-myDynamoDBTable-12WJFULYOYUJK')
  # item = database.get_item(Key)


  # db_item = db.get_item(
  #   TableName='lcos-dev-cfstack-createdb-myDynamoDBTable-12WJFULYOYUJK',
  #   Key={
  #     'lcos_masterlist_pk' : {
  #       'S' : specific_item
  #       }
  #     }
  #   )
  
  if len(event["postid"]) != 0:
    print("event is not Empty")
    specific_item = event["postid"]
    db_item = get_post(specific_item)
  else:
    print("event is Empty")
    # get all objects
    db_item = get_all()
  # db_item = len(event["postid"])


  
  return db_item



def get_post(postid):

  db_item = db.get_item(
  TableName='lcos-dev-cfstack-createdb-myDynamoDBTable-12WJFULYOYUJK',
  Key={
    'lcos_masterlist_pk' : {
      'S' : postid
      }
    }
  )

  response = {
      'statusCode': 200,
      'body': 'successfully retrieved item!',
      'items' : db_item,  
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }

  return response



def get_all():

  db_items = db.scan(
  TableName='lcos-dev-cfstack-createdb-myDynamoDBTable-12WJFULYOYUJK')
  
  response = {
      'statusCode': 200,
      'body': 'Here are all the objects;',
      'items' : db_items,
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }


  return response

