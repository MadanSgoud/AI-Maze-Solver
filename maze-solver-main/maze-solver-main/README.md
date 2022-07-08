# Maze-Solver

This is a project for a group of academics

Group Members :

201951159@iiitvadodara.ac.in - Syed Shahid Nazeer

201951179@iiitvadodara.ac.in - Yerrajenni Ediga Madan Swaroop Goud

201951061@iiitvadodara.ac.in - Gaini Om Prakash

201951186@iiitvadodara.ac.in - Dharavath Rajeev Gandhi


## Putting Search Algorithms into practice

We developed a program that takes a maze image as input and returns the solved maze image as output. 

### Search algorithm used : A-Star

Any image that does not match one of the guidelines will not operate in the software. The input image should only contain white pixels (Path) and black pixels (Walls), with an entry at the top and an exit at the bottom. The first black pixel line should have a white space (considered an entry) and the last black pixel line should have a white space (Considered as exit).


We can transform this maze into a graph using a one-pass approach, allowing us to solve the maze quickly.

#### Creation and joining of nodes

One - Pass algorithm : (Black pixel - Wall and White pixel - Path)

1. We go through each pixel row by row.
 
2. The start node will be the white pixel in the first row and the end node will be the white pixel in the last row.

3. If there is a possible way to the up or down and right or left from a pixel then it is a junction and we will consider that pixel as a node.

4. Joining of nodes : When we build a node, we must attach it to the node that came before it on the left (moving from right to left) or above it if there are any.


Like this we are create a graph on which we will apply A-Star search algorithm.

We've put this graph in a class called maze class.

Now, our target is to go from start node to end node.


Action value method : estimation of mean of rewards corresponding to the actions.










