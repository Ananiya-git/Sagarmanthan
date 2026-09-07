"""
SagarManthan API — Intelligent Freight Forecasting & Vessel Chartering Decision Platform
SIH 2026 — Problem Statement SIH26006
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(
    title="SagarManthan API",
    description="Intelligent Freight Forecasting Model for Optimized Vessel Chartering and Bulk Cargo Procurement — East Coast of India (SIH26006)",
    version="1.0.0-sih2026",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
def root():
    if FRONTEND_DIR.exists():
        return FileResponse(FRONTEND_DIR / "index.html")
    return {
        "name": "SagarManthan",
        "tagline": "From Reactive Spot Chartering to Predictive Multi-Voyage Intelligence",
        "problem": "SIH26006",
        "organization": "Ministry of Steel / SAIL",
        "docs": "/docs",
    }