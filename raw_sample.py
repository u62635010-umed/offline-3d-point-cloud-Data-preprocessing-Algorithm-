class RawSample:
    def __init__(self, timestamp, path_id, sweep_id,
                 half_sweep_id, sample_id,
                 angle_deg, distance,
                 drone_x, drone_y):

        self.timestamp = timestamp
        self.path_id = path_id
        self.sweep_id = sweep_id
        self.half_sweep_id = half_sweep_id
        self.sample_id = sample_id
        self.angle_deg = angle_deg
        self.distance = distance
        self.drone_x = drone_x
        self.drone_y = drone_y
