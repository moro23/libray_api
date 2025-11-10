# Library Website and API

A project that demonstrates the use of Django for creating a traditional website and Django REST Framework for building a web API.

## Project Overview

This project consists of two main components:

1.  A **Library Website** (`books` app) that displays a list of books from the database using Django's template engine.
2.  A **Web API** (`apis` app) that provides a JSON representation of the same book data.

## Features

-   **Website:** A webpage at the root URL (`/`) that lists all books.
-   **API:** A read-only API endpoint at `/apis/` that returns a list of all books in JSON format.
-   **Admin:** The Django admin interface is configured to manage the `Book` model.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)
*   Git

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/<your-username>/library-api.git
cd library-api
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to keep the project's dependencies isolated.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

After activation, your terminal prompt should be prefixed with `(venv)`, indicating that the virtual environment is active.

### 3. Install Dependencies

With the virtual environment activated, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Once the installation is complete, follow these steps to run the application.

### 1. Apply Database Migrations

This command will create the database and the necessary tables for the application.

```bash
python manage.py migrate
```

### 2. Create a Superuser

To access the Django admin panel, you need to create a superuser.

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### 3. Run the Development Server

Start the Django development server with the following command:

```bash
python manage.py runserver
```

The application will now be running at `http://127.0.0.1:8000/`.

### 4. Access the Application

You can now access the different parts of the project:

*   **Admin Panel:** Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials. Here you can add, edit, and delete books.
*   **Library Website:** Navigate to `http://127.0.0.1:8000/` to see the list of books rendered as an HTML page.
*   **Book API:** Navigate to `http://127.0.0.1:8000/apis/` to see the browsable API, which returns a list of all books in JSON format.
```

