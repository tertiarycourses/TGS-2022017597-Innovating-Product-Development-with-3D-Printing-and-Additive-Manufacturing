# Lab 13 — Layer Height and Top Thickness — Surface Quality

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — optimise layer height and top thickness for surface quality vs speed

## Goal

Slice the same model at 0.1 mm, 0.2 mm and 0.3 mm layer heights, adjust top thickness to a constant, and compare surface quality against print time.

## What you'll build

Sliced (and optionally printed) evidence of the layer-height ladder: finish vs time.

**Tools:** Ultimaker Cura, cube10.stl, FDM printer

## Steps

1. Open cube10.stl and slice at 0.2 mm layer height; record the time.

   ```
   Quality ▸ Layer Height — 0.2 mm
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
   Top/Bottom ▸ Top Thickness — 0.8 mm
   ```

5. In Preview, compare side-wall stair-stepping and the roof at each height.

   ```
   Preview ▸ compare walls + roof
   ```

6. Print the 0.1 mm and 0.3 mm cubes and compare finish by eye and touch.

   ```
   print both
   ```


## Test it

You can rank the three layer heights by surface quality and by print time, and state why top thickness (not top layer count) is the setting to keep constant.

## Files in this folder

- `cube10.stl`
