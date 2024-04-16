import numpy as np

###############
def calc_reservation_value(D_i, c_i): # uses binary search to find reservation value 
    # lower and upper bounds
    lower_bound = 0
    upper_bound = max(D_i)
    
    while lower_bound < upper_bound:
        # initialize r 
        r = (lower_bound + upper_bound) / 2
        
        t = sum(max(x - r, 0) for x in D_i) / len(D_i)

        if abs(upper_bound - lower_bound) < 1e-10:  # Terminate if the bounds are very close
            return (lower_bound + upper_bound) / 2
        
        if t > c_i:
            # If t is too high, update the upper bound
            lower_bound = r
        elif t < c_i:
            # If t is too low, update the lower bound
            upper_bound = r
        else:
            # If t matches c_i, we've found the reservation value
            return r
    
    # Return the midpoint as the approximation if exact match not found
    return (lower_bound + upper_bound) / 2
###############

def solve_pandoras_box(D, c):
    reservation_values = []
    types = ["5 min consultation", "1 hour appointment"] * (len(D) // 2)  # Alternating types
    index_count = 0  # only change index (therapist #) after every alteration 
    chosen_therapists = set()  # Keep track of therapists already chosen
    
    # calculate reservation values for D, c using binary search 
    for i, (D_i, c_i, type_i) in enumerate(zip(D, c, types)):
        reservation_value_i = calc_reservation_value(D_i, c_i)
        reservation_values.append((index_count + 1, reservation_value_i, type_i))
        if i % 2 == 1:
            index_count += 1
    print("--------------------")
    print("RESERVATION VALUES:", reservation_values)
    print("--------------------")

    # sort boxes according to reservation value
    sorted_reservations = sorted(reservation_values, key=lambda x: x[1], reverse=True)
    print("SORTED RESERVATION VALUES:", sorted_reservations)
    print("--------------------")

    considered_therapists = []  # Array to keep track of opened boxes
    
    largest_reward = None  # Initialize largest revealed reward
    chosen_therapists_by_type = {'5 min consultation': set(), '1 hour appointment': set()}  # Keep track of chosen therapists by type
    
    print("Now, using the calculated reservation values, run PBMA for choosing a therapist:")
    print()
    # Open boxes in sorted order until the condition is met
    for therapist_num, reservation_value, box_type in sorted_reservations:
        # Check if therapist has already been chosen for the opposite type
        if therapist_num in chosen_therapists_by_type["5 min consultation"] and box_type == "1 hour appointment":
            continue
        elif therapist_num in chosen_therapists_by_type["1 hour appointment"] and box_type == "5 min consultation":
            continue
        
        # Randomly select a reward from the distribution
        selected_reward = np.random.choice(D[therapist_num-1])
        
        # Open the box and add it to the considered therapists
        considered_therapists.append((therapist_num, selected_reward, box_type))
        
        # Update chosen therapists by type
        chosen_therapists_by_type[box_type].add(therapist_num)

        # Print which box is being opened alongside the reward
        print(f"Opened therapist {therapist_num} ({box_type}), with reward {selected_reward}")
        
        # Update the largest revealed reward
        largest_reward = selected_reward if largest_reward is None else max(largest_reward, selected_reward)
        print("largest reward thus far = ", largest_reward)
        print("--")

        
        # Check if the largest revealed reward exceeds the reservation value of the current box
        if largest_reward > reservation_value:
            break

    return considered_therapists

# EXAMPLE TEST

# === THERAPIST 1 ===

# 5 min consultation distribution 
D_1 = [55, 100]
c_1 = 15

# 1 hour appointment distribution 
D_2 = [0, 0, 0, 0, 0, 0, 0, 0, 240, 240]
c_2 = 20

# === THERAPIST 2 ===

# 5 min consultation distribution 
D_3 = [55, 100]
c_3 = 16

# 1 hour appointment distribution 
D_4 = [0, 0, 0, 0, 0, 0, 0, 0, 240, 240]
c_4 = 45

# === THERAPIST 3 ===

# 5 min consultation distribution 
D_3 = [60, 90, 100]
c_3 = 16

# 1 hour appointment distribution 
D_4 = [20, 20, 20, 20, 20, 20, 20, 20, 200, 200, 50, 50]
c_4 = 45

# === THERAPIST 4 ===

# 5 min consultation distribution 
D_5 = [50, 110]
c_5 = 16

# 1 hour appointment distribution 
D_6 = [10, 10, 10, 10, 10, 10, 10, 10, 250, 250, 3, 3]
c_6 = 45

distributions = [D_1, D_2, D_3, D_4, D_5, D_6]
costs = [c_1, c_2, c_3, c_4, c_5, c_6]


print("all opened boxes and associated rewards (last tuple being the claimed box) = ", solve_pandoras_box(distributions, costs))
