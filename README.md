# SUTD DTP III Project: Multiple Linear Regression Model
> [!NOTE]
> For more detailed documentation about the findings, please refer
> to the GitHub Repo Wiki for reference.

---
## About the Project
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

---
## Objectives
- [ ] Identify Anomalies, Normalize Data, etc.
- [X] Predict the growth of the dataset in the next 10 years.

---
## Libraries Used
- See `requirements.txt` for more info.

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
   
---
## File Structure
```plaintext
Lorem ipsum dolor sit amet, consectetur adipiscing e
lit, sed do eiusmod tempor incididunt ut labore et d
olore magna aliqua. Ut enim ad minim veniam, quis no
strud exercitation ullamco laboris nisi ut aliquip e
x ea commodo consequat. Duis aute irure dolor in rep
rehenderit in voluptate velit esse cillum.
```

---
## Team Members
- Randy Soh Jun Jie
- Teh Wu Rui
- Daniel Parsaulian Napitu
- Ng Zhan Kang

---
## References
- [IDK WHATS THIS](www.google.com)