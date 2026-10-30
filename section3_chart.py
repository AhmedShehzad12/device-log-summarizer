import json
import matplotlib.pyplot as plt

def generate_chart(json_filepath):
    try:
        with open(json_filepath, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSON file not found. Run Section 2 first.")
        return

    devices = [item['device_id'] for item in data]
    temps = [item['average_temperature'] for item in data]

    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create bars with a nice color
    bars = plt.bar(devices, temps, color='skyblue', edgecolor='black')

    # Formatting fixes (Overcoming the AI bug)
    plt.title("Average Temperature per Device (Filtered < 80°C)", fontsize=14)
    plt.xlabel("Device ID", fontsize=12)
    plt.ylabel("Average Temperature (°C)", fontsize=12)
    
    # FIX: Rotate labels to prevent overlapping
    plt.xticks(rotation=45)
    
    # FIX: Add value labels on top of bars for readability
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 1), ha='center', va='bottom')

    # FIX: Adjust layout so labels aren't cut off
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('temperature_chart.png')
    print("Chart saved as temperature_chart.png")
    plt.show()

if __name__ == "__main__":
    generate_chart("aggregated_output.json")