import random
import string

## --- Welcome Screen ---

print("EC2 Instance Generator")

## --- Department Name and Number of Instances ---

department_name = input("Department Name: ")

ec2_numbers = input("EC2 Instances to be created: ")

## --- Generate EC2 Names ---

print(f"\nEC2 Names for {department_name}:")
print("-" * 40)

for i in range(int(ec2_numbers)):
    # Generate Unique 8 character string
    random_chars = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    #Create EC2 name
    ec2_name = f"{department_name.upper()}-EC2-{random_chars}"

    print(f"{i+1}.{ec2_name}")