# A-Bit (Anti Bitrot indexing tool)
Detect file corruption and bitrot

## Description
Luxuries like ZFS or BTRFS are not always available. Therefore as an excercise I wrote a python script that will hash all files on disk and save the path with hash to a seperate file. This file can be included onto the same media (CD, DVD or USB drive) or stored somewhere else for later verifying if the contents are still the same. 

The output filename will contain the chosen hash algorithm to be given when performing verification.

## Installation
Included is a requirements file for installation: `pip install -r requirements.txt`

## Usage
The script supports the following arguments:
      - --create                : Creates hashes for files and writes them into the specified output file.
      - --verify                : Verifies hashes of files against the ones written in the specified output file.
      - --algorithm             : Specify the hash algorithm to use (default: md5). Options are 'md5', 'sha1', 'sha256', and 'sha3_256'.
      - --input                 : Specify the file that contains hashes and filepaths that you wish to verify
      - --output                : Specifies the path of the output file where hashes will be written or read from.
      - --help                  : Print help description

Then execute the script by running: `python Abit.py [--create | --verify] [--algorithm md5|sha1|sha256|sha3_256] [--output output_filename]`

## Todo
The following features might be developed, on a rainy day, someday :)
- [ ] Target directory as argument
- [ ] GUI version
- [ ] Option to use only filenames, making paths absolete 
- [ ] Write results to log file
- [ ] Threading for SSD's
- [x] Improved arguments error checking and help
- [ ] Config file for default behaviour

## Authors
Dennis Koster 

## Acknowledgments
Inspired by FreeFileSync - https://freefilesync.org/

## Changelog

## [0.0.3] Minor improvements
- Added better argument handling and description
- [FIX] Missing algorithm appending to the output file

## [0.0.2] Creature comforts
- Added Todo's to the readme
- Code cleanup/unused imports

## [0.0.1a] Initial working version

## License
This project is licensed under the Apache License 2.0 - see the LICENSE.md file for details
