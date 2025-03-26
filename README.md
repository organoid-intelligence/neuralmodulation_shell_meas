# Neuromodulation in neural organoids with shell MEAs
This repository contains scripts, code, and supporting documents to support the manuscript "Neuromodulation in neural organoids with shell MEAs."

Neural organoids (NOs) have emerged as important tissue engineering models for brain sciences and biocomputing. Establishing reliable relationships between stimulation and recording traces of electrical activity is essential to monitor the functionality of NOs, especially as it relates to realizing biocomputing paradigms such as reinforcement learning or stimulus discrimination. While researchers have demonstrated neuromodulation in NOs, they have primarily used 2D microelectrode arrays (MEAs) with limited access to the entire 3D contour of the NOs. Here, we report neuromodulation using tiny mimics of macroscale EEG caps or shell MEAs. Specifically, we observe that stimulating current within a specific range (20 to 30 µA) induced a statistically significant increase in neuron firing rate when comparing the activity five seconds before and after stimulation. We observed neuromodulatory behavior using both three- and 16-electrode shells and could generate 3D spatiotemporal maps of neuromodulatory activity around the surface of the NO. Our studies demonstrate a methodology for investigating 3D spatiotemporal neuromodulation in organoids of broad relevance to biomedical engineering and biocomputing.

Authors: Chris Acha, Derosh George, Lauren C. Diaz, Ziwei Ouyang, Dowlette-Mary M. Alam El Din, Hrishikesh Surlekar, Babak Moghadas, Eva Loftus, Gandhali M. Mangalvedhekar, Pratyush Sai R. Rayasam, Yu-Chiao Lai, Lena Smirnova, Brian S. Caffo, Erik C. Johnson, David H. Gracias

This repository contains Jupyter Notebooks in the folder 'notebooks' for replicating figures and analysis from this manuscript. 

## System Requirements
This project uses Python scripts and Jupyter notebooks, with additional open source dependences. No non-standard hardware is required (and no GPUs are required), and this repository should allow for cross-platform support. This code has been tested on Mac OSX Sonoma using Python >3.10 and 
jupyterlab 4.3.6.

## Installation
Installation through [Conda](https://anaconda.org/anaconda/conda) and [Pip](https://pypi.org/project/pip/) is recommended
```
conda create -n shell_electrodes Python==3.10
conda activate shell_electrodes
pip install -r requirements.txt
```
This typically takes 1-2 minutes.

## Demo and Running the Code
Notebooks can be found in the notebooks subdirectory, organized by figure from the manuscript. Each notebook contains instructions for running the code, and contains example output from the script. 

By running the command 
```
jupyter notebook
```
In this repository, a browser-based jupyter 

Each notebook should take 1-2 minutes to process on a standard workstation.

## Reproduction
Data to support this analysis can be found at: https://dandiarchive.org/dandiset/001336/draft
Data should be downloaded and placed in a 'data' subfolder in this directory.
Each notebook contains instrucitons for re-running analysis given these data. 

## License
These notebooks are available under the open-source MIT license. 