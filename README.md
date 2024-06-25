# A-Bit (Anti Bitrot indexing tool)
Detect file corruption and bitrot

## Description
Luxuries like ZFS or BTRFS are not always available. Therefore as an excercise I wrote a python script that will hash files on disk and save the filepath with hash to a seperate file. This file can be included onto the same media (CD, DVD or USB drive) or stored somewhere else for later verifying if the contents are still the same. Easy tool to do bulk hashing and verification.

The output filename will contain the chosen hash algorithm to be given when performing verification.

## Installation
Included is a requirements file for installation: `pip install -r requirements.txt`
alternatively use the portable package described below

## PyInstaller
A complete package is available for easier use without requiring installing modules.
Inside the `dist` directory you can find the latest portable application. Copy it somewhere on your pc and follow the usage section below. 

## Usage
The script supports the following arguments:<br>
      - --create                : Creates hashes for files and writes them into the specified output file.<br>
      - --verify                : Verifies hashes of files against the ones written in the specified output file.<br>
      - --algorithm             : Specify the hash algorithm to use (default: md5). Options are 'md5', 'sha1', 'sha256', and 'sha3_256'.<br>
      - --input                 : Specify the file that contains hashes and filepaths that you wish to verify.<br>
      - --output                : Specifies the path of the output file where hashes will be written or read from.<br>
      - --log_file              : Optional argument with --verify to safe results to logfile.<br>
      - --starting_dir          : The base directory to work from, includes subdirectories.<br>
      - --help                  : Print help description.<br>

Then execute the script by running: `python Abit.py [-h] [--create] [--verify] [--algorithm {md5,sha1,sha256,sha3_256}] [--input INPUT] [--output OUTPUT] [--log_file LOG_FILE] [--starting_dir STARTING_DIR]`

## Todo
The following features might be developed, on a rainy day, someday :)
- [x] Target directory as argument
- [ ] GUI version
- [ ] Option to use only filenames, making paths obsolete 
- [x] Write results to log file
- [ ] Threading for SSD's
- [x] Improved arguments error checking and help
- [ ] Config file for default behaviour
- [ ] Test and make compatible linux/ubuntu
- [ ] Hash files against other files instead of hashes
- [x] PyInstaller version in repository
- [ ] Better handling of hash file creation path handling

## Authors
Dennis Koster 

## Acknowledgments
Inspired by FreeFileSync - https://freefilesync.org/

## Changelog

## [1.1.0] UI version now available
- Introduced UI wrapper for console. 

## [1.0.0] First release
- Portable one click version in dist directory

## [0.0.5] Log to file
- Added function/argument to log verification results to file. Allows for shutdown after long verification sessions.

## [0.0.4] Target directory argument
- Added argument --starting_dir to specify a base directory where to start hashing from
- Readme fixes

## [0.0.3] Minor improvements
- Added better argument handling and description
- [FIX] Missing algorithm appending to the output file

## [0.0.2] Creature comforts
- Added Todo's to the readme
- Code cleanup/unused imports

## [0.0.1a] Initial working version

## License
This project is licensed under the Apache License 2.0 - see the LICENSE.md file for details
