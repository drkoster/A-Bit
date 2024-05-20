import hashlib
from tqdm import tqdm
import argparse
import os
import hashlib

def create_hash(filepath, algorithm):
    hasher = getattr(hashlib, algorithm)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_hash(filepath, hashval, algorithm):
    hasher = getattr(hashlib, algorithm)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest() == hashval

def main():
    parser = argparse.ArgumentParser(description="Create or verify file hashes")
    parser.add_argument("--create", action='store_true', help="Create hashes for files")
    parser.add_argument("--verify", action='store_true', help="Verify hashes of files")
    parser.add_argument("--algorithm", type=str, default='md5', choices=['md5', 'sha1', 'sha256', 'sha3_256'], help="Hash algorithm to use (default: md5)")
    parser.add_argument("--output", type=str, required=True, help="Output file path")

    args = parser.parse_args()

    if not (args.create or args.verify):
        raise ValueError("Either --create or --verify must be specified")

    algorithm_name = args.algorithm
    output_filename = os.path.join(os.path.dirname(args.output), f"{os.path.basename(args.output)}_{algorithm_name}")

    with open(args.output, 'w') as fout:
        for root, dirs, files in tqdm(os.walk('.'), desc="Scanning directories"):
            for file in files:
                filepath = os.path.join(root, file)
                if args.create:
                    hashval = create_hash(filepath, algorithm_name)
                    fout.write("{} {}\n".format(filepath, hashval))
                elif args.verify:
                    with open(filepath) as fin:
                        hashval = fin.read().split()[-1]
                    if verify_hash(filepath, hashval, algorithm_name):
                        print("{} OK".format(filepath))
                    else:
                        print("{} FAILED".format(filepath))

if __name__ == "__main__":
    main()