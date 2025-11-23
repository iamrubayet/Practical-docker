# Docker Practical Project

A practical Docker project demonstrating multi-container application architecture using Docker Compose. This project consists of two microservices: a main Flask web application and a counter service that communicate over a Docker network.

## 📋 Project Overview

This project showcases:
- Multi-container Docker applications using Docker Compose
- Service-to-service communication via Docker networks
- Flask-based microservices architecture
- Volume mounting for development
- Port mapping and container orchestration

## 🏗️ Architecture

The application consists of two services:

### 1. My-App Service
- **Port**: 5000 (exposed to host)
- **Framework**: Flask
- **Purpose**: Main web application that displays page view count
- **Dependencies**: Communicates with the counter service

### 2. Counter Service
- **Port**: 6000 (internal only)
- **Framework**: Flask
- **Purpose**: Maintains and increments a page view counter
- **Endpoint**: `/increment` - Returns the current count

## 🚀 Getting Started

### Prerequisites

- Docker installed on your system
- Docker Compose installed

### Running the Application

1. Clone the repository:
```bash
git clone https://github.com/iamrubayet/Practical-docker.git
cd Practical-docker
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
Open your browser and navigate to `http://localhost:5000`

You should see a message displaying the page view count, which increments with each refresh.

### Stopping the Application

```bash
docker-compose down
```

## 📁 Project Structure

```
.
├── docker-compose.yml          # Docker Compose configuration
├── my-app/
│   ├── app.py                  # Main Flask application
│   ├── Dockerfile              # Dockerfile for my-app service
│   ├── requirements.txt        # Python dependencies
│   └── commands.txt            # Helpful Docker commands
└── counter-service/
    ├── counter_app.py          # Counter service application
    ├── Dockerfile              # Dockerfile for counter service
    └── requirements.txt        # Python dependencies
```

## 🔧 Key Features

### Docker Compose Configuration
- **Networks**: Custom network (`my-app-network`) for inter-service communication
- **Volumes**: Volume mounting for live code updates during development
- **Multi-stage builds**: Optimized Docker images using Python 3.9-slim

### Service Communication
The main app communicates with the counter service using Docker's internal DNS resolution:
```python
response = requests.get('http://counter-service:6000/increment')
```

## 🛠️ Development

### Modifying the Code

Thanks to volume mounting, changes to the code in `my-app/` directory are reflected inside the container. You may need to restart the service to see changes:

```bash
docker-compose restart my-app
```

### Viewing Logs

```bash
# View logs for all services
docker-compose logs

# View logs for a specific service
docker-compose logs my-app
docker-compose logs counter
```

### Building Individual Services

```bash
# Build my-app service
docker-compose build my-app

# Build counter service
docker-compose build counter
```

## 📦 Dependencies

### My-App Service
- Flask 3.1.2
- requests 2.28.2

### Counter Service
- Flask 3.1.2

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**iamrubayet**
- GitHub: [@iamrubayet](https://github.com/iamrubayet)

## 🎓 Learning Outcomes

This project demonstrates:
- Creating custom Docker images with Dockerfiles
- Orchestrating multiple containers with Docker Compose
- Setting up Docker networks for service discovery
- Implementing microservices architecture
- Managing container volumes for development workflows
- Port mapping and container communication

---

Happy Dockerizing! 🐳
