# Memo commands for detecting Double Pulsar backdoor
# Run as root

# Download NSE script
wget -P /usr/share/nmap/scripts https://raw.githubusercontent.com/nmap/nmap/master/scripts/smb-double-pulsar-backdoor.nse

# Check infected machines
nmap -p445 --script smb-double-pulsar-backdoor 192.168.1.103
