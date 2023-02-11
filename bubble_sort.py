def bubble_sort(nums):
    for round in range(len(nums)):
        # length 用來讓我們知道後面還有幾個數字可以做比對
          # ex:長度5,我們在第三個位置，後面還有兩個數字要比對 
          # round是從0開始，故第三個位置round為2,length 為3
        length = len(nums) - round
        for i_run in range(1, length):
          # first run, nums[i_run -1 ] = 0 , nums[i_run]= 1
          if nums[i_run -1 ] > nums[i_run]:
            swap(nums , i_run - 1, i_run)
            
def swap(nums , i_left , i_right):
    tmp = nums[i_left]
    nums[i_left] = nums[i_right]
    nums[i_right] = tmp
    
if __name__ == "__main__":
    nums = [8 , 2 , 6, 10]
    bubble_sort(nums)
    print(nums)

