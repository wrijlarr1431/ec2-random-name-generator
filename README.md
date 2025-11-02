# EC2 Instance Name Generator

A Python script that generates a unique EC2 instance name for AWS environments with multiple department.

## Project Overview

This tool helps teams manage EC2 instances in shared AWS environments by generating unique, department-specific instance names.Each name includes a randome aplhanumeric identifier to ensure uniquness and easy identification.

## Features

- **User-friendly interface**: Simple command-line prompts
- **Department customization**: Incorporates department names into EC2 naming
- **Unique identifiers**: Generates random 8-character alphanumeric strings
- **Scalable**: Create names for any number of instances
- **Standardized format**: Follows AWS naming best practices

## How to Use

### Prerequisites
- Python 3.x installed on your system
- No external libraries required (uses built-in modules)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ec2-name-generator.git
cd ec2-name-generator
```

2. Run the script:
```bash
python ec2_name_generator.py
```