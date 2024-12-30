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

A Postman collection has been prepared for manual testing of the APIs. Import the collection into Postman to start testing.

## Testing Steps

### Manual API Testing

1. Use the Postman collection to test each endpoint.
2. Provide the necessary headers and body content for POST and PUT requests.
3. Verify the response status and body.

### Automated Testing

Run Django tests:
```bash
docker exec -it <django-container-id> python manage.py test
```

## Common Issues

- **RabbitMQ Connection Issues**: Ensure RabbitMQ is running and accessible.
- **Database Connectivity**: Check if the MySQL service is up and running.
- **Host Configuration**: Update the `ALLOWED_HOSTS` in Django settings to include `host.docker.internal`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.
