from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CCTV_Frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Optional[tuple[float, float]] = (0.0, 0.0)