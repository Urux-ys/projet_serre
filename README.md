# Raspbian
  install requierment using pip :
   ```
    [~]# sudo apt update && sudo apt install python-pip

    [~]# git clone https://github.com/Urux-ys/projet_serre.git

    [~]# cd projet_serre/

    [~/projet_serre]# sudo pip install -r requirements.txt

    [~/projet_serre]# sudo python main.py
   ```
 
# hardware 
  use Adafruit I2C ADC module
  and use A0 analog entry for light sensor \n
          A1 analog entry for heat sensor \n
          A3 analog entry for humidity sensor \n
  use pin number 11 for water control \n
                 13 for light control \n
                 15 for heat control  \n


# License 
This project is under the terms of the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
