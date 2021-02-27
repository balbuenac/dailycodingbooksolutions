func minOperations(boxes string) []int {
    // Input : boxes where boxes[i] = 1 or 0
    // Ouput: MINIMUM number of operations to have all the boxes in position i
    // Operation = adjacent(i-j) = 1 i, j are indices
    N := len(boxes)
    result := make([]int, 0, N)
    min := 0
    for i := 0; i < N; i++ {
        min = helper(boxes, i) 
        result = append(result, min)
    }
    return result
}

func helper(boxes string, curr int) int {
    total := 0
    
    for i:=0; i<curr; i++ {
        if (boxes[i] == '1') {
            total = total + (curr - i)
        } 
    }
    
    // right
    for j:=len(boxes)-1; j>curr; j-- {
        if (boxes[j] == '1') {
            total = total + (j - curr)
        } 
    }
    
    return total
}
