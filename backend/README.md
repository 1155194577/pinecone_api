# FastAPI Vector Management Application

This project is a FastAPI application that allows you to perform CRUD (Create, Read, Update, Delete) operations and vector search using Pinecone, a managed vector database.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Perform CRUD operations on vectors.
- Conduct vector searches using Pinecone.
- FastAPI for building the API.
- Easy integration with Pinecone for managing vectors.

## Technologies

- Python 3.12.5
- FastAPI
- Pinecone

## Installation

1. **Clone the repository**:

```sh
git clone https://github.com/1155194577/rag.git
cd rag/backend
```

2. **Activate the virtual environment**:

```sh
# python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies**:

```sh
pip install -r requirements.txt
```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Pinecone API key and other necessary configurations:

```env
PINECONE_API_KEY=your_pinecone_api_key
NAMESPACE_NAME=your_namespace 
```

or : cd to root dir (backend) and type "pwd" , then type EXPORT="the abs path shown on terminal"

## Usage

1. **Run the FastAPI application**: (at backend root dir)

```sh
python3 main.py
```

2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8080/redoc` to access the automatically generated API documentation.

## API Endpoints

### CRUD Operations

- **Create Vector**: `POST /api/v1/vector/{index_name}/{namespace_name}/`

  - Request body:

  ```json
  {
    "id": "vector_id",
    "values": [0.1, 0.2, 0.3],
    "metadata": { "key": "value" }
  }
  ```

- **Read Vector**: `GET /api/v1/vector/{index_name}/{namespace_name}/`

  - Query Parameters:

  - `vector_id`: str (required)

  - Response:

  ```json
  {
    "id": "vector_id",
    "values": [0.1, 0.2, 0.3],
    "metadata": { "key": "value" }
  }
  ```

- **Delete Vector**: `DELETE /api/v1/vector/{index_name}/{namespace_name}/`

  - Query Parameters:

  - `vector_id`: str (required)

  - Response:

  ```json
  {
    "isSuccessfulDeletion": true
  }
  ```

- **Update Vector**: `PATCH /api/v1/vector/{index_name}/{namespace_name}/`

  - Query Parameters:

  - `vector_id`: str (required)
  - `values`: Optional[List[float]]
  - `metadata`: Optional[Dict]

  - Response:

  ```json
  {
    "isSuccessfulUpdate": true
  }
  ```

### Vector Search

- **Search Vector**: `POST /api/v1/vector/{index_name}/{namespace_name}/search`

  - Request body:

  ```json
  {
    "values": [0.1, 0.2, 0.3],
    "top_k": 5,
    "include_metadata": false,
    "include_values": false
  }
  ```

  - Response:

  ```json
  {
    "matches": [
      {
        "id": "vector_id",
        "score": 0.95,
        "values": [0.1, 0.2, 0.3],
        "metadata": { "key": "value" }
      }
    ]
  }
  ```

### Namespace Operations

- **Delete Namespace**: `DELETE /api/v1/namespace/{namespace_name}/`

  - Response:

  ```json
  {
    "isSuccessfulDeletion": true
  }
  ```

  ### Index Operations

  - **Create Index**: `POST /api/v1/index/`

    - Request body:

    ```json
    {
      "name": "index_name",
      "dimension": 128,
      "metric": "cosine",
      "cloud": "aws",
      "region": "us-west-1"
    }
    ```

    - Response:

    ```json
    {
      "isSuccessfulCreation": true
    }
    ```

  - **Delete Index**: `DELETE /api/v1/index/{index_name}/`

    - Response:

    ```json
    {
      "isSuccessfulDeletion": true
    }
    ```

  - **Get All Index Names**: `GET /api/v1/indexes/`

    - Response:

    ```json
    ["index_name_1", "index_name_2"]
    ```

  - **Get Index Dimension**: `GET /api/v1/index/{index_name}/dimension`

    - Response:

    ```json
    {
      "dimension": 128
    }
    ```

  - **Get All Namespace Names**: `GET /api/v1/index/{index_name}/namespaces`

    - Response:

    ```json
    ["namespace_1", "namespace_2"]
    ```

  - **Get Namespace Stats**: `GET /api/v1/index/{index_name}/namespace/{namespace_name}/stats`

    - Response:

    ```json
    {
      "dimension": 128,
      "namespaces": {
        "namespace_1": {
          "vector_count": 1000
        }
      }
    }
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
