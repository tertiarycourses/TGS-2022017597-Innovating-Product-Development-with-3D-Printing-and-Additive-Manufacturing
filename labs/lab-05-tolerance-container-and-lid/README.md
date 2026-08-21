# Lab 5 — Tolerance — Container and Lid (0.2 mm Fit)

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 01:** Overview of Additive Manufacturing and 3D Scanning  
**TSC objective:** A1 — determine digital and physical tolerances between assembling parts

## Goal

Model a container and lid as two separate bodies in Fusion 360 with a 0.2 mm clearance, verify the digital tolerance, then 3D print and test the physical fit.

## What you'll build

A two-part container whose lid slides on with a designed 0.2 mm clearance.

**Tools:** Fusion 360, Ultimaker Cura, FDM printer (PLA), digital calipers, supplied FDM Box reference files

## Steps

1. Model a 50 × 50 × 30 mm box and shell it to 2 mm walls with the top face removed.

   ```
   Create > Box 50x50x30 > Modify > Shell — 2 mm
   ```

2. Model the lid as a second body: a 54 × 54 × 6 mm cap whose inner skirt is offset 0.2 mm from the box's outer wall.

   ```
   Create > Box (New Body) > Modify > Offset Faces — 0.2 mm clearance
   ```

3. Measure the designed gap with the Inspect > Measure tool to confirm 0.2 mm per side.

   ```
   Inspect > Measure — wall-to-skirt gap = 0.2 mm
   ```

4. Export each body as its own STL file.

   ```
   Right-click body > Save As Mesh — container.stl, lid.stl
   ```

5. In Cura, print the container open-end up; rotate the lid open-end up as well (invert it).

   ```
   Cura > Open Files > Rotate lid 180 degrees
   ```

6. Slice and print both parts in one job.

   ```
   Cura > Slice > Save to Disk > print
   ```

7. Measure the printed gap with digital calipers and test the fit.

   ```
   Calipers: outer wall vs lid skirt — expect ~0.2 mm/side
   ```

8. Open FDM-Box-Final.f3d as a read-only reference and inspect how its bodies, wall thickness and clearances are organised; do not replace your own design with it.

   ```
   Fusion 360 > File > Open > FDM-Box-Final.f3d > Inspect > Measure
   ```

9. Open FDM-Box-Cura.3mf and compare its saved orientation and slicer settings with your own job; record one setting you would retain and one you would change for your printer.

   ```
   Cura > File > Open Project > FDM-Box-Cura.3mf
   ```


## Evidence to capture

- Screenshot of the 0.2 mm designed clearance measured in Fusion 360.
- Cura comparison showing your model and FDM-Box-Final.stl at the intended scale and orientation.
- Caliper readings and a short pass/fail note for the printed lid fit.


## Test it

The lid slides onto the container with light friction — neither loose nor forced — and your evidence distinguishes the designed 0.2 mm clearance, the measured printed result and the supplied FDM Box reference setup.

## Files in this folder

- `FDM-Box-Final.f3d` — Editable Fusion 360 reference model for design-history and clearance inspection.
- `FDM-Box-Final.stl` — Printable mesh for orientation, scale and fit comparison.
- `FDM-Box-Cura.3mf` — Cura project retaining the supplied slicer setup for comparison with your own profile.
