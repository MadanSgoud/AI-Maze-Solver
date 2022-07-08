

"""     Create and save the output image.
    This drawing code travels between each node in turn, drawing either
    a horizontal or vertical line as required. Line colour is roughly interpolated between
    blue and red depending on how far down the path this section is    """


# Import Statements
from PIL import Image
import argparse   # For reading command line arguments
from mazes import Maze
from factory import SolveFactory
Image.MAX_IMAGE_PIXELS = None


def solve(factory, method, input_file, output_file):
    # Loading Image
    print("Loading Image")
    im = Image.open(input_file)

    # Creating the maze
    print("Creating Maze")
    maze = Maze(im)
    print("Node Count:", maze.count)  # Displays the node count of the graph created

    # Create and run solver
    [title, solver] = factory.createsolver(method)
    print("Starting Solve - ", title)
    [result, stats] = solver(maze)
    
    

    # Print solve stats
    print("Nodes explored: ", stats[0])
    if(stats[2]):
        print("Path found, length", stats[1])
    else:
        print("No Path Found")

    print("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]
    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Colours interpolated between blue and red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Draw horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px

    im.save(output_file)  # Saving the coloured file


def main():
    sf = SolverFactory()
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", nargs='?', const=sf.Default, default=sf.Default, choices=sf.Choices)
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    solve(sf, args.method, args.input_file, args.output_file)

if __name__ == "__main__":
    main()
