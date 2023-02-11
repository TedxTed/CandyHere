def bubble_sort(nums)
  nums.length.times do |num|
    p "num is #{num}"
    len = nums.length - num
    (1...len).each do |i_run|
      p "i_run is #{i_run} "
      swap(nums, i_run - 1, i_run) if nums[i_run - 1] > nums[i_run]
    end
  end
  nums
end

def swap(nums, i_left, i_right)
  tmp = nums[i_left]
  nums[i_left] = nums[i_right]
  nums[i_right] = tmp
end

p bubble_sort([2, 1, 3, 4])
