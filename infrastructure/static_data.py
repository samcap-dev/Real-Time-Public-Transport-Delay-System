import zipfile
import os
import pandas as pd

# Paths
zip_path = "/home/sam-sunny/Projects/Real-Time-Public-Transport-Delay-System/data/MBTA_GTFS.zip"
extract_path = "/home/sam-sunny/Projects/Real-Time-Public-Transport-Delay-System/data/MBTA_GTFS"
output_folder = "/home/sam-sunny/Projects/Real-Time-Public-Transport-Delay-System/data/cleaned"

# Create folders if not exists
os.makedirs(extract_path, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Extract files
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

print("Files extracted:", os.listdir(extract_path))

# Load CSVs
routes_df = pd.read_csv(os.path.join(extract_path, "routes.txt"))
trips_df = pd.read_csv(os.path.join(extract_path, "trips.txt"))
stops_df = pd.read_csv(os.path.join(extract_path, "stops.txt"))
stop_times_df = pd.read_csv(os.path.join(extract_path, "stop_times.txt"))

# --- Cleaning functions ---
def clean_stops(df):
    df = df.drop_duplicates(subset=['stop_id'])
    df['stop_name'] = df['stop_name'].fillna('Unknown Stop')
    df['stop_id'] = df['stop_id'].astype(str)
    return df

def clean_routes(df):
    df = df.drop_duplicates(subset=['route_id'])
    df['route_long_name'] = df['route_long_name'].fillna('Unknown Route')
    df['route_id'] = df['route_id'].astype(str)
    return df

def clean_trips(df):
    df = df.drop_duplicates()
    df['service_id'] = df['service_id'].astype(str)
    return df

def clean_stop_times(df):
    df = df.drop_duplicates()
    df['trip_id'] = df['trip_id'].astype(str)
    return df

# --- Apply cleaning ---
cleaned_stops_df = clean_stops(stops_df)
cleaned_routes_df = clean_routes(routes_df)
cleaned_trips_df = clean_trips(trips_df)
cleaned_stop_times_df = clean_stop_times(stop_times_df)

# --- Save cleaned outputs ---
cleaned_stops_df.to_csv(os.path.join(output_folder, "stops_cleaned.csv"), index=False)
cleaned_routes_df.to_csv(os.path.join(output_folder, "routes_cleaned.csv"), index=False)
cleaned_trips_df.to_csv(os.path.join(output_folder, "trips_cleaned.csv"), index=False)
cleaned_stop_times_df.to_csv(os.path.join(output_folder, "stop_times_cleaned.csv"), index=False)

print("✅ All cleaned files saved in:", output_folder)
