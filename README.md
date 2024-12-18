# fire-propagation
This is a simulation of fire propagation in a forest.

![](https://github.com/LukasGyp/fire-propagation/blob/main/docs/fire.gif)

## How to run
Execute `main.py` with these options
- `-s [int] [int]`, `--size [int] [int]`: size of map
- `--fire [int] [int]` : initial fire point
- `-w [int]`, `-wood [int]` : initial amount of wood in each cell 
- `-f [int]`, `--frame [int]` : number of frames
- `-o`, `--output`: output the result gif file

## Model
The fire spreads proportionally to the distance from the cells actually buring, 
and the intensity can be described by the following equation
```math
\frac{dB}{dt} = r B \left(1 - \frac{B}{K} \right),
```
where $`B`$ is the amount of wood which is not exposed to fire, $r$ is the grouth rate of fire, and $K$ is the initial amount of woods. (These values are attributed to each cells). This model seems to be inappropriate and has to be modified...

## To go further
By modifying the third line in `main` function, you can put multiple initial fires. 
`add_fire` function takes 2 arguments, which are x coordinate and y coordinate.