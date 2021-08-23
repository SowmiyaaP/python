r1 = ['☠️' , '☠️' , '☠️' ]
r2 = ['☠️' , '☠️' , '☠️' ]
r3 = ['☠️' , '☠️' , '☠️' ]
map = [r1 , r2 , r3]
print(f"{r1}\n{r2}\n{r3}")
pos = input("Where do you want to put the treasure? ")
select = map[int(pos[1])-1]
select[int(pos[0])-1] = "x"
print(f"{r1}\n{r2}\n{r3}")