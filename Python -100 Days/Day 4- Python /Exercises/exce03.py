#Declare Rows 
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

treasure_maps = [row1,row2,row3]
print(f'{row1}\n,{row2}\n,{row3}')

position = input("Where you want to put the treasure")

row = int(position[1])-1 
col = int(position[0])-1 

treasure_maps[row][col] = '❎️'

print(f"{row1}\n,{row2}\n,{row3}")