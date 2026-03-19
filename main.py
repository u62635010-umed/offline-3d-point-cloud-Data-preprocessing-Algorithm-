from csv_reader import read_raw_csv
from data_processor import process
from csv_writer import write_processed_csv
import terrain   # auto-plot after pipeline
import os

BASE_DIR = os.path.dirname(__file__)


def main():
    input_csv = os.path.join(BASE_DIR, "raw_lidar_data.csv")
    output_csv = os.path.join(BASE_DIR, "processed_points.csv")

    raw_samples = read_raw_csv(input_csv)
    processed_points = process(raw_samples)
    write_processed_csv(output_csv, processed_points)

    print("Pipeline complete. Launching 3D terrain plot...")
    terrain.plot(output_csv)

if __name__ == "__main__":
    main()
