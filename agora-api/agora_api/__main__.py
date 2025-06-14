import uvicorn
from agora_api.database.db import Base, engine
from agora_api.database import models # Import models to ensure they are registered with Base.metadata

if __name__ == "__main__":
    uvicorn.run("agora_api:app", host="0.0.0.0", port=8000, reload=True)
