# Lab 15 — Fuzzy Skin — Textured Walls on a Vase

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — apply fuzzy skin as a deliberate surface-texture treatment

## Goal

Enable fuzzy skin on a vase model so the outer wall is jittered into a stone-like texture that hides layer lines, and print it with buildplate adhesion.

## What you'll build

A vase with a uniform fuzzy texture that masks layer lines completely.

**Tools:** Ultimaker Cura, open vase.stl, 1.5mm-wall-vase.stl, FDM printer

## Steps

1. Open 'open vase.stl' in Cura.

   ```
   File > Open > open vase.stl
   ```

2. Enable fuzzy skin — the slicer adds random jitter to the outer wall toolpath.

   ```
   Experimental > Fuzzy Skin ✔
   ```

3. Set fuzzy skin thickness to 0.3 mm and density to 1.25/mm for a fine stone texture.

   ```
   Fuzzy Skin Thickness 0.3 mm · Density 1.25
   ```

4. Add a brim so the tall thin vase stays anchored.

   ```
   Build Plate Adhesion > Brim
   ```

5. Slice and inspect the jittered outer wall in Preview.

   ```
   Slice > Preview > outer wall
   ```

6. Print the vase and examine the texture — layer lines should be invisible within the fuzz.

   ```
   print + inspect
   ```

7. Open 1.5mm-wall-vase.stl and verify the chosen fuzzy-skin thickness will not consume the thin wall; reduce the effect if Preview shows unstable or missing wall paths.

   ```
   Open 1.5mm-wall-vase.stl > Preview > Line Type > inspect wall continuity
   ```


## Evidence to capture

- Cura Preview showing fuzzy-skin jitter and the 1.5 mm wall toolpaths.
- Close-up photo and tactile assessment of the finished texture.


## Test it

The printed vase carries an even tactile texture, and the 1.5 mm diagnostic vase retains continuous walls in Preview—showing that the texture setting fits the available wall thickness.

## Files in this folder

- `open vase.stl` — Core sample model used by the lab procedure.
- `1.5mm-wall-vase.stl` — Thin-walled vase benchmark for comparing fuzzy skin with wall-thickness constraints.
