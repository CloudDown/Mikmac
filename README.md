# Mikmac.py

Mikmac.py is a Python script for changing the MAC address of a network interface. This script provides different modes of operation, allowing you to change the MAC address once, in a chain, or using settings from a text file.

## Modes

### 1. Default Mode
In this mode, the script changes the MAC address once. You input the MAC address and the WiFi card.

### 2. Chain Mode
This mode allows you to continuously change the MAC address at regular intervals. You can specify the delay between each change, the path to a text file containing MAC addresses, and the WiFi card.

### 3. Chain with Python File Settings
Similar to Chain Mode, but the settings (text file path, delay, WiFi card) are specified within the Python script.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Mikmac.py.git
   cd Mikmac.py
   sudo python3 Mikmac.py

    Follow the on-screen instructions to choose the mode and provide necessary details.

## Requirements

    Python 3.x
    macchanger

## Customization

Feel free to customize the script according to your needs. You can modify the default variables, such as def_delay, def_way, and def_card, within the script.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Special thanks to the developers of macchanger for providing the underlying functionality.
   

