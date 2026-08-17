# Lab 5 — Tolerance — Container and Lid (0.2 mm Fit)

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — determine digital and physical tolerances between assembling parts

## Goal

Model a container and lid as two separate bodies in Fusion 360 with a 0.2 mm clearance, verify the digital tolerance, then 3D print and test the physical fit.

## What you'll build

A two-part container whose lid slides on with a designed 0.2 mm clearance.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA), digital calipers

## Steps

1. Model a 50 × 50 × 30 mm box and shell it to 2 mm walls with the top face removed.

   ```
   Create ▸ Box 50×50×30 ▸ Modify ▸ Shell — 2 mm
   ```

2. Model the lid as a second body: a 54 × 54 × 6 mm cap whose inner skirt is offset 0.2 mm from the box's outer wall.

   ```
   Create ▸ Box (New Body) ▸ Modify ▸ Offset Faces — 0.2 mm clearance
   ```

3. Measure the designed gap with the Inspect ▸ Measure tool to confirm 0.2 mm per side.

   ```
   Inspect ▸ Measure — wall-to-skirt gap = 0.2 mm
   ```

4. Export each body as its own STL file.

   ```
   Right-click body ▸ Save As Mesh — container.stl, lid.stl
   ```

5. In Cura, print the container open-end up; rotate the lid open-end up as well (invert it).

   ```
   Cura ▸ Open Files ▸ Rotate lid 180°
   ```

6. Slice and print both parts in one job.

   ```
   Cura ▸ Slice ▸ Save to Disk ▸ print
   ```

7. Measure the printed gap with digital calipers and test the fit.

   ```
   Calipers: outer wall vs lid skirt — expect ≈0.2 mm/side
   ```


## Test it

The lid slides onto the container with light friction — neither loose nor forced — proving the digital 0.2 mm tolerance reproduced physically.
