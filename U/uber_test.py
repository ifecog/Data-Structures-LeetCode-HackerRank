from collections import Counter, defaultdict, deque


def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    length = len(beginWord)
    
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(length):
            pattern = word[:i] + '*' + word[i+1:]
            all_combo_dict[pattern].append(word)

    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(length):
            pattern = current_word[:i] + '*' + current_word[i+1:]
            
            for neighbor in all_combo_dict[pattern]:
                if neighbor == endWord:
                    return level + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                    
            all_combo_dict[pattern] = []
    
    return 0

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))

# def max_sum(arr):
#     n = len(arr)
    
#     s0 = sum(i * arr[i] for i in range(n))
#     total_sum = sum(arr)
    
#     max_sum_val = s0
#     current_sum = s0
    
#     for i in range(1, n):
#         current_sum = current_sum + total_sum - (n * arr[n - 1])
#         max_sum_val = max(max_sum_val, current_sum)
    
#     return max_sum_val

# # Example usage:
# arr = [8, 3, 1, 2]
# print(max_sum(arr))
    

# def check_subarray_sum(nums, k):
#     prefix_mod = {0: -1}
#     current_sum = 0
    
#     for i, num in enumerate(nums):
#         current_sum += num
        
#         if k != 0:
#             current_sum %= k
            
#         if current_sum in prefix_mod:
#             if i - prefix_mod[current_sum] >= 2:
#                 return True
        
#         else:
#             prefix_mod[current_sum] = i
            
#     return False
    

# def subarray_sum(nums, k):
#     prefix_sums = {0: 1}
#     current_sum = 0
#     count = 0
    
#     for num in nums:
#         current_sum += num
        
#         complement = current_sum - k
        
#         if complement in prefix_sums:
#             count += prefix_sums[complement]
        
#         if current_sum in prefix_sums:
#             prefix_sums[current_sum] += 1
#         else:
#             prefix_sums[current_sum] = 1
    
#     return count
    

# def mini_subarray_length(nums, target):
#     left = 0
#     current_sum = 0
#     min_length = len(nums) + 1
    
#     for right, num in enumerate(nums):
#         current_sum += num
        
#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
            
#             current_sum -= nums[left]
#             left += 1
    
#     return min_length if min_length <= len(nums) else 0


# def taskSchedulerII(tasks, space):
#     last_done = {}
#     day = 0
    
#     for task in tasks:
#         day += 1
        
#         if task in last_done:
#             min_available_day = last_done[day] + space + 1
            
#             if day < min_available_day:
#                 day = min_available_day
                
#         last_done[task] = day
    
#     return day
    


# def leastInterval(tasks, n):
#     task_counts = Counter(tasks)
#     max_freq = max(task_counts.values())
#     max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)
    
#     return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)    

#     # Example usage:
# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2
# print("Minimum CPU intervals:", leastInterval(tasks, n))


# def first_non_repeating(nums):
#     freq = {}
    
#     for num in nums:
#         freq[num] = freq.get(num, 0) + 1
    
#     for i, num in enumerate(nums):
#         if freq[num] == 1:
#             return num
    
#     return -1

# # Example usage
# arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
# print(first_non_repeating(arr)) 


# def merge2_arrays(nums1, m, nums2, n):
#     nums1 += [0] * n
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
            
#         p_merged -= 1
        
#     if p2 >= 0:
#         nums1[:p2 + 1] = nums2[:p2 + 1]
        
#     return nums1

# # Example usage:
# nums1 = [1, 2, 3, 4, 4, 5]
# m = 6
# nums2 = [2, 5, 6]
# n = 3

# merge2_arrays(nums1, m, nums2, n)
# print(nums1)


# def merge_arrays(nums1, m, nums2, n):
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >=0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
            
#         p_merged -= 1
        
#     nums1[:p2 + 1] = nums2[:p2 + 1]
    
#     return nums1

# # Example usage:
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)


# # Minimum subarray length
# def min_subarray_length(nums, target):
#     left = 0
#     current_sum = 0
#     min_length = len(nums) + 1
    
#     for right, num in enumerate(nums):
#         current_sum += num
        
#         while current_sum >= target:
#              min_length = min(min_length, right - left + 1)
             
#              current_sum -= nums[left]
#              left += 1
             
#     return min_length if min_length <= len(nums) else 0   
    
    # n = len(nums)
    # min_length = n + 1
    
    # for i in range(n):
    #     current_sum = 0
        
    #     for j in range(i, n):
    #         current_sum += nums[j]
            
    #         if current_sum >= target:
    #             min_length = min(min_length, j - i + 1)
    #             break
            
    # return min_length if min_length <= len(nums) else 0

# # Example usage
# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# result = min_subarray_length(nums, target)
# print(result) 

    


# # Two Sum
# def two_sum(nums, target):
#     hash_map = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in hash_map:
#             return [hash_map[complement], i]
        
#         hash_map[num] = i

#     return []

# # Example usage:
# nums = [2, 7, 6, 5]
# target = 9
# result = two_sum(nums, target)
# print(result)

# # Rotate array
# def rotate_array(nums, k):
#     k = k % len(nums)
    
#     # nums[:] = nums[-k:] + nums[:-k]
    
#     # return nums
    
#     nums.reverse()
    
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
    
#     return nums

# # Test example
# nums = [-1,-100,3,99]
# k = 2
# print(rotate_array(nums, k))



# # Next permutation
# def next_permutation(nums):
#     n = len(nums)
    
#     i = n - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1
        
#     if i >= 0:
#         j = n - 1
#         while j >= 0 and nums[i] >= nums[j]:
#             j -= 1
            
#         nums[i], nums[j] = nums[j], nums[i]
        
#     left, right = i + 1, n - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right += 1
    
        



# # Arrange Zeros
# def arrange_zero_and_nonzero_elements(nums):
#     n = len(nums)
#     zero_index = 0
    
#     for i in range(n):
#         if nums[i] != 0:
#             nums[zero_index], nums[i] = nums[i], nums[zero_index]
#             zero_index += 1
            
# array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
# arrange_zero_and_nonzero_elements(array)
# print(array)

# def duplicate_zeros(arr):
#     n = len(arr)
#     zeros = arr.count(0)
    
#     i, j = n - 1, n + zeros - 1
    
#     while i >= 0:
#         if j < n:
#             arr[j] = arr[i]
            
#         if arr[i] == 0:
#             j -= 1
            
#             if j < n:
#                 arr[j] = 0
                
#         i -= 1
#         j -= 1
        
# # Example Usage:
# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# duplicate_zeros(arr)
# print(arr)


# # Products of Elements
# def product_of_elements(nums):
#     n = len(nums)
    
#     left_products = [1] * n
#     right_products = [1] * n
    
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
        
#     right_product = 1
#     for i in range(n - 2, -1, -1):
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
        
#     result = [left_products[i] * right_products[i] for i in range(n)]
    
#     return result


# # Example usage
# array = [2, 4, 6, 8, 10]
# result = product_of_elements(array)
# print(result)



# # Sorted Squares
# def sorted_squares(nums):
#     n = len(nums)
#     result = [0] * n
#     l, r = 0, n - 1
#     pos = n - 1
    
#     while l <= r:
#         left_square = nums[l] ** 2
#         right_square = nums[r] ** 2
        
#         if left_square > right_square:
#             result[pos] = left_square
#             l += 1
#         else:
#             result[pos] = right_square
#             r -= 1
        
#         pos -= 1
        
#     return result
        
    
#     # nums_square = [i ** 2 for i in nums]
#     # nums_square.sort()
    
#     # return nums_square

# # Example usage:
# nums = [-4, -1, 0, 3, 10]
# result = sorted_squares(nums)
# print(result)

