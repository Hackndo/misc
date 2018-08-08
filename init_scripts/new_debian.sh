# Part 1
apt update && apt -y upgrade
apt install sudo git -y
useradd -m pixis
passwd pixis

# Part 2
usermod -a -G sudo pixis
chsh -s /bin/bash pixis
