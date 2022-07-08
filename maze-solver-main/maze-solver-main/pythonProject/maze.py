
""" Creating the graph with the image given ( Traversing and finding the path through the image is faster than
    finding the path through the actual maze) We read from the image once per pixel"""

#Node Class
class Maze:
    class Node: 
        def __init__(self, position):
            self.Position = position 
            self.Neighbours = [None, None, None, None]   #Neighbours of the node, None is equivalent to wall

    def __init__(self, im):
    #This constructor traverses across the image(im) and constructs the graph strcuture.
        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(0))

        self.start = None
        self.end = None

        # Top row
        topnodes = [None] * width
        count = 0

        # Start row - For finding the start node
        for x in range(1, width - 1):
            if data[x] > 0:
                self.start = Maze.Node((0, x))
                topnodes[x] = self.start
                count += 1
                break

        #Now, we go to every single pixel in each row and based on previous square, current square we are on and next square we have to make a decision 
        #whether to create a node at that square and connect it to left or above node(As we are moving downwards and traversing through rows from left to right).  
        for y in range(1, height - 1):
            print("row", str(y))  # Progress of the graph

            rowoffset = y * width
            rowaboveoffset = rowoffset - width
            rowbelowoffset = rowoffset + width

            # Initialise previous, current and next values
            prv = False
            cur = False
            nxt = data[rowoffset + 1] > 0

            # Based on these values it is decided to create a node (or) not

            leftnode = None

            for x in range(1, width - 1):
                prv = cur
                cur = nxt
                nxt = data[rowoffset + x + 1] > 0

                n = None

                if cur == False:  # This means wall so no action is taken
                    continue

                if prv == True:
                    if nxt == True:
                        #PATH PATH PATH 
                        if data[rowaboveoffset + x] > 0 or data[rowbelowoffset + x] > 0:
                            n = Maze.Node((y, x))
                            leftnode.Neighbours[1] = n #Creating a node and connecting to its neighbour
                            n.Neighbours[3] = leftnode 
                            leftnode = n
                    else:
                        # Path Path Wall
                        # Create path at end of corridor
                        n = Maze.Node((y,x))
                        leftnode.Neighbours[1] = n
                        n.Neighbours[3] = leftnode
                        leftnode = None

                else:
                    if nxt == True:
                        # WALL PATH PATH
                        # Create path at start of corridor
                        n = Maze.Node((y, x))
                        leftnode = n

                    else:
                        # WALL PATH WALL
                        # Create node only if in dead end
                        if (data[rowaboveoffset + x] == 0) or (data[rowbelowoffset + x] == 0):
                            #print ("Create Node in dead end")
                            n = Maze.Node((y, x))

                # If node isn't none, we can assume we can connect N-S somewhere
                if n != None:
                    # Clear above, connect to waiting top node
                    if (data[rowaboveoffset + x] > 0):
                        t = topnodes[x]
                        t.Neighbours[2] = n
                        n.Neighbours[0] = t

                    # If clear below, put this new node in the top row for the next connection -  Connection of nodes
                    if (data[rowbelowoffset + x] > 0):
                        topnodes[x] = n
                    else:
                        topnodes[x] = None

                    count += 1

        # End row - For end nodes
        rowoffset = (height - 1) * width
        for x in range(1, width - 1):
            if data[rowoffset + x] > 0:
                self.end = Maze.Node((height - 1, x))
                t = topnodes[x]
                t.Neighbours[2] = self.end
                self.end.Neighbours[0] = t
                count += 1
                break

        self.count = count
        self.width = width
        self.height = height
