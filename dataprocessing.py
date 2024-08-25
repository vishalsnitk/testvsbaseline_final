



import os
import json
import pandas as pd

def generate_dataframe(folder_path):
    # folder_path = '\download\testvsbaseline\static\test'


    # folder_path = os.path.join(current_directory, folder_path)
    print(folder_path)
    all_data = []
    l = 500  # Starting number for the truncated baseline

    # Create a dictionary to map original baseline names to the new format
    baseline_mapping = {}

    for baseline in os.listdir(folder_path):
        folder_path2 = os.path.join(folder_path, baseline)
        if os.path.isdir(folder_path2):
            for testname in os.listdir(folder_path2):
                folder_path3 = os.path.join(folder_path2, testname)
                if os.path.isdir(folder_path3):
                    cumulative_time = 0
                    for filename in os.listdir(folder_path3):
                        if filename.endswith('.json'):
                            file_path4 = os.path.join(folder_path3, filename)
                            try:
                                with open(file_path4, 'r') as file:
                                    data = json.load(file)
                                    steps = data.get('StepDetails', [])
                                    for step in steps:
                                        timer_state = step.get('TimerState', {})
                                        time_stats = timer_state.get("TimerStats", {})
                                        cumulative_time += time_stats.get("Time (seconds)", 0)
                            except json.JSONDecodeError as e:
                                print(f"Error decoding JSON from file {file_path4}: {e}")

                    # Check if baseline already in mapping
                    # if baseline not in baseline_mapping:
                    #     baseline_mapping[baseline] = f"Assemblies_nx2412.2024071.{l}"
                    #     l += 100  # Increment for the next baseline
                    if baseline not in baseline_mapping:
                        if l < 900:
                            baseline_mapping[baseline] = f"Assemblies_nx2412.2024071.{l}"
                        else:
                            baseline_mapping[baseline] = "Assemblies_nx2412.2024072201"
                        l += 100  
    # Increment for the next baseline
                    # Append data with mapped baseline name
                    all_data.append({
                        'Baseline': baseline_mapping[baseline],
                        'TestName': testname,
                        'CumulativeTime': round(cumulative_time, 2)
                    })

    df = pd.DataFrame(all_data)
    return df

