import math
from point3d import Point3D

DRONE_ALTITUDE = 3.0

def process(raw_samples):
    points = []

    for s in raw_samples:

        # --- Basic filtering ---
        if s.distance <= 2.5 or s.distance > 3.5:
            continue
        if abs(s.angle_deg) > 15:
            continue

        # --- Normalize zig-zag ---
        angle = s.angle_deg
        if s.half_sweep_id == 1:
            angle = -angle

        # --- Polar → Cartesian ---
        theta = math.radians(angle)

        x = s.distance * math.sin(theta)
        z = DRONE_ALTITUDE - (s.distance * math.cos(theta))
        y = s.drone_y

        points.append(Point3D(x, y, z))

    smooth_z(points)
    return points


def smooth_z(points):
    for i in range(1, len(points) - 1):
        points[i].z = (
            points[i - 1].z +
            points[i].z +
            points[i + 1].z
        ) / 3.0
