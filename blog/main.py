from fastapi import FastAPI
from . import models
from .database import engine
from .router import authentication,blog, user 

tags_metadata = [
    {
        "name": "Blogs",
        "description": "Manage blogs. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
]


app = FastAPI(openapi_tags=tags_metadata)


models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
