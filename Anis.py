# A simple Python script to demonstrate the Docker container works.

import time

print("--- Python Application Started ---")
print("Running the application script.")

# For simplicity, we'll just print status updates.
# Will slightly modify the app, so that docker builds a new image and changes its tag from latest to Recording.

for i in range(6):
    print(f"Application Status: Running... (Cycle {i+1})")
    time.sleep(1)

print("--- Python Application Finished ---")
