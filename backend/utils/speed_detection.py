import time

def calculate_speed(vehicle_position_a, vehicle_position_b, time_diff):
    # Use the real-world distance between A and B (in meters)
    distance = 50  # meters (example)
    
    # Calculate speed in m/s, convert to km/h
    speed = (distance / time_diff) * 3.6
    return speed
