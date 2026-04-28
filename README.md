# 🚀 HAContainerized – Home Automation & Environmental Monitoring System
## 📌 Overview

HAContainerized is a fully containerized home automation and environmental monitoring system built around Home Assistant, designed to run efficiently on a Raspberry Pi (tested on Raspberry Pi 4 Model B).

The project combines IoT data ingestion, backend microservices, and containerized deployment, demonstrating practical skills in backend development and DevOps workflows.

## 🎯 Project Goals
- Deploy a reproducible Home Assistant environment using Docker
- Integrate external environmental data into home automation workflows
- Build a lightweight Python microservice exposing real-time data via REST API
- Enable modular, containerized architecture suitable for edge devices
- Demonstrate backend + DevOps integration in a real-world scenario

## 🏗️ System Architecture

The system is composed of two main containerized components:

### 🧠 Home Assistant Core
Central automation engine responsible for:
- Manages devices, sensors, and automation rules
- Consumes external APIs (pollen data service)
- Triggers events based on configured conditions

### 🌿 Pollen Data Microservice (Python REST API)
- External data ingestion service
- Scrapes real-time pollen levels from external source
- Exposes structured JSON API endpoint
- Built with Python, http.server, requests, regex
 
## 🔄 Data Flow
1. External website provides raw pollen data  
2. Python microservice scrapes and transforms raw data into structured JSON format
3. Home Assistant consumes API endpoint on a scheduled interval  
4. Automation engine evaluates conditions  
5. Alerts or actions are triggered based on thresholds  

## 🐳 Docker Architecture

The system follows a lightweight microservice-based architecture optimized for edge deployment:

- Home Assistant runs in an isolated container
- Python microservice runs as an independent API container
- Both services communicate over a shared Docker network
- Automatic restart policies ensure system resilience
- Fully reproducible deployment across environments

## 🧰 Tech Stack

### Backend & APIs
- Python (custom lightweight REST API using HTTP server)
- Web scraping (requests, regex parsing)

### Infrastructure
- Docker / Docker Compose
- Raspberry Pi (ARM deployment)

### Automation
- Home Assistant (event-driven automation engine)

### Version Control:
- Git / GitHub

## 🌍 Key Features
- Containerized IoT backend system with REST API integration
- Real-time environmental monitoring and data integration (pollen levels)
- Modular Docker-based architecture designed for edge deployment
- Edge deployment on Raspberry Pi
- Automation-driven event system

## 💡 What I Learned
- Designing containerized IoT backend systems
- Building and exposing lightweight REST APIs
- Integrating external data sources into automation workflows
- Designing event-driven systems with Home Assistant
- Deploying distributed systems using Docker Compose in constrained environments

## 📌 Possible Improvements
- Introduce time-series storage (InfluxDB) for historical analytics
- Add Grafana dashboards for system observability
- Expand sensor ingestion (CO₂, temperature, humidity)
- Replace scraping layer with official API integration
- Migrate API layer to FastAPI for better scalability

## 🚀 How to Run
   git clone git@github.com:MAInformatico/HAContainerized.git
   cd HAContainerized
   docker-compose up -d

## 📚 Reference

   Based on Home Assistant Docker deployment principles:
   https://www.manelrodero.com/blog/instalacion-de-home-assistant-en-docker
