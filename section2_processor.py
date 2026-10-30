import csv
import json
import os

def process_telemetry(csv_filename, json_filename):
    if not os.path.exists(csv_filename):
        print(f"Error: {csv_filename} not found.")
        return

    # Store raw data grouped by device
    devices_data = {}

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                dev_id = row['device_id']
                status = row['status']
                
                # Handle potential bad data in temperature
                try:
                    temp = float(row['temperature'])
                except ValueError:
                    continue # Skip bad rows

                if dev_id not in devices_data:
                    devices_data[dev_id] = {'temps': [], 'error_count': 0}
                
                devices_data[dev_id]['temps'].append(temp)
                
                if status == 'ERROR':
                    devices_data[dev_id]['error_count'] += 1

    except Exception as e:
        print(f"An error occurred reading the file: {e}")
        return

    # Aggregation & Filtering
    final_results = []
    
    print(f"{'Device ID':<10} | {'Avg Temp':<10} | {'Error Count':<12}")
    print("-" * 40)

    for dev_id, data in devices_data.items():
        total_records = len(data['temps'])
        avg_temp = sum(data['temps']) / total_records if total_records > 0 else 0
        error_count = data['error_count']

        # Filter: Exclude devices with average temp > 80.0
        if avg_temp > 80.0:
            continue

        result = {
            "device_id": dev_id,
            "total_records": total_records,
            "average_temperature": round(avg_temp, 2),
            "error_count": error_count
        }
        final_results.append(result)
        
        # Print summary to terminal
        print(f"{dev_id:<10} | {avg_temp:<10.2f} | {error_count:<12}")

    # Export to JSON
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(final_results, json_file, indent=4)
    
    print(f"\nSuccessfully saved aggregated data to {json_filename}")

if __name__ == "__main__":
    process_telemetry("device_telemetry.csv", "aggregated_output.json")