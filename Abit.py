import os
#import sys
import hashlib
import argparse
import __version__
#from pathlib import Path
from tqdm import tqdm

# Buffered file reader method
def get_hash(filepath, algorithm):
    with open(filepath, 'rb') as f:
        hasher = getattr(hashlib, algorithm)()
        for chunk in iter(lambda: f.read(8192), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

# Creates a file and writes absolute path together with hash
def create_file_hashes(output_file, algorithm, root_dir='.'):
    hashes = {}
    for root, dir, files in tqdm(os.walk('.'), desc="Scanning directories"):
        for file in files:
            filepath = os.path.join(root, file)
            hash_value = get_hash(filepath, algorithm)
            hashes[filepath] = hash_value
    
    with open(output_file, 'w') as f:
        for k, v in sorted(hashes.items()):
            f.write(f'{k}\t{v}\n')

# Reads the input file for hashes and compares against target directory
def verify_file_hashes(input_file, algorithm):
    hashes = {}
    with open(input_file) as f:
        for line in f:
            parts = line.split('\t')
            filepath, hash_value = parts[0], parts[1]
            hashes[filepath] = hash_value
    
    for root, dir, files in tqdm(os.walk('.'), desc="Verifying hashes"):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath in hashes:
                get_hash_from_file = get_hash(filepath, algorithm)
                if str(get_hash_from_file) != str(hashes[filepath]).rstrip():
                    print(f'Mismatch for {filepath}: calculated hash={get_hash_from_file} but stored hash={hashes[filepath]}')
            else:
                print(f'File not found in hashtable: {filepath}')

def main():
    print("A-Bit version:", __version__.__version__)
    parser = argparse.ArgumentParser(description="Anti Bit-rot Indexing Tool")
    parser.add_argument("--create", action='store_true', help="Create hashes for files")
    parser.add_argument("--verify", action='store_true', help="Verify hashes of files using input file")
    parser.add_argument("--algorithm", type=str, default='md5', choices=['md5', 'sha1', 'sha256', 'sha3_256'], help="Hash algorithm to use (default: md5)")
    parser.add_argument("--input", type=str, help="Input file containing hashes for verification")
    parser.add_argument("--output", type=str, default='hashes.out', help="Output file path or leave empty to print results (default: hashes.out)")

    args = parser.parse_args()

    if not (args.create or args.verify):
        raise ValueError("Either --create or --verify must be specified")
    elif not (args.input or args.output):
        raise ValueError("Missing input or output file")   

    algorithm_name = args.algorithm
    input_filename = args.input
    output_filename = os.path.join(os.getcwd(), args.output) if args.output else None

    if args.create:
        create_file_hashes(output_filename, algorithm_name)
    elif args.verify:
        verify_file_hashes(input_filename, algorithm_name)

    print("All done!")
        
if __name__ == '__main__':
    main()