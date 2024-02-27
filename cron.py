import schedule
import time
from simulate import send, check_env

# Store
store = {}

def update_store(key, value):
	store[key] = value
	
def get_store(key):
	return store[key]

def job():
		print("New event")
		check_env()

		battery_level = get_store('battery_level')
		occupancy = get_store('occupancy')
		
		battery_level, occupancy = send(old_battery_level=battery_level, old_occupancy=occupancy)
		update_store('battery_level', battery_level)
		update_store('occupancy', occupancy)

		print(f"Updated battery level: {battery_level}")
		print(f"Updated occupancy: {occupancy}")
		
		
if __name__ == '__main__':
		# Initialize the store
		update_store('battery_level', 1.0)
		update_store('occupancy', False)
		
		# Schedule the job
		schedule.every(1).minutes.do(job)

		# Run the job
		while True:
			schedule.run_pending()
			time.sleep(1)
			
