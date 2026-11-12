from pydantic import BaseModel, Field
from typing import Tuple
from datetime import datetime

class Vector3D(BaseModel):
    x: float
    y: float
    z: float

class Coordinates(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)
    altitude_msl: float

class TelemetryFrame(BaseModel):
    drone_id: str
    sequence_id: int = Field(..., ge=0)
    timestamp_utc_ns: int
    position: Coordinates
    velocity: Vector3D
    signature: str = Field(..., description="Ed25519 signature hex")

class SecurityEvent(BaseModel):
    event_id: str
    timestamp: datetime
    drone_id: str
    violation_type: str
    severity: str
    details: dict
