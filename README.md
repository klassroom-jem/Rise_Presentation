Klassroom Software Documents
=================================

This repository contains structured documents and large notebooks covering Machine Learning, Python, and SQL.

The project uses RISE to enable Jupyter Notebook slideshows.
Note: Jupyter and Notebook versions have been rolled back for compatibility (see requirements.txt).

---------------------------------
Project Structure
---------------------------------
- Documents: Each organized into 5 sections
- Notebooks: ML, Python, and SQL notebooks
- Rise: Enables slideshow functionality
- Installation Files: Located in Rise/Rise_Installation

---------------------------------
Installation
---------------------------------
1. Clone the repository:
   git clone <repo-url>
   cd <repo-folder>

2. Set up the environment:
   - Go to: Rise/Rise_Installation
   - Copy the following files into the project root:
       * install_env.bat
       * requirements.txt
   - Run:
       install_env.bat
     (This creates a virtual environment and installs dependencies)

---------------------------------
Running Jupyter with RISE
---------------------------------
1. Activate the virtual environment
   (On Windows, this is handled by the .bat script)

2. Start Jupyter Notebook:
   start_jupyter.bat

3. Open a notebook (.ipynb) in your browser

4. Launch slideshow mode:
   - Click the slideshow icon in the toolbar
   - OR press Alt + R

---------------------------------
Additional Notes
---------------------------------
- Detailed installation workflow:
  Rise/Rise_Installation Steps.txt

- If slideshow mode does not appear:
  Ensure Jupyter + Notebook versions match requirements.txt

---------------------------------
Ready to explore and present notebooks as interactive slideshows!
