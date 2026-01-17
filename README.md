# TOPSIS Implementation Project

A comprehensive implementation of **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** - a multi-criteria decision analysis method.

**Author:** Yajat Pahuja
**Roll No:** 102303185

---

## Table of Contents

- [Overview](#overview)
- [Part 1: Command Line Implementation](#part-1-command-line-implementation)
- [Part 2: PyPI Package](#part-2-pypi-package)
- [Part 3: Web Service](#part-3-web-service)
- [TOPSIS Methodology](#topsis-methodology)
- [Project Structure](#project-structure)

---

## Overview

This project implements TOPSIS in three different formats:

| Part | Description | Link |
|------|-------------|------|
| **Part 1** | Command-line Python script | [part1/](part1/) |
| **Part 2** | Published PyPI package | [pypi.org/project/Topsis-Yajat-102303185](https://pypi.org/project/Topsis-Yajat-102303185/) |
| **Part 3** | Web service with email | [topsis-web-service.onrender.com](https://topsis-web-service.onrender.com) |

---

## Part 1: Command Line Implementation

A Python script that performs TOPSIS analysis from the command line.

### Usage

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example

```bash
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" output.csv
```

### Input Format

```
Fund Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.5,42.6,12.56
M2,0.6,0.36,3.6,53.3,14.47
M3,0.82,0.67,3.8,63.1,17.1
...
```

### Output Format

```
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.67,0.45,6.5,42.6,12.56,0.42,5
M2,0.6,0.36,3.6,53.3,14.47,0.52,3
...
```

### Validations

- Correct number of parameters
- File not found handling
- Minimum 3 columns required
- Numeric values validation
- Weights/Impacts count match
- Impacts must be `+` or `-`

---

## Part 2: PyPI Package

A published Python package available on PyPI.

### Installation

```bash
pip install Topsis-Yajat-102303185
```

### Command Line Usage

```bash
topsis data.csv "1,1,1,2,1" "+,+,-,+,-" output.csv
```

### Python Usage

```python
from Topsis_Yajat_102303185 import topsis

topsis("data.csv", "1,1,1,2,1", "+,+,-,+,-", "output.csv")
```

### Package Link

[https://pypi.org/project/Topsis-Yajat-102303185/](https://pypi.org/project/Topsis-Yajat-102303185/)

---

## Part 3: Web Service

A Flask web application that performs TOPSIS analysis and sends results via email.

### Live Demo

[https://topsis-web-service.onrender.com](https://topsis-web-service.onrender.com)

### Features

- File upload interface
- Input validation
- Email delivery of results
- Responsive design

### Screenshot

```
┌─────────────────────────────────────────┐
│         TOPSIS Analysis                 │
├─────────────────────────────────────────┤
│                                         │
│  File Name    [Browse File...]          │
│                                         │
│  Weights      [1,1,1,1          ]       │
│                                         │
│  Impacts      [+,+,-,+          ]       │
│                                         │
│  Email Id     [email@example.com]       │
│                                         │
│            [ Submit ]                   │
│                                         │
└─────────────────────────────────────────┘
```

### Local Setup

```bash
cd part3
pip install flask python-dotenv pandas numpy
python app.py
```

Then open http://127.0.0.1:5000

---

## TOPSIS Methodology

### What is TOPSIS?

TOPSIS is a multi-criteria decision analysis method that identifies the best alternative based on:
- **Shortest distance** from the Positive Ideal Solution (PIS)
- **Longest distance** from the Negative Ideal Solution (NIS)

### Algorithm Steps

```
┌──────────────────────────────────────────────────────────────┐
│                    TOPSIS Algorithm                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Step 1: Create Decision Matrix                              │
│     ┌─────────────────────────────┐                          │
│     │    C1   C2   C3   C4        │                          │
│     │ A1 [x11  x12  x13  x14]     │                          │
│     │ A2 [x21  x22  x23  x24]     │                          │
│     │ A3 [x31  x32  x33  x34]     │                          │
│     └─────────────────────────────┘                          │
│                    ↓                                         │
│  Step 2: Normalize Matrix                                    │
│     rij = xij / √(Σ xij²)                                    │
│                    ↓                                         │
│  Step 3: Apply Weights                                       │
│     vij = wj × rij                                           │
│                    ↓                                         │
│  Step 4: Find Ideal Solutions                                │
│     V+ = (max benefit, min cost)                             │
│     V- = (min benefit, max cost)                             │
│                    ↓                                         │
│  Step 5: Calculate Distances                                 │
│     S+ = √(Σ(vij - vj+)²)                                    │
│     S- = √(Σ(vij - vj-)²)                                    │
│                    ↓                                         │
│  Step 6: Calculate Score                                     │
│     Ci = S- / (S+ + S-)                                      │
│                    ↓                                         │
│  Step 7: Rank (Higher Score = Better)                        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Key Formulas

| Step | Formula | Description |
|------|---------|-------------|
| Normalization | `rij = xij / √(Σ xij²)` | Vector normalization |
| Weighting | `vij = wj × rij` | Apply weights |
| Distance to Best | `S+ = √(Σ(vij - vj+)²)` | Euclidean distance |
| Distance to Worst | `S- = √(Σ(vij - vj-)²)` | Euclidean distance |
| TOPSIS Score | `Ci = S- / (S+ + S-)` | Relative closeness |

### Impact Types

| Impact | Meaning | Ideal Best | Ideal Worst |
|--------|---------|------------|-------------|
| `+` (Benefit) | Higher is better | Maximum | Minimum |
| `-` (Cost) | Lower is better | Minimum | Maximum |

---

## Project Structure

```
data_science_1/
│
├── README.md                 # This file
├── requirements.txt          # Dependencies
├── .gitignore
│
├── part1/                    # Command Line Implementation
│   ├── topsis.py
│   ├── data.csv
│   └── README.md
│
├── part2/                    # PyPI Package
│   ├── Topsis_Yajat_102303185/
│   │   ├── __init__.py
│   │   └── topsis.py
│   ├── pyproject.toml
│   ├── LICENSE
│   └── README.md
│
└── part3/                    # Web Service
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── requirements.txt
    └── README.md
```

---

## Quick Links

| Resource | Link |
|----------|------|
| PyPI Package | [pypi.org/project/Topsis-Yajat-102303185](https://pypi.org/project/Topsis-Yajat-102303185/) |
| Web Service | [topsis-web-service.onrender.com](https://topsis-web-service.onrender.com) |
| GitHub Repo | [github.com/YajatPahuja/data_science_1](https://github.com/YajatPahuja/data_science_1) |

---

## License

MIT License

---

*Made with Python, Flask, and NumPy*
