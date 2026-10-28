A virtual environment is an isolated environment for a Python project that keeps its installed packages separate from other Python projects. This prevents dependency conflicts.

Windows PowerShell

Create a virtual environment folder:

python -m venv .voice-ai-venv

View both visible and hidden content in the current folder:

Get-ChildItem -Force

Activate the virtual environment:

.voice-ai-venv\Scripts\Activate.ps1

Before you create a requirements.txt file, be sure that the
virtual environment for this particular project is activated.

Create a requirements.txt file:

pip freeze > requirements.txt