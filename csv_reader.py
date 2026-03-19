import csv
from raw_sample import RawSample

def read_raw_csv(file_path):
    samples = []

    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            samples.append(
                RawSample(
                    timestamp=int(row[0]),
                    path_id=int(row[1]),
                    sweep_id=int(row[2]),
                    half_sweep_id=int(row[3]),
                    sample_id=int(row[4]),
                    angle_deg=float(row[5]),
                    distance=float(row[6]),
                    drone_x=float(row[7]),
                    drone_y=float(row[8])
                )
            )

    return samples
