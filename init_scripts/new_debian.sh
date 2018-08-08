# Part 1
apt update && apt -y upgrade
apt install sudo git
useradd -m pixis

# Part 2
passwd pixis
usermod -a -G sudo pixis
chsh -s /bin/bash pixis
