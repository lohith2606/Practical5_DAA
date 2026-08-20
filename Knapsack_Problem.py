def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming (Tabulation).
    
    :param weights: List of weights of the items
    :param values: List of values/profits of the items
    :param capacity: Maximum weight capacity of the knapsack
    :return: Tuple containing (Max Value, List of selected item indices)
    """
    n = len(weights)
    
    # Step 1: Initialize the DP table with zeros
    # Rows: 0 to n items, Columns: 0 to capacity weight
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Step 2: Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item's weight is less than or equal to current capacity
            if weights[i - 1] <= w:
                # Max of including the item vs excluding the item
                dp[i][w] = max(
                    dp[i - 1][w], 
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                # Exclude the item if it's too heavy
                dp[i][w] = dp[i - 1][w]
                
    # The bottom-right cell contains the maximum value
    max_value = dp[n][capacity]
    
    # Step 3: Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the value changed, it means the item was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Store 0-based index
            w -= weights[i - 1]           # Reduce remaining capacity
            
    # Reverse to keep chronological order of selected items
    selected_items.reverse()
    
    return max_value, selected_items

# --- Example Usage ---
if __name__ == "__main__":
    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    knapsack_capacity = 50

    max_val, items = knapsack_01(item_weights, item_values, knapsack_capacity)
    
    print(f"Maximum Value in Knapsack: {max_val}")
    print(f"Selected Item Indices: {items}")
