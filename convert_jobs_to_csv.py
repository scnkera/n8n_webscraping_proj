import pandas as pd
import json

# Load the JSON file
with open('jobs.json', 'r') as f:
    data = json.load(f)

# Filter out only the successful jobs (those with 'url' key)
successful_jobs = [job for job in data if 'url' in job]

# Normalize the data for CSV
df = pd.json_normalize(successful_jobs)

# Save to CSV
df.to_csv('jobs.csv', index=False)

print("Saved", len(successful_jobs), "jobs to jobs.csv")
