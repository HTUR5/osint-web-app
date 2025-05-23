# app/models/schema.py

from pydantic import BaseModel
from typing import List

class ScanRequest(BaseModel):
    domain: str

class ScanResult(BaseModel):
    subdomains: List[str] = []
    emails: List[str] = []
    ips: List[str] = []
