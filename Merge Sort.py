# Merge Sort
# O(n log n)
def merge(lst1, lst2):
    merged_lst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged_lst.append(lst1[i])
            i += 1
        else:
            merged_lst.append(lst2[j])
            j += 1

    # Add any remaining elements from both lists
    merged_lst.extend(lst1[i:])
    merged_lst.extend(lst2[j:])

    return merged_lst

def merge_sort(lst):
    if len(lst) < 2: 
        return lst
    m = len(lst) // 2
    part1 = merge_sort(lst[:m]) 
    part2 = merge_sort(lst[m:])

    return merge(part1, part2)

# Example usage:
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_list)
    print("Sorted List:", sorted_list)
