echo "Creating a Python virtual environment"
if [ -d venv ]; then python3 -m venv ./venv; else echo "Virtual env already exists"; fi

echo ""
echo "Installing Python depenencies..."
source ./venv/bin/activate && python3 -m pip install --upgrade pip wheel
source ./venv/bin/activate && pip3 install -r requirements.txt
echo ""

echo ""
echo "****************************************"
echo " Dev Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'source ./venv/bin/activate' to switch this terminal to the Virtual env"
echo ""