# BE SURE TO REPLACE F: WITH YOUR USB PATH

import os
import shutil

# Define the origin folder
origin_folder = "F:/ROMS"

# Define the destination folders for each prefix
destinations = {
    'nes': os.path.join("F:/", 'FC'),
    'snes': os.path.join("F:/", 'SFC'),
    'pce': os.path.join("F:/", 'SFC'),
    'col': os.path.join("F:/", 'FC'),
    'a26': os.path.join("F:/", 'GB'),
    'a5200': os.path.join("F:/", 'GB'),
    'lnx': os.path.join("F:/", 'GB'),
    'int': os.path.join("F:/", 'GB'),
    'gb': os.path.join("F:/", 'GBC'),
    'gbc': os.path.join("F:/", 'GBC'),
    'gba': os.path.join("F:/", 'GBC'),
    'pokem': os.path.join("F:/", 'GBC'),
    'neo': os.path.join("F:/", 'GBA'),
    'wswan': os.path.join("F:/", 'GBA'),
    'wsv': os.path.join("F:/", 'GBA'),
    'amstrad': os.path.join("F:/", 'GBA'),
    'sega': os.path.join("F:/", 'MD'),
    'mega': os.path.join("F:/", 'MD'),
    'sms': os.path.join("F:/", 'MD'),
    'game': os.path.join("F:/", 'MD'),
    'm2k': os.path.join("F:/", 'ARCADE')
}

# Function to move files based on their prefixes
def move_files():
    for root, _, files in os.walk(origin_folder):
        for file in files:
            if file.endswith('.gba') and file.startswith(('nes', 'snes', 'pce', 'fds', 'colecovision', 'a26', '5200', 'lynx', 'intellivision', 'gb', 'gbc', 'gba', 'pokem', 'neo', 'wonderswan', 'supervision', 'amstrad', 'sega', 'mega', 'sms', 'game', 'm2k')):
                prefix = file.split(';')[0]
                destination = destinations.get(prefix.lower())
                if destination:
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(destination, file)
                    shutil.move(source_path, dest_path)
                    print(f"Moved {file} to {destination}")

# Call the function to move files
move_files()
