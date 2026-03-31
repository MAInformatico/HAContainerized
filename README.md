# HAContainerized

A fully containerized home automation setup for **Home Assistant** on a Raspberry Pi (tested on Raspberry Pi 4 Model B), designed to demonstrate practical backend and DevOps skills.

## Project Overview

This repository includes:

1. **Home Assistant Docker setup**  
   - Automates home devices and sensors  
   - Runs in a self-contained Docker container for easy deployment  

2. **Python REST microservice for pollen data**  
   - Scrapes pollen levels from the [UGR website](https://polen.redugr.es/provincias/granada/)  
   - Exposes real-time data in JSON format for Home Assistant integration  
   - Built with Python, `http.server`, `requests`, and `re`  

3. **Docker Compose orchestration**  
   - Runs both Home Assistant and the pollen microservice in isolated containers  
   - Automatic restart and local network access configured  
   - Enables reproducible, portable deployment

## Key Skills Demonstrated

- Backend development: Python, REST APIs, data scraping, JSON handling  
- DevOps: Docker, Docker Compose, containerized deployments  
- Version control: Git/GitHub workflow  
- IoT/Home automation: Home Assistant integration  

## How to Use

1. Clone the repository:  
   ```bash
   git clone git@github.com:MAInformatico/HAContainerized.git
   cd HAContainerized
(Do not forget to check the comments using < > on the source files)   

Using this reference as Source: https://www.manelrodero.com/blog/instalacion-de-home-assistant-en-docker


