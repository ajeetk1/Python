# Mathemics Function  - Day8
# We are creating math and ceil 
# ceil round fucntion to nearest whole number

from math import ceil 

def paint_calc(height,width,cover):
   paint_area = ceil(height*width/cover)
   return paint_area

# User Input
demo_h= int(input("Enter height of wall"))
demo_w  = int(input("Enter width of wall"))
coverage= 10


paint_area_total = paint_calc(demo_h, demo_w,coverage)
print(paint_area_total)
print(f"Total area is {paint_area_total}")
 
# # 

from math import ceil 

# Function Declare 
def rect_calc(length,width):
   rect_area = ceil(length*width)
   return rect_area

# user input 
l = 10
w= 20 

# Calculation

total_area = rect_calc(l,w)
print(total_area)





