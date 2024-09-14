# Python Backend Application with CRUD and Vector Search

This project is a Python backend application that allows you to perform CRUD (Create, Read, Update, Delete) operations and vector search using Pinecone, a managed vector database. This application is built using FastAPI for handling API requests.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Perform CRUD operations on items.
- Conduct vector searches using Pinecone.
- FastAPI for building the API.
- Easy integration with Pinecone for managing vectors.

## Technologies

- Python 3.11
- FastAPI
- Pinecone
- SQLAlchemy (for local storage, if needed)
- Uvicorn (for running the server)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Pinecone**:
   - Sign up at [Pinecone](https://www.pinecone.io/) and get your API key.
   - Create an `.env` file in the root directory with the following content:
     ```
     PINECONE_API_KEY=your_pinecone_api_key
     PINECONE_ENVIRONMENT=your_pinecone_environment
     ```

## Usage

1. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to access the automatically generated API documentation.

## API Endpoints

### CRUD Operations

- **Create Item**: `POST /items/`

  - Request body:
    ```json
    {
      "name": "Item name",
      "description": "Item description",
      "vector": [0.1, 0.2, 0.3, ...]  // Vector representation
    }
    ```

- **Read Item**: `GET /items/{item_id}`

  - Response:
    ```json
    {
      "id": "item_id",
      "name": "Item name",
      "description": "Item description",
      "vector": [0.1, 0.2, 0.3, ...]
    }
    ```

- **Update Item**: `PUT /items/{item_id}`

  - Request body:
    ```json
    {
      "name": "Updated name",
      "description": "Updated description",
      "vector": [0.4, 0.5, 0.6, ...]
    }
    ```

- **Delete Item**: `DELETE /items/{item_id}`

### Vector Search

- **Search Vectors**: `POST /search/`
  - Request body:
    ```json
    {
      "vector": [0.1, 0.2, 0.3, ...],
      "top_k": 5  // Number of nearest neighbors to return
    }
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
