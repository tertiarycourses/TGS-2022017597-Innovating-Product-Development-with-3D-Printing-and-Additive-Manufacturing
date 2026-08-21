# Lab 13 — Layer Height and Top Thickness — Surface Quality

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — optimise layer height and top thickness for surface quality vs speed

## Goal

Slice the same model at 0.1 mm, 0.2 mm and 0.3 mm layer heights, adjust top thickness to a constant, and compare surface quality against print time.

## What you'll build

Sliced (and optionally printed) evidence of the layer-height ladder: finish vs time.

**Tools:** Ultimaker Cura, cube10.stl, sloped-cube.stl, FDM printer

## Steps

1. Open cube10.stl and slice at 0.2 mm layer height; record the time.

   ```
   Quality > Layer Height — 0.2 mm
   ```

2. Slice at 0.1 mm; note the doubled layer count and time.

   ```
   Layer Height — 0.1 mm
   ```

3. Slice at 0.3 mm; note the coarser stairs and the reduced time.

   ```
   Layer Height — 0.3 mm
   ```

4. Keep top thickness constant at 0.8 mm — so the TOP LAYER COUNT changes with layer height (8 / 4 / 3 layers).

   ```
   Top/Bottom > Top Thickness — 0.8 mm
   ```

5. In Preview, compare side-wall stair-stepping and the roof at each height.

   ```
   Preview > compare walls + roof
   ```

6. Print the 0.1 mm and 0.3 mm cubes and compare finish by eye and touch.

   ```
   print both
   ```

7. Repeat the three slices with sloped-cube.stl and zoom into the sloped face; this geometry makes the staircase effect visible in Preview before printing.

   ```
   Open sloped-cube.stl > Slice at 0.1 / 0.2 / 0.3 mm > compare
   ```


## Evidence to capture

- Three-row layer-height table with layer count, print time and observed stair-stepping.
- Matched Preview screenshots of the sloped face at 0.1, 0.2 and 0.3 mm.


## Test it

You can rank the layer heights by finish and time, point to visible stair-stepping on sloped-cube.stl, and explain why constant top thickness—not a fixed top-layer count—keeps the comparison fair.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
- `sloped-cube.stl` — Sloped-face benchmark that makes layer-height stair-stepping easy to compare.
