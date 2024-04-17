# thesis_final_draft_code

## PBMA.py

### Summary

The provided code implements the Pandora's Box algorithm, a method for optimizing therapist selection based on the distribution of rewards (session durations) and associated costs (appointment fees). This algorithm employs a binary search technique to determine the reservation value for each therapist, then strategically selects therapists based on their reservation values and the distribution of rewards.

---

### Detailed Explanation

1. **`calc_reservation_value(D_i, c_i)`:**
    - **Input:** 
        - `D_i`: List representing the distribution of rewards for a specific therapist.
        - `c_i`: The associated cost (appointment fee) for the therapist.
    - **Output:** 
        - `r`: The calculated reservation value for the therapist.
    - This function calculates the reservation value for a given therapist, represented by the parameters `D_i` and `c_i`. It employs a binary search method to iteratively narrow down the reservation value within a specified range until convergence.

2. **`solve_pandoras_box(D, c)`:**
    - **Input:** 
        - `D`: List of lists, where each inner list represents the distribution of rewards for a therapist.
        - `c`: List of associated costs for each therapist.
    - **Output:** 
        - `considered_therapists`: List of tuples representing the selected therapists, their rewards, and appointment types.
    - This function implements the Pandora's Box algorithm to select therapists based on their reservation values and the distribution of rewards and costs.
    - It initializes variables and structures necessary for the algorithm.
    - For each therapist, it calculates the reservation value using `calc_reservation_value()`.
    - It then sorts therapists based on their reservation values in descending order.
    - Using the sorted list of therapists, it iteratively selects therapists until a stopping condition is met. Therapists are chosen based on whether their reservation values exceed the largest revealed reward.
    - The algorithm also ensures that therapists are not chosen if they have already been selected for the opposite type of appointment (5 min consultation vs. 1 hour appointment).

3. **Example Test:**
    - The code includes an example test scenario with multiple therapists, each with distinct distributions of rewards and costs.
    - **Input:** 
        - Distributions of rewards (`D`) and associated costs (`c`) for each therapist.
    - **Output:** 
        - List of selected therapists along with their rewards.
    - It prints out the opened therapists along with their rewards, demonstrating the selection process.

---

### Usage

To use the Pandora's Box algorithm for therapist selection, follow these steps:
1. Define the distributions of rewards (`D`) and associated costs (`c`) for each therapist.
2. Call the `solve_pandoras_box()` function with the distributions and costs as arguments.
3. The function will return a list of selected therapists along with their rewards.

Example:
```python
distributions = [...]  # List of reward distributions for each therapist
costs = [...]          # List of associated costs for each therapist

selected_therapists = solve_pandoras_box(distributions, costs)
print("Selected Therapists:", selected_therapists)

