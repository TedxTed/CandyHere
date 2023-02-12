def insertion_sort(nums)
  return unless nums.instance_of?(Array)

  nums.each_with_index do |_num, i_start|
    j_run = i_start - 1
    while j_run > -1
      swap(nums, j_run + 1, j_run) if nums[j_run + 1] > nums[j_run]
      j_run -= 1
    end
  end
  nums
end

def swap(nums, r, l)
  return unless nums.instance_of?(Array)

  tmp = nums[r]
  nums[r] = nums[l]
  nums[l] = tmp
end

p insertion_sort([1, 2, 3, 4])
