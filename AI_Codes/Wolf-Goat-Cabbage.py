# Define the initial and goal states
initial_state = ("left", {"wolf", "goat", "cabbage", "farmer"}, set())
goal_state = ("right", set(), {"wolf", "goat", "cabbage", "farmer"})

# Function to solve the WGC problem with boat constraints
def wgc(boat_position, left_bank, right_bank, path=[]):
    # If goal state is reached, print the solution path
    if (boat_position, left_bank, right_bank) == goal_state:
        for step in path:
            print(step)
        return True

    # Possible items that the farmer can take with him in the boat (only one at a time)
    items_to_take = [None, "wolf", "goat", "cabbage"]

    for item in items_to_take:
        # Determine the new state after moving the farmer and possibly one item
        if boat_position == "left":
            new_boat_position = "right"
            new_left_bank = left_bank - {"farmer", item} if item else left_bank - {"farmer"}
            new_right_bank = right_bank | {"farmer", item} if item else right_bank | {"farmer"}
        else:
            new_boat_position = "left"
            new_left_bank = left_bank | {"farmer", item} if item else left_bank | {"farmer"}
            new_right_bank = right_bank - {"farmer", item} if item else right_bank - {"farmer"}

        # Check safety conditions:
        # 1. Wolf and goat cannot be left together
        # 2. Goat and cabbage cannot be left together
        if "goat" in new_left_bank and "wolf" in new_left_bank and "farmer" not in new_left_bank:
            continue  # Unsafe: wolf and goat left together on left bank
        if "goat" in new_left_bank and "cabbage" in new_left_bank and "farmer" not in new_left_bank:
            continue  # Unsafe: goat and cabbage left together on left bank
        if "goat" in new_right_bank and "wolf" in new_right_bank and "farmer" not in new_right_bank:
            continue  # Unsafe: wolf and goat left together on right bank
        if "goat" in new_right_bank and "cabbage" in new_right_bank and "farmer" not in new_right_bank:
            continue  # Unsafe: goat and cabbage left together on right bank

        # Avoid revisiting states by storing them in path
        new_state = (new_boat_position, frozenset(new_left_bank), frozenset(new_right_bank))
        if new_state in path:
            continue  # Skip already visited states to avoid cycles

        # Recursive call with the new state
        if wgc(new_boat_position, new_left_bank, new_right_bank, path + [(new_boat_position, new_left_bank, new_right_bank)]):
            return True

    return False  # No solution found

# Start solving the problem from the initial state
print("Solution steps:")
wgc("left", {"wolf", "goat", "cabbage", "farmer"}, set())
