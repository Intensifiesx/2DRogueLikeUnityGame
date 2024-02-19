def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Boolean flag to track if any swaps are made in a pass
    swapped = True
    
    # Continue iterating until no swaps are performed in a pass
    while swapped:
        swapped = False
        
        # Iterate over the array
        for i in range(1, n):
            # Compare adjacent elements and swap if necessary
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                
                # Set the swapped flag to True indicating a swap occurred
                swapped = True
        
        # Reduce the range of iteration as the largest element gets bubbled up
        n -= 1
    
    # Return the sorted array
    return arr

if __name__ == "__main__":
    # Test the algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(test_array)
    print("Sorted array is:", sorted_array)
