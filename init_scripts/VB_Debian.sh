# VBox Additions
apt update
apt dist-upgrade -y
apt install build-essential dkms gcc linux-headers-$(uname -r)
mkdir /tmp/vboxadd
cp /media/cdrom0/VBoxLinuxAdditions.run /tmp/vboxadd/
cd /tmp/vboxadd/
chmod +x ./VBoxLinuxAdditions.run
./VBoxLinuxAdditions.run
reboot

# Tools
apt install git python terminator apache2 -y
