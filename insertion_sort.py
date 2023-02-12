def insertion_sort(nums):
    for i_start in range(len(nums)):
        for j_run in range(i_start -1 , -1 , -1):
          # range條件，從倒數第二個開始，若判斷j_run = -1 時停止 , 每次都減一 ->往前一個
            if nums[j_run + 1] > nums[j_run]:
                swap(nums, j_run + 1 , j_run)
def swap(nums , r , l):
    tmp = nums[r]
    nums[r] = nums[l]
    nums[l] = tmp
    
if __name__ == "__main__":
    nums = [8, 2 ,6 ,10, 4]
    insertion_sort(nums)
    print(nums)