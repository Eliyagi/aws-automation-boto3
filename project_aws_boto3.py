#!/bin/python3

import boto3
from time import sleep

###Deploy ec2###
def deploy_instance():
	ec2 = boto3.resource('ec2')
	instances = ec2.create_instance(
		ImageId=input("Ente AMI ID: \n"),#ami-0989fb15ce71ba39e (ubuntu free)
		MinCount=1,
		MaxCount=int(input("How many instances? \n")),
		InstanceType=input("Which type of instance? t3.micro/else "),
		KeyName=input("Which keyPair? eliya_key_aws/ else \n")#make sure it's exists
    )

###Describe ec2###
def describe_instance():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n-------------------------\n")

###Destroy ec2###
def destroy_instance():
    instances=input("enter the ids of the instances that you wish to terminate: ")
    ids= [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).terminate()

###start ec2###
def start_instance():
    instances=("enter the ids of the instances that you wish to start: ")
    ids= [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).start()

###stop ec2###
def stop_instance():
    instances=("enter the ids of the instances that you wish to stop: ")
    ids= [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).stop()
    
def menu():
        while(True):
            choice=input("Menu:\n1.Deploy EC2\n2.Destroy instance\n3.Stop instance\n4.Start instance\n5.Describe EC2\n")
            match choice:
                case "1":
                    print("Deploy instances: \n")
                    deploy_instance()
                    sleep(2)
                case "2":
                    print("Destroy instances: \n")
                    destroy_instance()
                    sleep(2)
                case "3":
                    print("Stop instances: \n")
                    stop_instance()
                    sleep(2)
                case "4":
                   print("Start instances: \n")
                   start_instance()
                   sleep(2)
                case "5":
                   print("Describe instances: \n")
                   sleep(2)
                   describe_instance()
                   sleep(2)
                case _:
                   print("Choose 1-5 only !\n")
                   sleep(1)
                   continue

            exit=input("Do you wish to exit? y/n \n")
            if(exit=="y"):
                print("bye bye...\n")
                break

menu()
