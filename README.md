# SUTD DTP III Project: Multiple Linear Regression Model
> [!NOTE]
> For more detailed documentation about the findings, please refer
> to the GitHub Repo Wiki for reference.

---
## About the Project
The purpose of this project is for you to apply what you have learnt in this course. This includes working with data and visualizing it, create model of linear regression, as well as using metrics to measure the accuracy of your model.

## Project Handout
---
Please find the project handout description [here.](./DDW%20-%20DTP%20III%20-%20Design%20Brief%202025.pdf)

---
## Objectives
- [X] Identify Anomalies, Normalize Data, etc.
- [X] Predict the energy consumption based on features.

---
## Libraries Used
- See `conda-project.yml` for more info.

---
## Local Setup
> [!IMPORTANT]
> The procedures below assume that users are familiar with command-line operations using PowerShell (on Windows) or Bash (on MacOS/Linux). If you are unfamiliar with these tools, please consult their respective documentation before proceeding.
1. Clone the repository to the working directory where you want the cloned directory:
     ```commandline 
     git clone [REPO_URL]
     cd [project-folder]
     ```
2. [Download Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install), then open Anaconda Prompt (Windows) or Terminal (Mac/Linux). Run the following commands, it should download all the necessary libraries already:
     ```commandline
     conda env create --file environment.yml
     conda activate dtp3
     ```
   You should see the word `(dtp3)` in your prompt something like:
     ```commandline
     (dtp3) user $
     ```
   If you ever have to install/uninstall new libraries in future, download/uninstall the library first, and once done, lock the project, so that the environment is reproducible to the team during updates. See more [here](https://www.anaconda.com/docs/tools/working-with-conda/environments#locking-an-environment).
   ```commandline
   conda activate dtp3
   conda [install/uninstall] <WHATEVER LIBRARY YOU HAVE TO INSTALL>
   conda install conda-project
   conda-project lock
   conda env export > environment.yml
   ```
   To deactivate the conda environment, simply type:
   ```commandline
   conda deactivate
   ```
   And in future if you ever want to open the conda environment again, simply type:
   ```commandline
   conda activate dtp3
   ```
3. To run StreamLit, simply go the the main directory of the project and type the following:
   ```commandline
   streamlit run Home.py
   ```
   Open the `Local URL` in your preferred browser. To stop the server, simply press the keybind `Ctrl` + `C`.
   
---
## File Structure
```plaintext
|
|-data
| |-Energy_Consumption_Dataset.csv
| |-energyConsumption.xlsx
|-pages
| |-Make Predictions.py
| |-View Dataset.py
|-training
| |-Project Template.ipynb
| |-multiRegressionModel.npz
|-.condarc
|-.gitignore
|-conda-lock.default.yml
|-conda-project.yml
|-DDW - DTP III - Design Brief 2025.pdf
|-environment.yml
|-hepler.py
|-Home.py
|-LICENSE
|-README.md
```

---
## Team Members
- Randy Soh Jun Jie
- Teh Wu Rui
- Daniel Parsaulian Napitu
- Ng Zhan Kang

---
## References
- [Multi Linear Regression(Energy Consumption Data)](https://www.kaggle.com/code/devsurakshitkapoor/multi-linear-regression-energy-consumption-data)
- [SUTD DDW Mini Project 1: Sorting App](https://data-driven-world.github.io/2023/projects/sorting-app)
- [SUTD DDW Mini Project 2: Math Quiz App](https://data-driven-world.github.io/2023/projects/calculator-app)