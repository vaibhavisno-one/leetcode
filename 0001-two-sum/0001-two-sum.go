func twoSum(nums []int, target int) []int {
 
    seen := make(map[int]int, len(nums))
    
    for currentIndex, num := range nums {
        complement := target - num
        
  
        if mapIndex, found := seen[complement]; found {
            return []int{mapIndex, currentIndex}
        }
        
        seen[num] = currentIndex
    }
    
    return nil
}

