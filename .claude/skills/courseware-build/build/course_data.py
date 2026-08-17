"""
SINGLE SOURCE OF TRUTH — course metadata.

Innovating Product Development with 3D Printing and Additive Manufacturing
(TGS-2022017597) — WSQ 2-day course, Tertiary Infotech Academy Pte Ltd.

Every artifact (PPT, LP, LG, LG.md, labs) is generated from this file plus
data_domain1.py … data_domain3.py so they stay 100% aligned with the
TSC (Additive Manufacturing, PRE-OPR-4012-1.1) and the assessments.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Innovating Product Development with 3D Printing and Additive Manufacturing"
SHORT_TITLE  = "Innovating Product Development with 3D Printing and Additive Manufacturing"
COURSE_CODE  = "TGS-2022017597"
VERSION      = "v8.0"
VERSION_DATE = "18 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 2

# ------------------------------------------------------------------ skills framework
TSC_TITLE = "Additive Manufacturing"
TSC_CODE  = "PRE-OPR-4012-1.1"
TSC_ABILITIES = [
    "A1: Analyse and determine material considerations of components to be manufactured",
    "A2: Analyse process-related issues for using DMLS, SLS, SLM, powder bed and inkjet head, and/or 3D printing for AM",
    "A3: Determine processes and procedures for manufacturing metallic and non-metallic components using AM",
    "A4: Evaluate use of reverse engineering processes for components through 3D scanning and subsequent AM",
    "A5: Apply optimisation techniques to improve efficiency of AM processes and product quality",
    "A6: Assess the impact of manufacturing process improvements on business operations",
]
TSC_KNOWLEDGE = [
    "K1: AM characteristics, techniques and systems",
    "K2: Requirements of different AM processes",
    "K3: Factors to be considered when selecting AM solutions",
    "K4: Impact of AM on manufacturing operations",
    "K5: Methods for reviewing AM performance",
    "K6: Benefits and trade-offs of AM",
    "K7: Methods of ensuring long-term sustainability of AM",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Analyze the AM and evaluate the use of reverse engineering using 3D scanning",
    "LO2: Analyze the issues and determine the requirements for AM processes",
    "LO3: Apply AM optimization techniques and assess the impact of process improvement",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Overview of Additive Manufacturing and 3D Scanning",
         subtitle="AM systems · material considerations · benefits & trade-offs · 3D scanning and reverse engineering  (K1, K3, K6 · A1, A4)",
         weighting="LO1",
         concepts=[
            ("Additive manufacturing", "Builds parts layer by layer directly from a CAD file — no part-specific tools, dies or molds."),
            ("Seven process families", "Material extrusion, vat photopolymerisation, powder bed fusion, material jetting, binder jetting, directed energy deposition, sheet lamination."),
            ("Material considerations", "Mechanical/thermal properties, design complexity, volume, post-processing and cost drive the choice of AM solution."),
            ("Benefits & trade-offs", "Design freedom, rapid prototyping and low-waste versus slower throughput, material limits and post-processing."),
            ("3D scanning", "Captures real-world geometry so worn or legacy parts can be reverse-engineered into CAD and re-manufactured with AM."),
            ("Design for AM", "Fusion 360 extrude, sweep, loft and revolve; stress concentration and tolerance-aware design."),
         ]),
    dict(num=2, code="02",
         title="Process Related Issues for AM",
         subtitle="Printer hardware · slicing · adhesion · extrusion · temperature · materials  (K2, K4 · A2, A3)",
         weighting="LO2",
         concepts=[
            ("Five issue sources", "Printer hardware, materials, printing process conditions, environment conditions and design-caused issues."),
            ("Slicing", "The slicer converts an STL model into G-code printer instructions — settings decide quality, time and strength."),
            ("Bed adhesion", "Geometry, nozzle distance, platform surface and platform temperature govern whether the first layer sticks."),
            ("Extrusion issues", "Over/under-extrusion, retraction, oozing and stringing — diagnosed from the printed surface."),
            ("Temperature window", "Each material has a working temperature band; too low fails adhesion, too high causes sag, strings and smells."),
            ("Material requirements", "ABS, PLA, PETG and Nylon each demand specific temperatures, beds, ventilation and storage."),
         ]),
    dict(num=3, code="03",
         title="Process Improvement for AM",
         subtitle="Infill · surface quality · supports · post-processing · business impact  (K5, K7 · A5, A6)",
         weighting="LO3",
         concepts=[
            ("Infill optimisation", "Perimeters, infill pattern and density trade strength against material use and print time."),
            ("Surface quality", "Layer height, top thickness, ironing and fuzzy skin control the finish and the print duration."),
            ("Support strategy", "Orient parts to minimise supports; add them only where overhangs demand, and plan their removal."),
            ("Post-processing", "FDM, SLS, SLA and metal parts each have a defined finishing chain — from support removal to plating."),
            ("Business impact", "Measure speed, quality, material use, cost and user feedback before and after every process change."),
            ("Sustainability", "Calibration, training, sustainable materials and stakeholder collaboration keep AM operations viable long-term."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Additive Manufacturing, 3D Scanning and Design for AM",
    2: "Process Issues, Process Improvement and Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — scenario-based practical tasks, 90 minutes, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

PRACTICE_EXAM_URL = "https://exams.tertiaryinfotech.com"
LMS_URL = "https://lms-tms.tertiaryinfotech.com"
