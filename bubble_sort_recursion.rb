def bubble_sort_recursion(nums)
  round = 0
  bubble_sort_recursion_helper1(nums, round)
  nums
end

def bubble_sort_recursion_helper1(nums, round)
  return if round >= nums.length

  len = nums.length - round
  i_run = 1
  bubble_sort_recursion_helper2(nums, len, i_run)

  bubble_sort_recursion_helper1(nums, round + 1)
end

def bubble_sort_recursion_helper2(nums, len, i_run)
  return if i_run >= len

  swap(nums, i_run - 1, i_run) if nums[i_run - 1] > nums[i_run]

  bubble_sort_recursion_helper2(nums, len, i_run + 1)
end

def swap(nums, i_left, i_right)
  tmp = nums[i_left]
  nums[i_left] = nums[i_right]
  nums[i_right] = tmp
end

p bubble_sort_recursion([2, 1, 3, 4])
