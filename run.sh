#!/bin/bash
source venv/bin/activate

pip install -r requirements.txt

python generate_lunar_data.py
