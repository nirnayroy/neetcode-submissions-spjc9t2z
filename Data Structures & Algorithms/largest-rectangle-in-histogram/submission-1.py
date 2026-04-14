class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_stack = [] # (last_popped_index, height)
        max_area = 0

        for i, height in enumerate(heights):
            last_popped_index = i
            while len(heights_stack) > 0 and height <= heights_stack[-1][1]:

                max_area = max(max_area, heights_stack[-1][1]*(i-heights_stack[-1][0]))
                (last_popped, _) = heights_stack.pop(-1)
                last_popped_index = last_popped
        
            heights_stack.append((last_popped_index, height))
            # if len(heights_stack) > 0 and height > heights_stack[-1][1]:
            #     last_popped_index = i
            
            
            
            print(max_area)
        
        print(heights_stack)
        for i, height in heights_stack:
            max_area = max(max_area, height*(len(heights)-i))
            
        return max_area