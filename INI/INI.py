from Bio.Seq import Seq
from sys import argv

script, filename = argv

with open(filename, 'r') as input_file:
    seq = Seq(input_file.readline().strip())
    print ' '.join([str(seq.count('A')),
                    str(seq.count('C')),
                    str(seq.count('G')),
                    str(seq.count('T'))])
