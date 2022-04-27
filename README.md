# Traffic sign classification web app

Implemented CNN with help using `keras` ([link](https://colab.research.google.com/drive/1V8Dmem-VzrjPktkpHtWMKEDwoBP9cZwC?usp=sharing) to Google Colab notebook).

## How to run locally

```bash
# Cloning the repository
git clone https://github.com/ernurator/ML-Final-2022
cd ML-Final-2022

# Skip if virtualenv is installed
python3 -m pip install virtualenv

# Create virtual env
python3 -m virtualenv .venv

# Install all required libraries
pip install -r requirements.txt

# Run the web app
flask run
# Then open http://127.0.0.1:5000 in browser
```
