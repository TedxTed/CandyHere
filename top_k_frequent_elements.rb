# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
  result = {}
  nums.each do |num|
    if result[num]
      result[num] += 1
    else
      result[num] = 1
    end
  end
  
end

nums = [1, 1, 1, 2, 2, 3]
k = 2

p top_k_frequent(nums, k) # [1,2]
