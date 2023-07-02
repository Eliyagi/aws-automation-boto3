#!/bin/python3

import boto3

###Deploy ec2###
ec2 = boto3.resource('ec2')

#Create a new EC2 instance
instances = ec2.create_instance(
	ImageId='ami-0b8263ebecd7261d5',
	MinCount=1,
	MaxCount=2,
	InstanceType='t3.micro',
	KeyName='eliya_key_aws'
)

###Destroy ec2###
instances=("enter the ids of the instances that you wish to terminate: ")
ids= [instances]
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds = ids).terminate()

###start ec2###
instances=("enter the ids of the instances that you wish to start: ")
ids= [instances]
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds = ids).start()

###stop ec2###
instances=("enter the ids of the instances that you wish to stop: ")
ids= [instances]
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds = ids).stop()
	