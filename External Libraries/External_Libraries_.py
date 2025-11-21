# 🔹 1) Virtual Environments & Package Management
# Task:
 
# Create a virtual environment named my_env
# Install the packages: requests, pandas
# Write a Python script that prints the version of each 
# installed package using import pkg_resources.
# Expected Output Example:
# requests==2.31.0
# pandas==2.1.0

import pkg_resources

packages = ['requests', 'pandas']

for package in packages:
    version = pkg_resources.get_distribution(package).version
    print(f"{package}=={version}")
    
