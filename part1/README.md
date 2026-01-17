# TOPSIS Implementation in Python

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method originally developed by Hwang and Yoon in 1981.

---

## Author Information
- **Name:** Your Name
- **Roll No:** Your Roll Number

---

## Table of Contents
1. [Methodology](#methodology)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Input/Output Format](#inputoutput-format)
5. [Result Table](#result-table)
6. [Result Graph](#result-graph)
7. [Error Handling](#error-handling)

---

## Methodology

### What is TOPSIS?

TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the **Positive Ideal Solution (PIS)** and the longest geometric distance from the **Negative Ideal Solution (NIS)**.

### Step-by-Step Algorithm

#### Step 1: Construct the Decision Matrix

Create an evaluation matrix consisting of m alternatives and n criteria:

```
        C1    C2    C3   ...   Cn
A1    [x11   x12   x13  ...   x1n]
A2    [x21   x22   x23  ...   x2n]
...
Am    [xm1   xm2   xm3  ...   xmn]
```

#### Step 2: Normalize the Decision Matrix

Apply **Vector Normalization** to make the criteria dimensionless and comparable:

$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

Where:
- $x_{ij}$ = Original value of alternative i for criterion j
- $r_{ij}$ = Normalized value
- $m$ = Number of alternatives

#### Step 3: Calculate the Weighted Normalized Decision Matrix

Multiply each column of the normalized matrix by its corresponding weight:

$$v_{ij} = w_j \times r_{ij}$$

Where:
- $w_j$ = Weight of criterion j (given by user)
- $v_{ij}$ = Weighted normalized value

#### Step 4: Determine the Ideal Best and Ideal Worst Solutions

**Ideal Best (V+):**
- For **Benefit criteria** (+): $V_j^+ = \max(v_{ij})$ (maximum value in column)
- For **Cost criteria** (-): $V_j^+ = \min(v_{ij})$ (minimum value in column)

**Ideal Worst (V-):**
- For **Benefit criteria** (+): $V_j^- = \min(v_{ij})$ (minimum value in column)
- For **Cost criteria** (-): $V_j^- = \max(v_{ij})$ (maximum value in column)

#### Step 5: Calculate Separation Measures

**Distance from Ideal Best (S+):**

$$S_i^+ = \sqrt{\sum_{j=1}^{n} (v_{ij} - V_j^+)^2}$$

**Distance from Ideal Worst (S-):**

$$S_i^- = \sqrt{\sum_{j=1}^{n} (v_{ij} - V_j^-)^2}$$

#### Step 6: Calculate the Relative Closeness (TOPSIS Score)

$$C_i = \frac{S_i^-}{S_i^+ + S_i^-}$$

Where:
- $0 \leq C_i \leq 1$
- $C_i = 1$ if the alternative is closest to the ideal best
- $C_i = 0$ if the alternative is closest to the ideal worst
- **Higher score = Better alternative**

#### Step 7: Rank the Alternatives

Rank all alternatives in descending order of their TOPSIS scores. The alternative with the highest score gets Rank 1.

---

## Installation

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/topsis-implementation.git
cd topsis-implementation
```

---

## Usage

### Command Line Interface

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Example

```bash
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" output-result.csv
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| InputDataFile | Path to input CSV file | `data.csv` |
| Weights | Comma-separated weights for each criterion | `"1,1,1,2,1"` |
| Impacts | Comma-separated impacts (`+` or `-`) for each criterion | `"+,+,-,+,-"` |
| ResultFileName | Path for output CSV file | `output-result.csv` |

### Google Colab

Open the `TOPSIS_Implementation.ipynb` notebook in Google Colab:
1. Upload the notebook to your Google Drive
2. Open with Google Colab
3. Run all cells

---

## Input/Output Format

### Input File Format (data.csv)

| Fund Name | P1 | P2 | P3 | P4 | P5 |
|-----------|------|------|-----|------|-------|
| M1 | 0.67 | 0.45 | 6.5 | 42.6 | 12.56 |
| M2 | 0.6 | 0.36 | 3.6 | 53.3 | 14.47 |
| M3 | 0.82 | 0.67 | 3.8 | 63.1 | 17.1 |
| M4 | 0.6 | 0.36 | 3.5 | 69.2 | 18.42 |
| M5 | 0.76 | 0.58 | 4.8 | 43 | 12.29 |
| M6 | 0.69 | 0.48 | 6.6 | 48.7 | 14.12 |
| M7 | 0.79 | 0.62 | 4.8 | 59.2 | 16.35 |
| M8 | 0.84 | 0.71 | 6.5 | 34.5 | 10.64 |

**Requirements:**
- First column: Alternative names/identifiers
- Second column onwards: Numeric criterion values
- Minimum 3 columns required

### Output File Format (output-result.csv)

| Fund Name | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank |
|-----------|------|------|-----|------|-------|--------------|------|
| M1 | 0.67 | 0.45 | 6.5 | 42.6 | 12.56 | 0.42 | 5 |
| M2 | 0.6 | 0.36 | 3.6 | 53.3 | 14.47 | 0.52 | 3 |
| M3 | 0.82 | 0.67 | 3.8 | 63.1 | 17.1 | 0.64 | 2 |
| M4 | 0.6 | 0.36 | 3.5 | 69.2 | 18.42 | 0.71 | 1 |
| M5 | 0.76 | 0.58 | 4.8 | 43 | 12.29 | 0.33 | 7 |
| M6 | 0.69 | 0.48 | 6.6 | 48.7 | 14.12 | 0.35 | 6 |
| M7 | 0.79 | 0.62 | 4.8 | 59.2 | 16.35 | 0.53 | 3 |
| M8 | 0.84 | 0.71 | 6.5 | 34.5 | 10.64 | 0.28 | 8 |

---

## Result Table

Example results with weights = [1, 1, 1, 2, 1] and impacts = [+, +, -, +, -]:

| Alternative | TOPSIS Score | Rank | Interpretation |
|-------------|--------------|------|----------------|
| M4 | 0.71 | 1 | Best alternative |
| M3 | 0.64 | 2 | Second best |
| M7 | 0.53 | 3 | Third best |
| M2 | 0.52 | 4 | - |
| M1 | 0.42 | 5 | - |
| M6 | 0.35 | 6 | - |
| M5 | 0.33 | 7 | - |
| M8 | 0.28 | 8 | Worst alternative |

### Interpretation

- **M4 (Rank 1):** Has the highest TOPSIS score of 0.71, indicating it is closest to the ideal solution and farthest from the worst solution.
- **M8 (Rank 8):** Has the lowest score of 0.28, making it the least preferred alternative.

---

## Result Graph

The implementation generates two visualizations:

### 1. TOPSIS Scores Bar Chart
![TOPSIS Scores](topsis_results.png)

A bar chart showing the TOPSIS score for each alternative. The color gradient (red to green) indicates the relative performance:
- **Green:** Higher scores (better alternatives)
- **Red:** Lower scores (worse alternatives)

### 2. Ranked Alternatives Horizontal Bar Chart

A horizontal bar chart showing alternatives sorted by their TOPSIS scores with rank labels, providing a clear visual comparison of all alternatives.

---

## Error Handling

The program validates inputs and handles the following errors:

| Error | Message |
|-------|---------|
| Incorrect number of parameters | `Error: Incorrect number of parameters.` |
| File not found | `Error: File 'filename' not found.` |
| Less than 3 columns | `Error: Input file must contain three or more columns.` |
| Non-numeric values | `Error: Column 'X' contains non-numeric values.` |
| Mismatched weights count | `Error: Number of weights (X) must match number of criteria (Y).` |
| Mismatched impacts count | `Error: Number of impacts (X) must match number of criteria (Y).` |
| Invalid impact value | `Error: Impacts must be either '+' or '-'. Found: 'X'` |

---

## File Structure

```
topsis-implementation/
├── topsis.py                    # Main command-line program
├── TOPSIS_Implementation.ipynb  # Jupyter notebook for Colab
├── data.csv                     # Sample input data
├── output-result.csv            # Sample output (generated)
├── topsis_results.png           # Result visualization (generated)
├── README.md                    # This documentation
└── .gitignore                   # Git ignore file
```

---

## References

1. Hwang, C.L.; Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. New York: Springer-Verlag.
2. Behzadian, M., et al. (2012). "A state-of-the-art survey of TOPSIS applications." *Expert Systems with Applications*, 39(17), 13051-13069.

---

## License

This project is licensed under the MIT License.
