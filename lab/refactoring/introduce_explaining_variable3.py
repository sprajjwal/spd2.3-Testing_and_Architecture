# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(order):
    if order.desired_state() == 'well-done' and order.time() * order.temperature() * order.pressure() * COOKED_CONSTANT >= WELL_DONE: 
        return True
    if order.desired_state() == 'medium' and order.time() * order.temperature() * order.pressure() * COOKED_CONSTANT >= MEDIUM:
        return True
    return False