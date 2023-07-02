#!/bin/python3

import boto3

###Describe ec2###
client = boto3.client('ec2')
response = client.describe_instances()
for r in response['Reservations']:
    for i in r['Instances']:
        print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n-------------------------\n")
