# Download NSE script
wget -P /usr/share/nmap/scripts https://raw.githubusercontent.com/Waffles-2/SambaCry/master/CVE-2017-7494.nse

# Check vulnerable machines
nmap -p445 --script CVE-2017-7494 192.168.1.103
