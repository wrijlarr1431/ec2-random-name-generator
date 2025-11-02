import random

## --- Welcome Screen ---

print("EC2 Instance Generator")

## --- Department Name and Number of Instances ---

department_name = input("Department Name: ")

ec2_numbers = input("EC2 Instances to be created?: ")

## --- Generate EC2 Names ---

print(f"\nEC2 Names for {department_name}:")
print("-" * 40)
