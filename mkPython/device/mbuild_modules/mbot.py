from utils.common import num_range_scale
from engine.F0F7.neurons_engine import neurons_request, neurons_blocking_read, neurons_async_read

def run(left_speed, right_speed, index = 1):
    if not isinstance(index, (int, float)):
        return
    if not isinstance(left_speed, (int, float)):
        return

    neurons_request("m_mbot", "run", (left_speed, right_speed), index)
