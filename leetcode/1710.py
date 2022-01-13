class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        '''
        Return the maximum total number of units that can be put on the truck.
        
        -   Knapsack problem ??? 
        
        -   Greedy ?
        
        truckSize = number of boxes that can be placed in the truck
        
        MAXIMUM total number of UNITS
        
        
         A = [[5,10],[2,5],[4,7],[3,9]],
         
         [[5,10],[3,9],[4,7],[2,5]]


         Recursive ??? 
        
        '''
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        #print(sorted_boxes)
        size = truckSize
        i = 0
        total = 0
        while size > 0 and i < len(sorted_boxes):
            curr_box = sorted_boxes[i][0]
            curr_box_units = sorted_boxes[i][1]
            #print(curr_box, curr_box_units, size)
            if size > 0:
                if curr_box <= size:
                    total += curr_box * curr_box_units
                    size = size - curr_box
                else:
                    total += size * curr_box_units
                    break
            i += 1
        return total
                    
                
            
