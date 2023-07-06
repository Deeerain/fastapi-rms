from fastapi import FastAPI

import leads
import customers

app = FastAPI(title='RMS')
app.include_router(leads.router)
app.include_router(customers.router)