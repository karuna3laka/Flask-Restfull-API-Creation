# Flask Planets API

This project is a Flask-based RESTful API designed to manage planetary and user data using an SQLite database. It includes functionality for CRUD operations, dynamic routing, and database commands.

## Features

- **CLI Commands:**
  - `db_create`: Creates the database tables.
  - `db_drop`: Drops all the database tables.
  - `db_seed`: Seeds the database with sample data.

- **API Endpoints:**
  - `/`: A simple welcome endpoint.
  - `/super_simple`: Returns a simple JSON response.
  - `/not_found`: Returns a 404 status with a custom message.
  - `/parameters`: Handles query parameters for name and age.
  - `/url_variable/<name>/<age>`: Demonstrates routing with URL variables.

- **Database Models:**
  - `User`: Manages user data with attributes for first name, last name, email, and password.
  - `Planet`: Manages planetary data, including name, type, mass, radius, and distance from the home star.

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run
   ```

### Database Setup

1. Create the database tables:
   ```bash
   flask db_create
   ```

2. Seed the database with sample data:
   ```bash
   flask db_seed
   ```

3. Drop the database tables:
   ```bash
   flask db_drop
   ```

## API Endpoints

- `GET /`
  - **Description:** Returns a "Hello World!" message.

- `GET /super_simple`
  - **Description:** Returns a simple JSON response with a message.

- `GET /not_found`
  - **Description:** Returns a 404 status with a custom not-found message.

- `GET /parameters`
  - **Description:** Accepts `name` and `age` as query parameters and validates the age.
  - **Example:** `/parameters?name=John&age=25`

- `GET /url_variable/<name>/<age>`
  - **Description:** Accepts `name` and `age` as URL variables and validates the age.
  - **Example:** `/url_variable/John/25`

## Database Models

### User
- `id`: Integer, Primary Key.
- `first_name`: String.
- `last_name`: String.
- `email`: String, Unique.
- `password`: String.

### Planet
- `planet_id`: Integer, Primary Key.
- `planet_name`: String.
- `planet_type`: String.
- `home_star`: String.
- `mass`: Float.
- `radius`: Float.
- `distance`: Float.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

