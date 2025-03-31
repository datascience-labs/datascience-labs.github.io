# AnomaliFlow
This application provides a robust framework for managing machine learning tasks using a combination of FastAPI, Celery, Streamlit, MongoDB, Prefect and Redis. The system allows users to upload datasets, select features, choose machine learning algorithms, and execute tasks asynchronously. Results and task statuses are displayed in real-time, leveraging the power of modern web technologies and scalable background task processing.

## Features 
- File Upload, Cloud Storage Mount, and Data Preview
- Feature Engineering
- ML/DL Algorithms Selection
- Asynchronous Task & Workflow Execution
- Real-time Status Updates
- Results Display
- API Documentation

## components
- Swagger UI: API Documentation
- Celery: asynchronous task queue/job queue based on distributed message passing
- FastAPI: A modern, fast, web framework for building APIs 
- MongoDB: NoSQL Database
- Redis: in-memory data structure store
- Streamlit: open-source app framework for Machine Learning and Data Science
- Prefect: Data pipeline workflow ochestration

## run
> docker-compose up --build -d

> docker-compose --profile prefect_server up

## access the application
- Streamlit Interface: Open your browser and navigate to http://localhost:8501 to access the Streamlit interface.
- Dash Interface: Open your browser and navigate to http://localhost:8050 to access the Dash interface.
- API Documentation: Visit http://localhost:8000/docs to view the interactive API documentation provided by FastAPI.
- Prefect Interface: Open your browser and navigate to http://localhost:4200 to access the Prefect interface.

### ports
- MongoDB: 27017  (use [Compass](https://www.mongodb.com/products/tools/compass))
- Redis: 6379
- FastAPI: 8000
- Streamlit: 8501
- Prefect: 4200 
