from functools import lru_cache

input_file = input"

devices = dict()
with open(input_file, "r") as f:
    for line in f:
        split = line.strip().split(":")
        devices[split[0]] = split[1].split()

print(devices)


def update_state(state, visited_states):
    if state == "out" or state in visited_states:
        if "dac" in visited_states and "fft" in visited_states:
            return 1
        else:
            return 0

    visited_states.add(state)
    result = 0
    for s in devices[state]:
        result += update_state(s, visited_states.copy())

    return result


total = update_state("svr", set())

print(total)
