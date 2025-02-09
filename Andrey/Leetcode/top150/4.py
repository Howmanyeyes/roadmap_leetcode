import time
import os

def clear_screen():
    # Clears the terminal screen for a smoother animation
    pass
    #os.system('cls' if os.name == 'nt' else 'clear')

def print_state(nums, slow, fast, count, message=""):
    """
    Prints the current state of the array along with indices,
    and marks the positions of the slow and fast pointers.
    """
    # Build the header for indices.
    idx_line = "Indices:  " + " ".join(f"{i:^5}" for i in range(len(nums)))
    
    # Build the array line.
    array_line = "Array:    " + " ".join(f"{num:^5}" for num in nums)
    
    # Build the pointer line.
    pointer_line = "Pointers:"
    for i in range(len(nums)):
        marker = "      "  # 5 spaces to match the cell width
        if i == slow and i == fast:
            marker = "  SF  "
        elif i == slow:
            marker = "  S   "
        elif i == fast:
            marker = "  F  "
        pointer_line += marker

    # Print the message, array state, and current count.
    print(message)
    print(idx_line)
    print(array_line)
    print(pointer_line)
    print(f"Current count: {count}\n")
    time.sleep(1)  # Pause so you can follow along

def removeDuplicates_visualize(nums):
    """
    Removes duplicates from a sorted array so that each element
    appears at most twice. Visualizes each step of the algorithm.
    """
    slow = fast = 1
    count = 1

    clear_screen()
    print_state(nums, slow, fast, count, "Initial state:")

    while fast < len(nums):
        # Show what we are about to compare.
        clear_screen()
        message = f"Comparing nums[{fast}] ({nums[fast]}) with nums[{fast - 1}] ({nums[fast - 1]})"
        print_state(nums, slow, fast, count, message)

        if nums[fast] == nums[fast - 1]:
            count += 1
            if count > 2:
                # Extra duplicate detected; skip copying.
                clear_screen()
                message = (f"Duplicate count ({count}) > 2 at index {fast} (value: {nums[fast]}).\n"
                           "Skipping this element.")
                print_state(nums, slow, fast, count, message)
                fast += 1
                continue
        else:
            # New number encountered; reset count.
            count = 1

        # Copy the valid element to the 'slow' pointer location.
        clear_screen()
        message = (f"Copying value from index {fast} ({nums[fast]}) to index {slow}.\n"
                   f"count = {count} (allowed duplicate or new element).")
        nums[slow] = nums[fast]
        print_state(nums, slow, fast, count, message)
        
        # Move both pointers forward.
        slow += 1
        fast += 1

    clear_screen()
    final_message = f"Finished processing. New length is {slow}."
    print_state(nums, slow, fast, count, final_message)
    return slow

if __name__ == "__main__":
    # Example input: three 1's, two 2's, one 3.
    nums = [0,0,1,1,1,1,2,3,3]
    new_length = removeDuplicates_visualize(nums)
    
    # Show the resulting array (only the first new_length elements are valid)
    print(f"New length of array: {new_length}")
    print("Resulting array:", nums[:new_length])
