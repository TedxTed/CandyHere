
def bubble_sort_recursion(nums):
    # recursion 要先設起始點
    round = 0 
    bubble_sort_recursion_help1(nums, round)
    
# recursion helper 1 step 1 : add function   
def bubble_sort_recursion_help1(nums , round):
    # recursion helper 1 step 3 add recursion terminate condition
    if round >= len(nums): 
        return
        
    length = len(nums) - round
    # for i_run in range(1, length):
        # if nums[i_run -1 ] > nums[i_run]:
        #   swap(nums , i_run - 1, i_run)
    # 迴圈改遞迴
      # 觀察起始點到最終點 起始點：1 到 最終點：length(剩餘長度)
    # 設新的recursion helper 2 
    # recursion 先設起始點
    i_run = 1
    bubble_sort_recursion_help2(nums, length , i_run )
          
    # recursion helper 1 step 2 : call by myself，and +1 
    bubble_sort_recursion_help1(nums, round+1)


def bubble_sort_recursion_help2(nums, length , i_run):
  
  if i_run >= length:
      return
    
  if nums[i_run -1 ] > nums[i_run]:
            swap(nums , i_run - 1, i_run)
            
  bubble_sort_recursion_help2(nums, length , i_run + 1 )

def swap(nums , i_left , i_right):
    tmp = nums[i_left]
    nums[i_left] = nums[i_right]
    nums[i_right] = tmp
    
if __name__ == "__main__":
    nums = [8 , 2 , 6, 10]
    bubble_sort_recursion(nums)
    print(nums)
