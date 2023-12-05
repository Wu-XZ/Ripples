# Ripples

## A high-dimensional multimodal synthetic function that specifically serves as a black-box function for the BBC problem

The formula of Ripples is shown as below.

$$
f(\boldsymbol{x})= \sum _{i = 1} ^ {dim} \left(e^{-\frac{x_i^2}{2\sigma}} + k cos(\omega x_i) - k \right), \ \text{where} \ x_i = \Vert \boldsymbol{x} + M_{i,:} \Vert_2, \ \text{for all} \  i = 1, 2, ..., dim
$$

In which, 

$$
M  = I_{dim} \times bias
$$
where $dim$ is the dimension of the function. $I_{dim}$ is an identity matrix with order $dim$. $M_{i,:}$ represents the $i$th row of the matrix $M$. $\sigma$, $k$, $\omega$ and $bias$ are parameters that determine the shape of the function and the locations of the optimal points.
