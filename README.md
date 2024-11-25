# Common problem
  File "/workspaces/pinecone_api/backend/./app/main.py", line 1, in <module>
    from app.api.api import app
ModuleNotFoundError: No module named 'app'

type in terminal : export PYTHONPATH=/workspaces/pinecone_api/backend

File "/workspaces/pinecone_api/backend/venv/lib/python3.12/site-packages/pinecone/config/config.py", line 56, in build
    raise PineconeConfigurationError("You haven't specified an Api-Key.")
pinecone.exceptions.exceptions.PineconeConfigurationError: You haven't specified an Api-Key.

export PINECONE_API_KEY=your_pinecone_api_key
export NAMESPACE_NAME=your_namespace 

 File "/workspaces/pinecone_api/backend/app/main.py", line 7, in <module>
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT")) or 8000,reload=True)
                                                 ^^^^^^^^^^^^^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

export PORT=5000