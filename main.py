import uvicorn

from core.config import config

if __name__ == "__main__":
    print("heisenberg DB")
    server_config = uvicorn.Config(
        app="core.server:app",
        host="localhost",
        port=5000,
        reload=False if config.ENVIRONMENT == "production" else True,
        workers=1,
    )
    server = uvicorn.Server(config=server_config)
    server.run()