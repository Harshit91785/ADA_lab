
# Program 5: Fractional Knapsack and Job Scheduling

# ---------- Fractional Knapsack ----------
def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio
    items = []
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0

    # Select items according to their ratio
    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            # Take a fraction of the item
            total_profit += ratio * capacity
            capacity = 0

    return total_profit


# ---------- Job Scheduling ----------
def job_scheduling(jobs):
    # Sort jobs according to profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    # Create empty time slots
    slots = [None] * max_deadline
    total_profit = 0

    # Schedule each job before its deadline
    for job_id, deadline, profit in jobs:
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Remove empty slots
    sequence = [job for job in slots if job is not None]

    return sequence, total_profit


# ---------- Main Program ----------
print("PROGRAM 5")
print("Fractional Knapsack and Job Scheduling")

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

profit = fractional_knapsack(weights, values, capacity)
print("\nFractional Knapsack")
print("Maximum Profit =", profit)

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

sequence, cost = job_scheduling(jobs)

print("\nJob Scheduling")
print("Job Sequence =", sequence)
print("Total Profit =", cost)
