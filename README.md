# EUCLID Hyperelasticity 

This repository contains a refactored and modularized version of the EUCLID hyperelasticity code, originally presented as a Jupyter Notebook. The goal of this refactoring is to enhance readability, maintainability, and extensibility, making it suitable for academic research and engineering applications.

## Project Structure

```
EUCLID (THESIS)/
├── EUCLID/
│   ├── __init__.py
│   ├── constants.py
│   ├── data_loader.py
│   ├── kinematics.py
│   ├── features.py
│   ├── assembly.py
│   ├── euclid_solver.py
│   └── main.py
├── docs/
│   └── physics_and_math.md
└── README.md
```

## Modules Overview

- `constants.py`: Defines global parameters and constants used throughout the project.
- `data_loader.py`: Handles the loading and preprocessing of FEM data, including the `Reaction` class.
- `kinematics.py`: Contains functions for computing kinematic quantities such as Cauchy-Green strain, Jacobian, and strain invariants.
- `features.py`: Implements the computation of material features and their derivatives, central to the EUCLID method.
- `assembly.py`: Provides utilities for assembling matrices and vectors, crucial for constructing the linear equations.
- `euclid_solver.py`: Encapsulates the core EUCLID algorithm, including sparse regression for material model discovery.
- `main.py`: The main entry point for executing the EUCLID hyperelasticity analysis.


Attribution & Acknowledgments
This repository is an independent extension and structural refactoring focused on hyperelastic material models. We deeply acknowledge and credit the original creators of the EUCLID methodology for their foundational open-source work:

Original EUCLID Framework & CodeBase: Available at [EUCLID Code Website](https://euclid-code.github.io/) and their Official GitHub Repository.

Reference Dataset: Utilized from the public Zenodo record available at [Zenodo Data](https://zenodo.org/records/18617429?preview_file=force_vfm.csv).

