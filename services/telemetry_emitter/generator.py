import time
import uuid
import logging
from contracts.telemetry_frame import TelemetryFrame, Coordinates, Vector3D

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_mock_telemetry(drone_id: str, seq_id: int) -> TelemetryFrame:
    """
    TODO (Urvi): Expand this generator to simulate realistic flight paths.
    Currently emits static hovering coordinates. You must implement waypoint transitions.
    """
    return TelemetryFrame(
        drone_id=drone_id,
        sequence_id=seq_id,
        timestamp_utc_ns=int(time.time() * 1e9),
        position=Coordinates(latitude=18.5204, longitude=73.8567, altitude_msl=120.5),
        velocity=Vector3D(x=0.0, y=0.0, z=0.0),
        signature="UNINITIALIZED_TEST_SIGNATURE" # To be signed by local test key later
    )

if __name__ == "__main__":
    print("Swarm-Sec Telemetry Emitter initializing...")
    test_drone = str(uuid.uuid4())
    seq = 0
    
    while True:
        frame = generate_mock_telemetry(test_drone, seq)
        logger.info(f"Emitting: {frame.drone_id} | Seq: {frame.sequence_id} | Alt: {frame.position.altitude_msl}m")
        seq += 1
        time.sleep(1) # 1 Hz emission rate
