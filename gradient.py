import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# B4: Gradient Descent to find local minimum of y = (x + 3)^2
# Starting at x = 2
# =====================================================

# 1. Objective function and its derivative
def cost_function(x):
    return (x + 3) ** 2

def gradient(x):
    return 2 * (x + 3)

# 2. Hyperparameters
cur_x = 2.0           # Starting point specified in the problem statement
learning_rate = 0.1   # Step size (alpha)
precision = 0.000001  # Tolerance to stop the loop
max_iters = 1000      # Maximum iterations to prevent infinite loop
previous_step_size = 1.0
iters = 0

# Lists to track history for plotting
x_history = [cur_x]
y_history = [cost_function(cur_x)]

# 3. Gradient Descent Loop
while previous_step_size > precision and iters < max_iters:
    prev_x = cur_x
    grad = gradient(prev_x)
    
    # Gradient Descent update rule: x_new = x_old - alpha * dy/dx
    cur_x = cur_x - learning_rate * grad
    
    previous_step_size = abs(cur_x - prev_x)
    iters += 1
    
    x_history.append(cur_x)
    y_history.append(cost_function(cur_x))
    
    print(f"Iteration {iters:3d}: x = {cur_x:10.6f}, y = {cost_function(cur_x):10.6f}")

print("\n--- Results ---")
print(f"Local minimum occurs at x = {cur_x:.6f}")
print(f"Minimum value of y = {cost_function(cur_x):.6f}")
print(f"Total iterations: {iters}")

# 4. Optional: Plot the convergence curve
x_vals = np.linspace(-6, 3, 200)
y_vals = cost_function(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="y = (x + 3)^2", color="blue")
plt.plot(x_history, y_history, "ro-", label="Gradient Descent Steps")
plt.title("Gradient Descent Optimization")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

