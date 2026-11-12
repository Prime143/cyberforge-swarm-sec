import logging
from contracts.telemetry_frame import TelemetryFrame

logger = logging.getLogger(__name__)

class KinematicFilter:
    def __init__(self, max_velocity_mps: float = 35.0, max_descent_mps: float = 8.0):
        self.max_velocity = max_velocity_mps
        self.max_descent = max_descent_mps
        # TODO (Tejal): Implement state tracking (cache) for previous frames to calculate Delta V
        self.state_cache = {}

    def evaluate_kinematics(self, frame: TelemetryFrame) -> bool:
        """
        TODO (Tejal): Implement physics sanity checks.
        
        1. Calculate delta velocity from the last known frame for this drone_id in self.state_cache.
        2. Reject if delta V exceeds self.max_velocity.
        3. Reject if vertical descent exceeds self.max_descent.
        """
        logger.debug(f"Evaluating kinematics for {frame.drone_id}")
        
        # Candidate Implementation Required
        raise NotImplementedError("Kinematic anomaly engine is not yet implemented.")
