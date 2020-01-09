# CS-110
The most notable projects (and necessary libraries) from my Python class at Hamilton.

## Pulsar
This project required the analysis of pulsar data from <a href = "https://www.atnf.csiro.au" target ="_blank">The ATNF Pulsar Catalog</a> in
hopes of understanding pulsars in the ”vicinity” of earth. The data were contained in a CSV (data.csv in this repo), and our task was to parse the data appropriately and run experiments that print superlatives (such as oldest, closest, and most recently discovered) to the console as well as all of the data associated with that pulsar. Testing is accomlished in the file testing_pulsar.py using the file pulsar_test_data.csv.

## Tiling
A tetris-style tiling game (written using turtle) where the goal is to use "triominoes" to populate a grid. Pressing "t" creates a triomino, "r" rotates it 90 degrees, and movement in two dimensions is controlled via the arrow keys. Pressing "t" again will "place" the triomino on the grid (where it can no longer be moved) and create a new active triomino in the upper-left corner of the grid. Triominoes are not allowed to overlap, and the board has a randomly-placed hole (which guarantees that a solution is possible).

## The Game (Lost Cities)
The final project of CS-110. Using a graphics library [created specifically for CS-110 at Hamilton](https://github.com/matthewjenkins97/CS110-Graphics), I recreated the board game Lost Cities, [whose rules can be found here](https://cdn.1j1ju.com/medias/c8/66/47-lost-cities-rulebook.pdf).
