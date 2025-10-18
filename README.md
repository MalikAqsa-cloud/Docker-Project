# Docker Assignment - Full Stack Application

**Student:** [Your Name]  
**Course:** [Course Name]  
**Assignment:** Docker Containerization Project  
**Date:** [Current Date]

## 📋 Project Overview

This project demonstrates a complete full-stack application containerized with Docker, featuring a **Flask backend** served by **Gunicorn** and a **Nginx frontend** with reverse proxy configuration. The application showcases modern DevOps practices including health checks, production-ready configurations, and proper service orchestration.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │
│   (Nginx)       │◄──►│   (Flask+Gunicorn)│
│   Port: 3000    │    │   Port: 5000    │
└─────────────────┘    └─────────────────┘
         │                       │
         └───────────────────────┘
                   │
            Docker Compose
```

## 📁 Project Structure

```
docker-assignment/
├── backend/
│   ├── app.py              # Flask API with production endpoints
│   ├── requirements.txt    # Python dependencies (Flask + Gunicorn)
│   └── Dockerfile         # Production backend container
├── frontend/
│   ├── index.html          # Modern responsive frontend
│   ├── nginx/
│   │   └── default.conf    # Nginx reverse proxy configuration
│   └── Dockerfile         # Production frontend container
├── docker-compose.yml     # Multi-container orchestration
├── README.md              # This documentation
└── screenshots/           # Project screenshots
```

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed and running
- Docker Compose v2.0+ installed
- Git (for version control)

### Step 1: Clone and Navigate
```bash
git clone [your-repository-url]
cd docker-assignment
```

### Step 2: Build and Run
```bash
docker compose up --build
```

### Step 3: Access Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## 🔧 API Endpoints

### Backend Service (Port 5000)

| Endpoint | Method | Description | Example Response |
|----------|--------|-------------|-----------------|
| `/api/health` | GET | Health check for monitoring | `{"status": "healthy", "service": "docker-assignment-backend"}` |
| `/api/greet` | GET/POST | Greeting with optional name parameter | `{"message": "Hello, World!"}` |
| `/api/echo` | POST | Echo back JSON data | `{"echo": {"message": "test"}}` |
| `/api/info` | GET | Service information | `{"service": "Docker Assignment Backend"}` |

### Frontend Service (Port 3000)
- Serves static HTML/CSS/JavaScript
- Proxies `/api/*` requests to backend
- Includes health check endpoint at `/health`

## 🐳 Docker Configuration Details

### Backend Dockerfile Features
- **Base Image**: Python 3.11-slim (production-optimized)
- **Security**: Non-root user execution
- **WSGI Server**: Gunicorn with 2 workers
- **Health Check**: Built-in endpoint monitoring
- **Resource Limits**: Memory constraints for production

### Frontend Dockerfile Features
- **Base Image**: Nginx Alpine (lightweight)
- **Security Headers**: XSS protection, content type validation
- **Compression**: Gzip enabled for performance
- **Caching**: Static asset optimization
- **Health Check**: Nginx status monitoring

### Docker Compose Features
- **Service Dependencies**: Frontend waits for backend health
- **Health Checks**: Both services monitored
- **Resource Limits**: Memory constraints defined
- **Custom Network**: Isolated service communication
- **Restart Policies**: Automatic recovery

## 📸 Screenshots Required

Please capture and save the following screenshots in the `screenshots/` folder:

1. **Frontend Homepage** - http://localhost:3000
2. **Backend API Response** - http://localhost:5000/api/health
3. **Docker Compose Logs** - `docker compose logs`
4. **Container Status** - `docker compose ps`
5. **Health Check Status** - `docker compose ps --format "table {{.Name}}\t{{.Status}}"`

## 🧪 Testing Instructions

### Manual Testing
1. **Start Services**: `docker compose up --build`
2. **Test Frontend**: Visit http://localhost:3000
3. **Test API Health**: Click "Test Health" button
4. **Test Greeting**: Click "Greet with Name" button
5. **Test Echo**: Click "Test Echo" button
6. **Verify Service Info**: Click "Get Service Info" button

### Command Line Testing
```bash
# Test backend health
curl http://localhost:5000/api/health

# Test greeting endpoint
curl http://localhost:5000/api/greet?name=Docker

# Test echo endpoint
curl -X POST http://localhost:5000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello Docker!"}'

# Test frontend health
curl http://localhost:3000/health
```

## 🔍 Monitoring and Debugging

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f frontend
```

### Container Status
```bash
# Running containers
docker compose ps

# Resource usage
docker stats
```

### Health Check Status
```bash
# Detailed health status
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

## 🚀 Deployment Commands

### Development
```bash
# Build and start
docker compose up --build

# Run in background
docker compose up -d --build

# Stop services
docker compose down
```

### Production Considerations
```bash
# Build without cache
docker compose build --no-cache

# Scale backend (if needed)
docker compose up --scale backend=3

# View resource usage
docker compose top
```

## 📚 Learning Objectives Demonstrated

This project showcases:

- ✅ **Containerization**: Docker images for both frontend and backend
- ✅ **Orchestration**: Docker Compose for multi-container management
- ✅ **Production Practices**: Gunicorn WSGI server, health checks, security headers
- ✅ **Reverse Proxy**: Nginx configuration for API routing
- ✅ **Service Communication**: Inter-container networking
- ✅ **Monitoring**: Health checks and logging
- ✅ **Resource Management**: Memory limits and restart policies
- ✅ **Modern Web Development**: Responsive UI with API integration

## 🔧 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Check port usage
netstat -tlnp | grep :3000
netstat -tlnp | grep :5000
```

**Container Won't Start**
```bash
# Check logs
docker compose logs backend
docker compose logs frontend

# Rebuild containers
docker compose down
docker compose up --build
```

**Health Check Failures**
```bash
# Check health status
docker compose ps
docker compose logs backend
```

## 📝 Submission Checklist

- [ ] Project builds successfully with `docker compose up --build`
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend API responds at http://localhost:5000
- [ ] All API endpoints tested and working
- [ ] Screenshots captured and saved in `screenshots/` folder
- [ ] Code pushed to GitHub repository
- [ ] README.md updated with your information

## 🎯 Next Steps

1. **Take Screenshots**: Capture all required screenshots
2. **Test Thoroughly**: Verify all functionality works
3. **Push to GitHub**: Commit and push your code
4. **Document Issues**: Note any problems encountered
5. **Submit Assignment**: Follow your course submission guidelines

---

**Assignment completed successfully! 🎉**

*This project demonstrates proficiency in Docker containerization, multi-service orchestration, and modern web application deployment practices.*