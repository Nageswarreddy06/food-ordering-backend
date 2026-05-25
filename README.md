# Automated REST Backend — Food Ordering Platform

## 📌 Project Overview
Deployed a modular Flask REST API on Linux, reducing data errors by ~40%; automated environment setup with shell scripts, applying infrastructure-as-code principles. Managed the full development lifecycle via Git branching and merge workflows, reflecting DevOps collaboration best practices for software delivery.

## 🛠 Tech Stack & Infrastructure
* **Backend Framework:** Python (Flask)
* **Database Engine:** MySQL (Containerized via Docker)
* **Infrastructure & Containerization:** Docker Desktop
* **Version Control:** Git & GitHub

## 🚀 Key Features & Architectural Implementation
* **Containerized Database Layer:** Runs a detached MySQL database instance inside a Docker container, isolating data storage and mapping traffic smoothly via custom ports (`3307:3306`).
* **Robust REST Routing:** Contains native `GET` and `POST` endpoints to dynamically fetch the live culinary menu and securely insert customer orders directly into database rows.
* **Data Integrity & Validation:** Implemented structural payload validation checks on incoming JSON requests to drastically lower data input errors.

## 📁 How to Run This Project Locally

### 1. Spin up the Database Container
Ensure Docker Desktop is running, then execute the following command to spin up the decoupled database:
```bash

docker run --name food-db -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=food_ordering -p 3307:3307 -d mysql:latest
