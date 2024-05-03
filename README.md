# Password Recovery System

## Project Overview
The Password Recovery System is designed to securely generate and recover passwords using the SHA-256 hashing algorithm. This project not only demonstrates salted hash generation and brute-force password recovery but also incorporates external storage functionality to simulate real-world data handling scenarios. This enhances both the application's efficiency and security.

## Features
- **Password Input**: Accepts a four-character password from the user.
- **Salt Generation**: Automatically generates a random 16-character salt.
- **Hash Generation**: Produces a secure hash using SHA-256, which is then stored externally.
- **Password Recovery**: Employs a brute-force method to recover the original password using the stored hash and salt from external storage.

## Getting Started
These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites
Ensure you have the following installed:
- **Python 3.8 or higher**
  - Python can be installed from [Python's official website](https://python.org).

### Installing
Follow these steps to get your development environment running:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alshohb/Digital-Forensics-Password-Cracker.git

2. Navigate to the project directory:
cd Digital-Forensics-Password-Cracker

3. Run the script:
python password_recovery.py


## Usage
Execute the script and follow the on-screen prompts to enter a password. The system will generate a hash and store it along with the salt in an external file. You can then proceed to test the password recovery functionality.
