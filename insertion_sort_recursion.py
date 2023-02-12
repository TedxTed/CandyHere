def insertion_sort_recursion(nums):
    i_start = 0
    insertion_sort_recursion_helper01(nums , i_start)
    
def insertion_sort_recursion_helper01(nums, i_start):
    if i_start >= len(nums):
      return

    j_run  = i_start-1
    insertion_sort_recursion_helper02(nums , j_run)

    insertion_sort_recursion_helper01(nums , i_start + 1 )

def insertion_sort_recursion_helper02(nums , j_run):
    
    if j_run < 0 :
        return

    if nums[j_run + 1] > nums[j_run]:
        swap(nums, j_run + 1 , j_run)
    else:
      # 沒有比較快就直接return省掉後面的運算時間
        return
    
    insertion_sort_recursion_helper02(nums , j_run -1 )
    
def swap(nums , r , l):
    tmp = nums[r]
    nums[r] = nums[l]
    nums[l] = tmp

if __name__ == "__main__":
  nums = [8,2, 6, 10 ,4,5]
  insertion_sort_recursion(nums)
  print(nums)