# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate_t(nums)
  # here
  a = {}
  nums.each do |num|
    if a[num]
      a[num] += 1
    else
      a[num] = 1
    end
  end
  a.values.each do |value|
    return true if value > 1
  end
  false
end

def contains_duplicate_a(nums)
  hash = {}
  nums.each do |num|
    return true if hash.key? num

    hash[num] = true
  end
  false
end
p contains_duplicate([4, 2, 3, 1]) # True
p contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) # true
