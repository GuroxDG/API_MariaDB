from fastapi import FastAPI
from routes.timeseries_routes import user
import uvicorn

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
)
app.include_router(user)

# if __name__ == '__main__':
#     uvicorn.run('app:app', host='127.0.0.1 ', port=8000, reload=True)