# Introduction

A pipeline for generating the necessary files needed for CAMISIM to run for *de novo* community design and read simulation.
This pipeline is particurly useful for simulations of several hundred (or more) genomes as it decreases the need to manually create
hundreds of necessary files and configuration files for CAMISIM.

The *de novo* community design needs two files to run:

1. A file containing, tab separated, a genome identifier and that path to the file of the genome.

2. A [[meta data file|meta-data-file-format] that contains, tab separated and with header, genome identifier, novelty categorization, 
otu assignment and a taxonomic classification.

For a review of CAMISIM, please visit https://github.com/CAMI-challenge/CAMISIM/wiki/User-manual.

# Code

## Synthethic Genome Generator

In the case where studies require the creation of synthethic genomes, this code will create a .fasta file with the desired number of
genomes and desired naming convention. Keep in mind that the code is also capable of generating strains from the original set of synthetic
genomes (references). However, if there is only a need for a single set of synthetic genomes, then simply run the first part of the code 
(i.e. Generating Reference Sequences -> Creating FASTA File with References).

## Split FASTA File

CAMISIM requires that all genomes be in individual FASTA files. This code takes as input the file containing all of the genomes and outputs
each genome saved in its own .fa file. CAMISIM takes either .fasta or .fa.

## CAMISIM De Novo Files

In the case where strains are generated, it's important to run CAMISIM for reach reference+strain set. This can be created using the
[community0] section in CAMISIM's configuration file template. This means that individual metadata and id-to-genome .tsv files need
to be created for each reference+strain set. This code takes as inputs the names of the genomes (can also be referred to as genome IDs)
and outputs the a metadata_n.tsv and the id_to_genome_n.tsv files, for n number of reference+strain sets (i.e. number of reference genomes)
starting at 0.

## CAMISIM Configuration Files

Finally, this code generates the configuration files for n number of reference+strain sets. Keep in mind that most options have to be set manually within the code itself to fit individual needs. Please take a look at the CAMISIM user manual above to see what each of the values mean in the configuration file.

# Running CAMISIM

For cases of several hundred references/reference+strain sets, a shell script can be created to run CAMISIM for each of the configuration files. Take a look at CAMISIM.sh as an example.

# Keeping Track of File Paths

It's important to thoroughly check the file paths for the inputs and outputs. I suggest using the CAMISIM directory as the main input for CAMISIM. Inside the CAMISIM directory, I have a folder for the configuration files, a folder for the FASTA files, and a folder for the *de novo* files. These folders help keep track of where everything is, especially if there are many files.

/Users/sarahussin/CAMISIM

  /CAMISIM/FASTA_Files/

    {containes all the 

