# fire-propagation
This is a simulation of fire propagation in a forest.

![](https://github.com/LukasGyp/fire-propagation/blob/main/docs/fire.gif)

The fire spreads proportionally to the distance from the cells actually buring, 
and the intensity can be described by the following equation
```math
\frac{dB}{dt} = r B \left(1 - \frac{B}{K} \right),
```
where $`B`$ is the amount of wood which is not exposed to fire, $r$ is the grouth rate of fire, and $K$ is the initial amount of woods. (These values are attributed to each cells). This model seems to be inappropriate and has to be modified...