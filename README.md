# Food Truck API

This project is a Django-based API that allows users to find the nearest food trucks based on their latitude and longitude.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.8 or above
* You have installed `pip` and `pipenv`

## Installation

Follow these steps to set up your development environment:

1. Clone the repository to your local machine.
2. Navigate to the project directory where the `Pipfile` is located.
3. Run `pipenv install` to install the dependencies and create a virtual environment.

## Running the Application

Once the setup is complete, you can run the application using the following steps:

1. Activate the virtual environment:

   ```shell
   pipenv shell
   ```

2. Run the Django server:

   ```shell
   python manage.py runserver
   ```

## Accessing Swagger UI

After starting the Django server, you can access the Swagger UI by navigating to:

```
http://127.0.0.1:8000/swagger/
```

In the Swagger UI, you can interact with the API and make requests.

## Making API Calls

To find the nearest food trucks, make a `POST` request to the following endpoint:

```
http://127.0.0.1:8000/api/get-food-trucks/
```

Include the latitude and longitude in the request body as JSON:

```json
{
    "latitude": 20.7128,
    "longitude": 74.0060
}
```

Example of a successful response:

```json
{
    "nearest_trucks": [
        {
            "Applicant": "F & C Catering",
            "Location": "(0.0, 0.0)",
            "Distance": 76.84990644002112
        },
        {
            "Applicant": "Quan Catering",
            "Location": "(0.0, 0.0)",
            "Distance": 76.84990644002112
        },
        {
            "Applicant": "SOHOMEI, LLC",
            "Location": "(0.0, 0.0)",
            "Distance": 76.84990644002112
        },
        {
            "Applicant": "Santana ESG, Inc.",
            "Location": "(0.0, 0.0)",
            "Distance": 76.84990644002112
        },
        {
            "Applicant": "Zuri Food Facilities",
            "Location": "(0.0, 0.0)",
            "Distance": 76.84990644002112
        }
    ]
}
```

Replace the example coordinates with actual data to get real results.

## Docker Setup

To containerize the Django application, follow these instructions to use Docker.

### Building the Docker Image

1. Ensure Docker is installed on your system.
2. Navigate to the root of the project directory where the `Dockerfile` is located.
3. Build the Docker image with the following command:

    ```bash
    docker build -t food-truck-api .
    ```

    Replace `food-truck-api` with your preferred image name.

### Running the Docker Container

After building the image, run the container using:

```bash
docker run -d -p 8000:8000 food-truck-api
```

This command will start a container in detached mode, bind port 8000 on your host to port 8000 in the Docker container, and serve your application.

### Accessing the Application

With the container running, you can access the application in your web browser:

- Django Application: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/swagger/`

## License

This project is licensed under the [MIT License](LICENSE).

