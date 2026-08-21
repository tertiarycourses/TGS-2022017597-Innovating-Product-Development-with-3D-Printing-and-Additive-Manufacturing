# Lab 9 — Support Structures for Overhangs

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 02:** Process Related Issues for AM  
**TSC objective:** A2, A3 — determine when overhang geometry requires supports and generate them

## Goal

Use supplied twist, wedge and sideways-hole models to identify unsupported islands, compare orientation choices, then generate only the supports the geometry needs.

## What you'll build

A support decision sheet plus a printed Twisted Solid whose critical overhangs succeed with controlled support use.

**Tools:** Ultimaker Cura, Twisted-Solid.stl, wedge.stl, cube20-sideways-hole.stl, FDM printer

## Steps

1. Open Twisted-Solid.stl in Cura and slice it with supports off.

   ```
   File > Open > Twisted-Solid.stl > Slice
   ```

2. In Preview, find the layers that start in mid-air — these overhangs would droop or fail.

   ```
   Preview > layer slider — spot unsupported islands
   ```

3. Enable support generation.

   ```
   Print Settings > Support > Generate Support ✔
   ```

4. Set placement to Touching Buildplate first; compare with Everywhere and note the difference in Preview.

   ```
   Support Placement — Touching Buildplate vs Everywhere
   ```

5. Keep the support overhang angle at 45–50° so only genuinely steep faces get support.

   ```
   Support Overhang Angle — 50 degrees
   ```

6. Slice again and compare time and material with the unsupported version, then print.

   ```
   Slice > Save to Disk > print
   ```

7. Snap the supports off with pliers, working from the edges inward, and inspect the supported surfaces.

   ```
   Needle-nose pliers > remove supports
   ```

8. Repeat the analysis with wedge.stl and cube20-sideways-hole.stl; for each, compare adding support with rotating the model to make the geometry self-supporting.

   ```
   Open both models > Rotate > Slice > Preview > record decision
   ```


## Evidence to capture

- Three-model support decision table: risk, best orientation, support placement and reason.
- Before/after Cura Preview screenshots for Twisted-Solid.stl with supports off and on.
- Photo of the printed benchmark after support removal, with scarring annotated.


## Test it

Your decision table correctly identifies unsupported islands and distinguishes when support is necessary from when reorientation is the better fix; the Twisted Solid print completes with removable support and only minor underside scarring.

## Files in this folder

- `twist.stl` — Core sample model used by the lab procedure.
- `Twisted-Solid.stl` — 49 mm twisted benchmark with steep faces and changing overhangs.
- `wedge.stl` — Simple 60 mm overhang-angle benchmark for reading progressive underside quality.
- `cube20-sideways-hole.stl` — Sideways-hole benchmark for comparing support, bridging and reorientation.
