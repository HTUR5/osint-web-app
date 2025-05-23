from fastapi import APIRouter
from app.models.schema import ScanRequest, ScanResult
from app.services.scanner import run_all_scans

router = APIRouter()

@router.post(
    "/scan",
    response_model=ScanResult,
    tags=["סריקות"],
    summary="הרצת סריקה",
    description="מריץ את כלי ה־OSINT על דומיין ומחזיר תוצאות"
)
async def scan(request: ScanRequest):
    return run_all_scans(request.domain)


