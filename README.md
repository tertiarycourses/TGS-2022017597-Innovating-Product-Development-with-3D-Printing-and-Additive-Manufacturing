# Innovating Product Development with 3D Printing and Additive Manufacturing

Build, diagnose and improve additive-manufacturing workflows through Fusion 360, 3D scanning, Cura and evidence-based FDM experiments.

| Course detail | Information |
|---|---|
| Course code | `TGS-2022017597` |
| Programme | WSQ |
| TSC | Additive Manufacturing (`PRE-OPR-4012-1.1`) |
| Duration | 2 days / 16 hours |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-innovating-product-development-with-3d-printing-and-additive-manufacturing.html) |
| Funding | Up to 70% course-fee funding for eligible learners/employers. Eligibility, funding validity and terms apply; verify them on the registration page. |
| Courseware release | v8.1 - 22 August 2026 |

## About the course

This practical course develops the skills to select additive-manufacturing solutions, design and reverse-engineer printable products, diagnose process issues, and improve quality, time and material performance. Learners work with Fusion 360, mobile 3D scanning, Ultimaker Cura and FDM printers, using supplied diagnostic models to connect each slicer decision to visible evidence.

## Learning outcomes

On completion, learners will be able to:

- analyse additive-manufacturing systems and evaluate reverse engineering through 3D scanning;
- analyse process-related issues and determine the requirements for AM processes; and
- apply AM optimisation techniques and assess the impact of process improvements.

## Topics covered

- **Overview of Additive Manufacturing and 3D Scanning:** AM systems, materials, benefits and trade-offs, design for AM, 3D scanning and reverse engineering.
- **Process Related Issues for AM:** printer hardware, slicing, adhesion, supports, extrusion, temperature, cooling and material requirements.
- **Process Improvement for AM:** walls and infill, surface quality, support strategy, post-processing, business impact and long-term sustainability.

## Labs

Each lab folder contains a detailed learner README, a same-basename printable PDF, evidence requirements, acceptance checks and any models or project files needed for the task.

1. [Extrude - Personalised Keychain Token](labs/lab-01-extrude-personalised-keychain-token/README.md)
2. [Sweep - Giant Paper Clip Bookmark](labs/lab-02-sweep-giant-paper-clip/README.md)
3. [Loft - Mini Plant Pot with Custom Rails](labs/lab-03-loft-mini-plant-pot/README.md)
4. [Revolve - Funnel from a 2D Profile](labs/lab-04-revolve-funnel-from-a/README.md)
5. [Tolerance - Container and Lid](labs/lab-05-tolerance-container-and-lid/README.md) - includes Fusion 360, STL and Cura project references.
6. [3D Scan and Print a Real Object](labs/lab-06-3d-scan-and-print/README.md)
7. [Install Cura and Slice Your First Model](labs/lab-07-install-cura-and-slice/README.md) - includes 10 mm and 20 mm calibration cubes.
8. [Bed Adhesion - Skirt vs Brim vs Raft](labs/lab-08-bed-adhesion-skirt-vs/README.md)
9. [Support Structures for Overhangs](labs/lab-09-support-structures-for-overhangs/README.md) - twist, wedge and sideways-hole benchmarks.
10. [Filament Diagnostics - Diameter, Temperature and Flow](labs/lab-10-filament-diagnostics-diameter-temperature/README.md) - retraction and cooling benchmarks.
11. [Perimeters and Infill - Strength vs Speed](labs/lab-11-perimeters-and-infill-strength/README.md) - line-width and matched hole-wall models.
12. [Infill Patterns - Zigzag vs Grid Strength Test](labs/lab-12-infill-patterns-zigzag-vs/README.md) - four supplied optimisation variants.
13. [Layer Height and Top Thickness - Surface Quality](labs/lab-13-layer-height-and-top/README.md) - sloped-face stair-stepping benchmark.
14. [Ironing - Glass-Smooth Top Surfaces](labs/lab-14-ironing-glass-smooth-top/README.md) - detailed Z-block top-surface benchmark.
15. [Fuzzy Skin - Textured Walls on a Vase](labs/lab-15-fuzzy-skin-textured-walls/README.md) - 1.5 mm thin-wall vase diagnostic.
16. [Post-Processing - Support Removal and Sanding](labs/lab-16-post-processing-support-removal/README.md) - mixed-feature finishing benchmark.

## Public package

- `courseware/`: current v8.1 trainer slides as PPTX/PDF, Learner Guide and Lesson Plan as DOCX/PDF, plus the changelog.
- `LG-*.md`: editable Markdown mirror of the Learner Guide.
- `labs/`: 16 self-contained lab folders with Markdown/PDF instructions and learner-facing working files.
- `.claude/skills/courseware-build/`: single-source generators that keep the deck, guide, plan and labs aligned.

The public repository intentionally excludes `assessment/`, `reference/`, credentials, answer keys, archives, QA renders and local configuration. Assessments and answer keys are managed separately on Google Drive; answer keys are trainer-only and are never linked from LMS-TMS or GitHub.

## Rebuilding the courseware

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh
python3 .claude/skills/courseware-build/build/build_labs.py
python3 ~/.agents/skills/courseware-build/scripts/render_activity_markdown_pdfs.py --root labs
```

All artifacts are generated from `.claude/skills/courseware-build/build/course_data.py` and `data_domain1.py` through `data_domain3.py`.

## Provider

Tertiary Infotech Academy Pte Ltd (UEN 201200696W)

Copyright 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
