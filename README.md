# spray-and-prey
Chrome extension that personalizes your resume for each job application using LLMs

## Installation
1. Clone the repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable developer mode
4. Click on `Load unpacked` and upload the repository folder
5. The extension should now be installed

## Getting started
1. Modify the values in `backend/constants.py` to match your own
2. Change resume in input folder to your own resume

## Starting local server
1. Go to the `backend` directory
2. Run `uvicorn main:app --reload` to start the server
3. Use chrome extension as intended



