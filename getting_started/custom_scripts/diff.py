import gcvb
import argparse

def parse():
    parser = argparse.ArgumentParser(description="stupid diff")
    parser.add_argument('file1',metavar="first",type=str,help="first file for the comparaison")
    parser.add_argument('file2',metavar="second",type=str,help="second file for the comparaison")
    parser.add_argument('valid',metavar="valid",type=str,help="validation id")
    args = parser.parse_args()
    return args

def relative_change(new_value,reference):
    return abs((new_value-reference)/reference)

def main():
    args=parse()
    with open(args.file1, 'r') as f1, open(args.file2, 'r') as f2:
        v1=float(f1.readlines()[0])
        v2=float(f2.readlines()[0])
    dis=relative_change(v1,v2)
    gcvb.add_metric(args.valid,dis)

if __name__ == '__main__':
    main()