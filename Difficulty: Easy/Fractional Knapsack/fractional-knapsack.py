class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # Build list of (value/weight ratio, value, weight) for each item
        # Ignore any items with zero weight to avoid division by zero
        items = [(v / w, v, w) for v, w in zip(val, wt) if w > 0]
        
        
        items.sort(key = lambda x : x[0] , reverse = True )
        
        
        currw = 0 
        finalvalue = 0.0 
        
        for ratio , v, w in items:
            if currw + w <= capacity:
                currw += w
                finalvalue += v
            else:
                
                remain = capacity - currw
                if remain <= 0:
                    break 
                finalvalue += ratio * remain 
                break 
            
        return finalvalue 
            
        
        
        
        
        