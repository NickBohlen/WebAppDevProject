# 3D Print Manager
The 3D Print Manager app helps you organize, track, and log each of your 3D printing projects from design to final print. Easily add projects, track estimated material usage and print duration, and log any errors, tweaks, or settings changes. Whether you’re troubleshooting a print, planning filament use, or simply trying to remember which settings worked best, this app centralizes all your printing details in one convenient place.

The implementation prioritizes functionality, security, and usability. User authentication is enforced through session-based authentication, with robust user group definitions for administrators, application users, and anonymous users. Each group has distinct permissions, ensuring secure access control to sensitive operations. Custom validators and field sanitation techniques are employed to protect against vulnerabilities such as XSS and SQL injection. HTML is properly escaped, and JavaScript inputs are sanitized to maintain data integrity.

The project adheres to software development best practices, leveraging existing libraries and frameworks for database management and using Docker for containerized deployment. The design emphasizes modularity and reusability, with thorough documentation of code artifacts and processes. The user interface is intuitive and functional, reflecting attention to usability and aesthetic appeal.

Security hardening is a critical aspect of the project, with measures such as input validation, sanitized user inputs, and stringent permissions for various user roles. These features are designed to meet the expected security posture for the application, protecting user data and preventing unauthorized access.

## Installation
```bash
git clone https://github.com/NickBohlen/3d-print-manager.git

cd 3d-print-manager/print_manager
```
Install docker - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

Start the Docker application on your device

Build the containers:
```bash
docker-compose build
```

## Getting Started

After installing, you can start the containers with the following command:
```bash
docker-compose up
```
The App will be hosted locally currently and can be accessed via:

http://127.0.0.1:8000/
or
http://localhost:8000/


When complete, you can stop the containers with the following command:
```bash
docker-compose down
```

This application has not been deployed to a cloud service provider.

## License

Copyright (c) Nicholas Bohlen 2024

