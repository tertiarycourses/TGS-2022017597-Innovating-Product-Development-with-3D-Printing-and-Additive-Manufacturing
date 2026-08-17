# Lab 9 — Support Structures for Overhangs

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 02:** Process Related Issues for AM  
**TSC objective:** A2, A3 — determine when overhang geometry requires supports and generate them

## Goal

Slice twist.stl — a model with steep overhangs — first without and then with generated supports, print it, and remove the supports cleanly.

## What you'll build

A printed twist model whose overhangs succeeded because of correctly placed supports.

**Tools:** Ultimaker Cura, twist.stl, FDM printer

## Steps

1. Open twist.stl in Cura and slice it with supports off.

   ```
   File ▸ Open ▸ twist.stl ▸ Slice
   ```

2. In Preview, find the layers that start in mid-air — these overhangs would droop or fail.

   ```
   Preview ▸ layer slider — spot unsupported islands
   ```

3. Enable support generation.

   ```
   Print Settings ▸ Support ▸ Generate Support ✔
   ```

4. Set placement to Touching Buildplate first; compare with Everywhere and note the difference in Preview.

   ```
   Support Placement — Touching Buildplate vs Everywhere
   ```

5. Keep the support overhang angle at 45–50° so only genuinely steep faces get support.

   ```
   Support Overhang Angle — 50°
   ```

6. Slice again and compare time and material with the unsupported version, then print.

   ```
   Slice ▸ Save to Disk ▸ print
   ```

7. Snap the supports off with pliers, working from the edges inward, and inspect the supported surfaces.

   ```
   Needle-nose pliers ▸ remove supports
   ```


## Test it

The unsupported slice shows mid-air layers while the supported print completes; supports snap away leaving only minor scarring on the underside.

## Files in this folder

- `twist.stl`
