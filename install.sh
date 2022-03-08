echo ""
echo "Installing..."
echo ""
sudo apt-get update
sudo apt-get install nmap
echo ""
echo "Nmap Successfully Installed."
echo ""
echo "nmap Version : "
nmap --version
clear
echo ""
echo "Loading..."
echo ""
sleep 2
clear
python3 netmap.py