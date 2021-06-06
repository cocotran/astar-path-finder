# Covid19 Map Simulation

A program using A* algorithm to find the optimal paths between any located points on the map.  

## Usage
This program requires Python 3.8.5 or above, and only uses the Python standard library.  
  
To run the program:  
  
In the root project directory, run:  

```bash
$ python3 main.py [--d ROWxCOLUMN]  # [--d ROWxCOLUMN] is an optional argument to specify the map dimension
```
  
Example:
```bash
$ python3 main.py
Enter map dimension (row x column) (e.g., 3 x 4): 5x5
```
is the same as:
```bash
$ python3 main.py --d 5x5
```
after specifying the dimension, new map will be generated and printed to the console. The program will ask for the start and end point:
```bash
Enter start point coordinate (x, y) (e.g., 0.4, 0.15):
Enter start point coordinate (x, y) (e.g., 0.4, 0.15):
```
the program will then perform calculation to find and print the optimal path and it's cost:
```bash
Path to quarantine place with lowest cost:
Path: A --> B --> C --> D
Cost: 6.0
```
  
Complete example:
```bash
$ python3 main.py --d 5x5

A-----B-----C-----D-----E-----F
|  @  |  *  |  %  |  @  |  @  |
G-----H-----I-----J-----K-----L
|  %  |     |  @  |     |     |
M-----N-----O-----P-----Q-----R
|  @  |  %  |  @  |  %  |  @  |
S-----T-----U-----V-----W-----X
|     |  *  |     |  *  |  @  |
Y-----Z-----a-----b-----c-----d
|  @  |  *  |  @  |  *  |  @  |
e-----f-----g-----h-----i-----j

Enter start point coordinate (x, y) (e.g., 0.4, 0.15): 0, 0
Enter start point coordinate (x, y) (e.g., 0.4, 0.15): 0.60, 0.43

Path to quarantine place with lowest cost:
Path: A --> B --> C
Cost: 3.0
```


