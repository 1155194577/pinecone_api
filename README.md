# rag

This is the backend of our music search engine.

# How to use 

## Installation

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Running the Server

To start the backend server, use:
```bash
python app.py
```

## API Endpoints

- `GET /search`: Search for music tracks.
- `POST /add`: Add a new music track.

## Configuration

Ensure you have the correct environment variables set up in a `.env` file:
```
API_KEY=your_api_key
DATABASE_URL=your_database_url
```

## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.