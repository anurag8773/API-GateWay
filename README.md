# Microservices Project with Django and Flask

This repository contains a microservices-based project that leverages Django for backend development and Flask for additional API handling. It demonstrates a seamless integration of two frameworks with RabbitMQ as a message broker and MySQL as the database.

## Features

- **Django Microservices**: Provides REST APIs for managing products and user-related operations.
- **Flask Microservices**: Handles additional API functionalities like liking products and RabbitMQ message publishing.
- **Message Queue**: Implements RabbitMQ for asynchronous communication between services.
- **Database**: MySQL is used to store data with proper relational mapping.
- **Docker Integration**: The project is containerized using Docker Compose for seamless deployment.

## Technologies Used

- **Django**
- **Flask**
- **RabbitMQ**
- **MySQL**
- **Docker & Docker Compose**
- **Postman** (for API testing)

## Installation

### Prerequisites

Ensure the following are installed on your system:

- Python (3.8+)
- Docker & Docker Compose
- Git

### Steps to Clone and Run

1. Clone the repository:
   ```bash
   git clone https://github.com/anurag8773/API-GateWay.git
   cd API-GateWay
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Apply Django migrations:
   ```bash
   docker exec -it <django-container-id> python manage.py makemigrations
   docker exec -it <django-container-id> python manage.py migrate
   ```

4. Open the Flask and Django services:
   - Django: `http://localhost:8000`
   - Flask: `http://localhost:8001`

5. Use Postman to test APIs.

## Project Structure

```
API-GateWay/
├── django-app/           # Contains Django service
├── flask-app/            # Contains Flask service
├── docker-compose.yml    # Docker configuration
├── README.md             # Project documentation
└── .env                  # Environment variables
```

## API Endpoints

### Django Endpoints

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| GET    | `/api/products`         | List all products       |
| POST   | `/api/products`         | Create a new product    |
| GET    | `/api/products/<id>`    | Retrieve a product      |
| PUT    | `/api/products/<id>`    | Update a product        |
| DELETE | `/api/products/<id>`    | Delete a product        |
| GET    | `/api/user`             | Retrieve user details   |

### Flask Endpoints

| Method | Endpoint                     | Description             |
|--------|------------------------------|-------------------------|
| GET    | `/api/products`              | List all products       |
| POST   | `/api/products/<id>/like`    | Like a product          |

## Postman Collection
Collection Link: https://documenter.getpostman.com/view/37271849/2sAYJ7ey2G

A Postman collection has been prepared for manual testing of the APIs. Import the collection into Postman to start testing.

## Testing Steps

### Manual API Testing

1. Use the Postman collection to test each endpoint.
2. Provide the necessary headers and body content for POST and PUT requests.
3. Verify the response status and body.


## Common Issues

- **RabbitMQ Connection Issues**: Ensure RabbitMQ is running and accessible.
- **Database Connectivity**: Check if the MySQL service is up and running.
- **Host Configuration**: Update the `ALLOWED_HOSTS` in Django settings to include `host.docker.internal`.

## Problems Faced and Learnings

### Problems Faced
1. **Database Connection Issues**:
   - Encountered MySQL connection errors due to incorrect credentials.
   - Resolved by ensuring consistent environment variables in `docker-compose.yml`.

2. **RabbitMQ Channel Closure**:
   - Faced `Channel is closed` errors during message publishing.
   - Fixed by ensuring a persistent connection and handling connection resets in `producer.py`.

3. **Django Host Restrictions**:
   - Received `Invalid HTTP_HOST header` errors.
   - Resolved by adding `host.docker.internal` to `ALLOWED_HOSTS`.

4. **Duplicate Entries in Database**:
   - Encountered `IntegrityError` when users liked the same product multiple times.
   - Implemented unique constraints in the `ProductUser` model to handle duplicates.

5. **Docker Networking Issues**:
   - APIs running in containers couldn’t resolve `localhost`.
   - Solved by using `host.docker.internal` for inter-service communication.

### Learnings
- **Microservices Architecture**: Gained hands-on experience in designing loosely coupled systems.
- **Event-Driven Communication**: Learned how RabbitMQ facilitates asynchronous communication.
- **Database Transactions**: Understood the importance of atomic transactions in avoiding data inconsistencies.
- **Containerization**: Mastered Docker Compose for orchestrating multi-container applications.
- **API Testing**: Improved skills in creating detailed Postman collections for manual testing.

---


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.
