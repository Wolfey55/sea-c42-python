# Name: Stephan Bosch
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# sum of G, C, A and T count.
sum_gcat = 0
# Number of GC and AT nucleotides seen so far.
gc_count = 0
at_count = 0
# Number of G, C, A and T nucleotides seen so far (individually).
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    # if the bp is an A or T,
    if bp == 'A' or bp == 'T':
        # increment the count of AT
        at_count = at_count + 1

    # if the bp is a G,
    if bp == 'G':
        # increment the count of G
        g_count = g_count + 1

    # if the bp is a C,
    if bp == 'C':
        # increment the count of C
        c_count = c_count + 1

    # if the bp is a A,
    if bp == 'A':
        # increment the count of A
        a_count = a_count + 1

    # if the bp is a T,
    if bp == 'T':
        # increment the count of T
        t_count = t_count + 1

# add the g, c , a and t count to get an accurate total count
sum_gcat = g_count + c_count + a_count + t_count


# divide the gc_count by the sum_gcat
gc_content = float(gc_count) / sum_gcat

# divide the at_count by the sum_gcat
at_content = float(at_count) / sum_gcat

# Print the answer
print('Total Count:', total_count)
print('Sequence Length:', len(seq))
print('Sum of GCAT:', sum_gcat)
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G-count:', g_count)
print('C-count:', c_count)
print('A-count:', a_count)
print('T-count:', t_count)
