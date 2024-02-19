# SphericalGridProjector
Blender operators for spherical grid projection

How To Use:

1. Prepare a plane grid mesh in range (-1,1) (both x,y axis).
2. Run InitialGridOperator.py.
3. Run SphericalGridOperator.py.
4. Prepare low-poly sphere mesh which has radius = radius_scalar in SphericalGridOperator.py
5. Remove boundary faces and merge & connect vertices of grid mesh/sphere mesh.

Note : The grid projection is theoretically based on Florian Michelic's paper [Real-Time Rendering of Procedurally Generated Planets]

https://cescg.org/wp-content/uploads/2018/04/Michelic-Real-Time-Rendering-of-Procedurally-Generated-Planets-2.pdf
