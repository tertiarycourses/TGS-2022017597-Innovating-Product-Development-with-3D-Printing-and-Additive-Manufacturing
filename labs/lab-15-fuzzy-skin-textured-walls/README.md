# Lab 15 — Fuzzy Skin — Textured Walls on a Vase

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — apply fuzzy skin as a deliberate surface-texture treatment

## Goal

Enable fuzzy skin on a vase model so the outer wall is jittered into a stone-like texture that hides layer lines, and print it with buildplate adhesion.

## What you'll build

A vase with a uniform fuzzy texture that masks layer lines completely.

**Tools:** Ultimaker Cura, open vase.stl, FDM printer

## Steps

1. Open 'open vase.stl' in Cura.

   ```
   File ▸ Open ▸ open vase.stl
   ```

2. Enable fuzzy skin — the slicer adds random jitter to the outer wall toolpath.

   ```
   Experimental ▸ Fuzzy Skin ✔
   ```

3. Set fuzzy skin thickness to 0.3 mm and density to 1.25/mm for a fine stone texture.

   ```
   Fuzzy Skin Thickness 0.3 mm · Density 1.25
   ```

4. Add a brim so the tall thin vase stays anchored.

   ```
   Build Plate Adhesion ▸ Brim
   ```

5. Slice and inspect the jittered outer wall in Preview.

   ```
   Slice ▸ Preview ▸ outer wall
   ```

6. Print the vase and examine the texture — layer lines should be invisible within the fuzz.

   ```
   print + inspect
   ```


## Test it

The printed vase carries an even, tactile texture on every outer wall with no visible layer banding — a finish achieved purely in slicing, with zero post-processing.

## Files in this folder

- `open vase.stl`
