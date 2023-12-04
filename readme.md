# Calculator App

This project is a simple calculator application built using FastAPI for the backend and React for the frontend. Docker is used for containerization.

## Getting Started

### Prerequisites

Make sure you have Docker installed on your machine. You can download it [here](https://www.docker.com/products/docker-desktop).

### Installation

1. Clone the repository:

   
    git clone https://github.com/your-username/calculator-app.git
    

2. Navigate to the project root:

    
    cd calculator-app
    

### Running the App with Docker Compose

Run the following command to start the services:

   
    docker-compose up

This will build and start the containers for the Python backend and React frontend. The app will be accessible at http://localhost:80.

The Python backend will be available at http://localhost:8000.


### Documentation
#### Backend - FastAPI
main.py
This module contains the FastAPI application for the calculator backend.

app: FastAPI application instance.
Base: SQLAlchemy declarative base for database models.
Calculation: SQLAlchemy model for calculations.
evaluate_npi: Function to evaluate expressions in Reverse Polish Notation (RPN).
calculate: FastAPI endpoint for evaluating expressions.
export_to_csv: FastAPI endpoint for exporting calculations to CSV.
calculations.py
This module contains functions for evaluating mathematical expressions.

evaluate_npi: Function to evaluate expressions in Reverse Polish Notation (RPN).
export.py
This module contains functions for exporting calculations to CSV.

export_to_csv: Function to export calculations to CSV.

#### Frontend - React
App.js
This file contains the main component for the React frontend.

Main component structure and logic.

### Testing
The project includes unit tests for both the backend and frontend components. To run tests, follow the instructions mentioned above for each component.
