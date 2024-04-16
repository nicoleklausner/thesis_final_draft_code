import itertools

def calculate_distribution(client_weights, provider_probabilities_choices, client_choices):
    num_features = len(client_weights)
    distributions = {}
    
    # Generate all possible combinations of heads for the coin flips
    head_combinations = list(itertools.product([0, 1], repeat=num_features))
    
    for combination in head_combinations:
        heads_indices = [i for i, value in enumerate(combination) if value == 1]
        distribution_value = sum(client_weights[i] for i in heads_indices)
        probability = 1.0
        
        for i, choice in enumerate(client_choices):
            probability *= provider_probabilities_choices[i][choice] if combination[i] == 1 else (1 - provider_probabilities_choices[i][choice])
            
        if distribution_value in distributions:
            distributions[distribution_value] += probability
        else:
            distributions[distribution_value] = probability
    
    return distributions

# preset feature descriptors, option descriptors, and probabilities
feature_descriptors = ["Gender", "Language"]
option_descriptors = [["Male", "Female"], ["English", "Spanish"]]
provider_probabilities_choices = [[0.5, 0.5], [0.5, 0.5]]  # probabilities for two features and two choices

# user input for client_choices
client_choices = []
for i, descriptor in enumerate(feature_descriptors):
    print(f"For {descriptor}:")
    print("Options:")
    for j, option in enumerate(option_descriptors[i]):
        print(f"{j}: {option}")
    choice = int(input("Enter your choice: "))
    client_choices.append(choice)
    
# user input for client_weights
client_weights = []
for i, descriptor in enumerate(feature_descriptors):
    weight = float(input(f"Rank importance (1-10) of the therapist match accomodating your indicated {descriptor} preference: "))
    client_weights.append(weight)

distribution = calculate_distribution(client_weights, provider_probabilities_choices, client_choices)

print("Distribution for provider:")
for key in sorted(distribution.keys()):
    print(f"* {key}: {distribution[key]}")

# Generate the array representation of the distribution
distribution_array = []
for key, value in distribution.items():
    distribution_array.extend([key] * int(value * 1000))  # Scale probability for better precision

print("\nDistribution for provider (Array representation):")
print(distribution_array)