from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse
from src.services.ComputrabajoWebScrapingService import (
    ComputrabajoWebScrapingService as Scraper,
)

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])


@router.get(
    path="",
    summary="Obtener ofertas de Trabajo",
)
async def get_ofertas(
    job_title: str = Query(min_length=4),
    location: str = Query(min_length=4),
    page: int = Query(default=1, ge=1),
):
    scraper = Scraper()
    try:
        ofertas = scraper.get_job_offers(job_title, location, page)
        if not ofertas:
            raise HTTPException(status_code=404, detail="No se encontraron ofertas")
        return JSONResponse(
            content=ofertas, status_code=200, media_type="application/json"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
