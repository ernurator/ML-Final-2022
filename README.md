# Traffic sign classification web app

Implemented CNN for traffic sign classification using `keras` ([link](https://colab.research.google.com/drive/1V8Dmem-VzrjPktkpHtWMKEDwoBP9cZwC?usp=sharing) to Google Colab notebook). [Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) on which the model was trained.

The model recognizes following traffic sign classes:

1. Speed limit [20]
1. Speed limit [30]
1. Speed limit [50]
1. Speed limit [60]
1. Speed limit [70]
1. Speed limit [80]
1. End of speed limit [80]
1. Speed limit [100]
1. Speed limit [120]
1. No passing
1. No trucks passing
1. Right-of-way at intersection
1. Priority road
1. Yield
1. Stop
1. No vehicles
1. No trucks
1. No entry
1. General caution
1. Dangerous curve left
1. Dangerous curve right
1. Double curve
1. Bumpy road
1. Slippery road
1. Road narrows on the right
1. Road work
1. Traffic signals
1. Pedestrians
1. Children crossing
1. Bicycles crossing
1. Beware of ice/snow
1. Wild animals crossing
1. Speed and passing limits end
1. Turn right ahead
1. Turn left ahead
1. Ahead only
1. Go straight or right
1. Go straight or left
1. Keep right
1. Keep left
1. Roundabout
1. End of no passing
1. End of no passing trucks

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
