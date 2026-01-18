#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo ""
echo "Setup complete! Virtual environment is activated."
echo ""
echo "To run the demo scripts:"
echo "  python demo_track_sales.py"
echo "  python demo_track_listings.py"
echo ""
echo "To activate the venv later, run: source venv/bin/activate"
