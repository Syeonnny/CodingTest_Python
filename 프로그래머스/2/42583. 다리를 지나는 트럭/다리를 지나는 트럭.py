from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    current_weight = 0
    
    while truck or sum(bridge) > 0:
        time += 1
        current_weight -= bridge.popleft()
        
        if truck and current_weight + truck[0] <= weight:
            t = truck.popleft()
            bridge.append(t)
            current_weight += t
        else:
            bridge.append(0)
    return time