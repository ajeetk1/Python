for number in range(1,100):
    print(number)
    print()

for number in range (1,12):
 print(number)

 for number in range(1,10,11):
  print(number)
  # range(start,stop,step)
  # Meaning: start at 1, then keep adding 11, until it reaches or passes 10.First value: 1 Next would be 1 + 11 = 12 → but 12 ≥ 10, so the loop ends.
  #So the output should be just 1, not 1,1,1,2.