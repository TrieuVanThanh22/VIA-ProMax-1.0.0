# Via ProMax

Windows desktop application packaged from `Via_ProMax.py`.

## For users

Download the Windows build (`Via_ProMax-Windows.zip`), extract it, and run `Via_ProMax.exe`.
No Python or additional Python packages are required on the user's computer.

## Build locally on Windows

Requirements for the **developer/build machine only**:

1. Install Python 3.12+.
2. Open this folder in Command Prompt.
3. Run `build.bat`.
4. The executable will be created at `dist\\Via_ProMax\\Via_ProMax.exe`.

## Build automatically with GitHub Actions

The repository contains `.github/workflows/build-windows.yml`.

- Push the repository to GitHub.
- Open **Actions → Build Windows EXE → Run workflow**.
- Download the generated `Via_ProMax-Windows` artifact.

To create a GitHub Release automatically, create and push a tag such as `v1.0.0`.

## Important

This repository contains the original application source provided by the project owner. Review the source before making it public if it contains credentials, cookies, access tokens, private URLs, or other secrets.
