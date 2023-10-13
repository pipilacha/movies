echo "Creating a Python virtual environment"
if [ -d venv2 ]; then python3 -m venv ./venv; else echo "Virtual env already exists"; fi

echo ""
echo "Installing Python depenencies..."
source ./venv/bin/activate && python3 -m pip install --upgrade pip wheel
source ./venv/bin/activate && pip3 install -r requirements.txt
echo ""

echo ""
echo "Copying Postgres service file to ~"
cp -v .pg_service.conf ~
echo "Remember to add password file. .moviesapp_db_pgpass  content: localhost:5432:moviesapp:moviesapp:password"
echo ""

echo ""
echo "****************************************"
echo " Dev Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'source ./venv/bin/activate' to switch this terminal to the venv"
echo ""