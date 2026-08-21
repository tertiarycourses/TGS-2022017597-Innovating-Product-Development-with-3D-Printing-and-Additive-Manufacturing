# Lab 8 — Bed Adhesion — Skirt vs Brim vs Raft

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 02:** Process Related Issues for AM  
**TSC objective:** A2 — analyse first-layer adhesion issues and select the correct adhesion aid

## Goal

Slice three instances of the same cube with a skirt, a brim and a raft, print them, and compare adhesion strength, removal effort and bottom-surface finish.

## What you'll build

Three prints of cube10.stl demonstrating skirt, brim and raft — and a rule for when to use each.

**Tools:** Ultimaker Cura, cube10.stl, FDM printer

## Steps

1. Open cube10.stl in Cura and duplicate it twice so three cubes sit on the plate.

   ```
   Right-click > Multiply Selected — 2 copies
   ```

2. Select cube 1 and set Build Plate Adhesion to Skirt — a loop that primes the nozzle without touching the part.

   ```
   Per Model Settings > Build Plate Adhesion > Skirt
   ```

3. Select cube 2 and set adhesion to Brim, 8 mm — a flat border fused to the part's first layer.

   ```
   Build Plate Adhesion > Brim — width 8 mm
   ```

4. Select cube 3 and set adhesion to Raft — a printed platform the part sits on.

   ```
   Build Plate Adhesion > Raft
   ```

5. Slice and compare the three toolpaths in Preview; note the extra time and material the raft adds.

   ```
   Slice > Preview
   ```

6. Print all three cubes in one job.

   ```
   Save to Disk > print
   ```

7. Remove each cube: note how the skirt never touches, the brim peels off the edge, and the raft must be pried from the base.

   ```
   Deburring tool / scraper
   ```


## Evidence to capture

- Cura Preview screenshot showing the skirt, 8 mm brim and raft toolpaths.
- Recorded time/material estimate for each adhesion option.
- Photo or observation table comparing removal effort and bottom-surface finish.


## Test it

You can state when each aid applies — skirt to prime the nozzle, brim for warping-prone or small-footprint parts, raft for top-heavy or poorly adhering parts — and show the bottom-finish difference.

## Files in this folder

- `cube10.stl` — Core sample model used by the lab procedure.
