# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:14:27 2017

@author: zhoujb
"""

#from __future__ import print_function, division #If python2,add this line
import os
from itertools import product

# Where to save the data
PROJECT_ROOT_DIR = "."  

def k_mer_dna(number):
    
    return {''.join(x):0 for x in product('ACTG', repeat=number)}

def count_k_mer(seq,n):
    k_mer_dna_dict = k_mer_dna(n)
    for i in range(len(seq) - n + 1):
        count = seq[i:i+n]
        if count in k_mer_dna_dict:
            k_mer_dna_dict[count] += 1
    
    return k_mer_dna_dict

def write_file(file_name,k_mer):
    
    output_file = open(os.path.join(PROJECT_ROOT_DIR,'k_mer_output.tsv'),'w')
    seq = ''
    
    for line in open(os.path.join(PROJECT_ROOT_DIR,file_name)):
        line = line.rstrip()
        if line.startswith(">") and seq == '':
            output_file.write('\t'.join(k_mer_dna(k_mer).keys())+'\n')
    
        elif not line.startswith('>'):
            seq += line
    
        elif line.startswith('>') and seq != '':
            output_file.write('\t'.join([str(x) for x in count_k_mer(seq,k_mer).values()])+'\n')
            seq = ''

    output_file.write('\t'.join([str(x) for x in count_k_mer(seq,k_mer).values()])+'\n')
    output_file.close()

def print_k_mer(file_name='k_mer_output.tsv'):
    
    for line in open(os.path.join(PROJECT_ROOT_DIR,file_name)):
        line = line.rstrip()
        print(line)
        
def main(file_name,k_mer=3):
    write_file(file_name,k_mer)
    print_k_mer(file_name='k_mer_output.tsv')

if __name__ == "__main__":
    main('example.txt')