# kheerganga
Game Server

## Run the Server

### Using Docker (Recommended)

Build and run with Docker Compose:
```bash
docker-compose up --build
```

Or build and run with Docker:
```bash
docker build -t kheerganga .
docker run -p 8000:8000 kheerganga
```

### Without Docker

```bash
uvicorn main:app --reload
```

## Access

The server will be available at: `http://localhost:8000`

WebSocket endpoint: `ws://localhost:8000/ws/{player_id}`