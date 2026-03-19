import csv

def write_processed_csv(file_path, points):
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "z"])

        for p in points:
            writer.writerow([
                f"{p.x:.3f}",
                f"{p.y:.3f}",
                f"{p.z:.3f}"
            ])
