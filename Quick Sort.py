
# Quick Sort
#divide-and-conquer
# Worst case: O(n^2)
# Best case: O(n log n)

def partition(A, l, r):
    pivot = l
    p = A[l]  # Choosing the pivot as the first element
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] <= p:
            A[i], A[j] = A[j], A[i]  # Swap if element is less than or equal to pivot
            i += 1
    A[pivot], A[i - 1] = A[i - 1], A[pivot]  # Place the pivot in the correct position
    return i - 1  # Return the index of the pivot

def quick_sort(A, l, r):
    if l >= r:
        return  # Base case: if the sub-array has 0 or 1 element, it's already sorted
    p = partition(A, l, r)  # Partition the array
    quick_sort(A, l, p - 1)  # Recursively sort the left sub-array
    quick_sort(A, p + 1, r)  # Recursively sort the right sub-array

# Example usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)