# A simple Python script to demonstrate the Docker container works.

import time

print("--- Python Application Started ---")
print("Running the application script.")

# For simplicity, we'll just print status updates.

for i in range(5):
    print(f"Application Status: Running... (Cycle {i+1})")
    time.sleep(1)

print("--- Python Application Finished ---")
