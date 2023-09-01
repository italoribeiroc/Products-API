from fastapi import FastAPI
from .import models
from .database import engine
from .database import get_db
from .routers import product, seller, login

app = FastAPI(
    title="Products API",
    description="Get details for all the products on our website",
    terms_of_service="http://www.google.com",
    developer_contact={
        "name": "Italo Ribeiro",
        "website": "http://www.google.com",
        "email": "italo@example.com",
    },
    license_info={
        "name": "XYZ",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)
models.Base.metadata.create_all(engine)
    

