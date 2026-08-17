# Lab 16 — Post-Processing — Support Removal and Sanding

**Course:** Innovating Product Development with 3D Printing and Additive Manufacturing (TGS-2022017597)  
**Topic 03:** Process Improvement for AM  
**TSC objective:** A5 — apply post-processing to lift the quality of an FDM part

## Goal

Print the vase tilted so it needs supports, remove them cleanly, then sand the scarred surfaces through progressive grits to a smooth finish.

## What you'll build

A tilted-print vase taken from raw support-scarred print to a smooth finished part.

**Tools:** Ultimaker Cura, open vase.stl, FDM printer, pliers, sandpaper 120→400 grit

## Steps

1. Open 'open vase.stl' in Cura and rotate it 15–20° off vertical so one side overhangs.

   ```
   Rotate — 15–20° tilt
   ```

2. Enable supports (Touching Buildplate) and slice.

   ```
   Support ▸ Generate ✔ ▸ Touching Buildplate
   ```

3. Print the tilted vase with its supports.

   ```
   Save to Disk ▸ print
   ```

4. Snap the supports off with pliers, working from the outer edge toward the part.

   ```
   Needle-nose pliers
   ```

5. Sand the support-scarred areas with 120-grit, then step through 240 → 400 grit in circular motions.

   ```
   Sandpaper 120 → 240 → 400
   ```

6. Optionally wet-sand at 400 grit for a satin finish, and compare the treated side with an untouched area.

   ```
   Wet sand + compare
   ```


## Test it

The support side of the vase is smooth to the touch with no visible scars from a normal viewing distance — the part looks moulded rather than printed.

## Files in this folder

- `open vase.stl`
