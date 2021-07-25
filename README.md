# silly_house

First of all
```
git clone https://github.com/kostorub/silly_house.git
cd ./silly_house
chmod +x configure.sh
./configure.sh
```

To start application run
```
source venv/bin/activate
python3 automated_house/app.py
```

For the country house
When using Huawei modem add this at the end of /etc/rc.local for enable access to the camera at eth0

```
ip addr add 192.168.2.1/24 dev eth0
```
If there is very unstable internet connection use this in "sudo crontab -e"
```
0 */3 * * * systemctl restart openvpn-client@client1
```