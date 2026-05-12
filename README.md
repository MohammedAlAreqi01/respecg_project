# Respiratory Rate from ECG

A computational pipeline for extracting respiratory rate from single-lead ECG
recordings, validated against the PhysioNet Apnea-ECG database.

## Methods

Two independent ECG-derived respiration techniques are implemented:

- **Tachogram (RSA-based):** R-peak detection (Pan-Tompkins) → R-R interval
  series → cubic spline resampling to 4 Hz → sliding-window Welch spectral
  analysis → dominant peak in the 0.15–0.4 Hz respiratory band.
- **EDR (amplitude-based):** R-peak amplitudes → cubic spline resampling →
  same spectral pipeline.

## Results summary

Across 8 records (4 apneic, 4 healthy controls):

|         | Tachogram      | EDR            |
|---------|----------------|----------------|
| Apneic  | 54.3 ± 11.9%   | 62.6 ± 5.2%    |
| Healthy | 77.7 ± 6.0%    | 69.0 ± 12.7%   |

(% windows producing a respiratory rate in the plausible 12–20 bpm adult range.)

Tachogram method shows clearer between-group separation; EDR is more sensitive
to between-subject recording variation.

## Setup

```bash
conda env create -f environment.yml
conda activate respecg
```

Download the Apnea-ECG database from
https://physionet.org/content/apnea-ecg/1.0.0/ and place all `.dat`/`.hea`/
`.apn`/`.qrs` files in a `data/` folder at the project root.

## Usage

All analysis is in `week1.ipynb`, organised by week using markdown section headers:

- **Week 1:** Data loading, ECG visualisation, apnea event overlay
- **Week 2:** Bandpass filtering, Pan-Tompkins R-peak detection, validation
  against `.qrs` annotations
- **Week 3:** Tachogram-based respiratory rate extraction with sliding-window
  Welch spectral analysis
- **Week 4:** Multi-record validation and EDR (amplitude modulation) method
  comparison

Open the notebook from the project root:

```bash
jupyter notebook week1.ipynb
```

## Course

COMP90072, The Art of Scientific Computing.