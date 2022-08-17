"""Compose main app from routers."""

from fastapi import FastAPI

from app.routers import hello

app = FastAPI(title='TemplateAPI', version='1.0.0')

app.include_router(hello.router)
