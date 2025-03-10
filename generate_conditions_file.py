from pathlib import Path
import csv

# Set the folder you want to process
folder_path = Path('Stimuli')  # Change '.' to your specific folder if needed

# Find all .wav files in the folder
wav_files = folder_path.glob("*.wav")

# Define the output CSV file and the headers
output_csv = "low_frequency_conditions.csv"
headers = ["path", "file_type", "SNR", "frequency", "angle", "channel", "location_condition"]

with open(output_csv, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    
    # Process each wav file
    for file in wav_files:
        rel_path = file.relative_to("./")
        parts = file.stem.split('.')
        
        # Check if the filename splits into exactly 5 parts (as expected)
        if len(parts) == 5:
            file_type, snr, frequency, angle, channel = parts
            
            # Determine the location_condition based on channel and angle.
            # Assumes angle is "30" or "90" and channel indicates left/right.
            if channel.lower().startswith('l'):
                location_condition = f"LEFT{angle}"
            elif channel.lower().startswith('r'):
                location_condition = f"RIGHT{angle}"
            else:
                location_condition = "Unknown"
            
            writer.writerow([str(rel_path), file_type, snr, frequency, angle, channel, location_condition])
        else:
            # Optionally, handle files that do not match the expected pattern.
            print(f"Skipping file with unexpected format: {file.name}")

print(f"CSV file '{output_csv}' created successfully.")
