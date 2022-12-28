




combos={"a":["ABC","ACB"],
        "b":["BAC","BCA"],
        "c":["CAB","CBA"]
}


inputs=""
numThings=int(input("# of things"))


for i in range(numThings*2):
    n=input("Insert")
    inputs+=n





grid = ["","","",
        "","","",
        "","",""]
tGrid = [["","",""],
        ["","",""],
        ["","",""]]
for i in range(numThings):
    grid[int(inputs[i*2])-1]=inputs[i*2+1]


print(grid)
