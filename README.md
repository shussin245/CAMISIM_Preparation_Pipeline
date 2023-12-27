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
each genomes saved in its own .fa file.

## CAMISIM De Novo Files

In the case where strains are generated, it's important to run CAMISIM for reach reference+strain set. This can be created using the
[community] sections in CAMISIM's configuration file template. This means that individual metadata and id-to-genome .tsv files need
to be created for each reference+strain set. This code takes as inputs the names of the genomes (can also be referred to as genome IDs)
and outputs the a metadata_n.tsv and the id_to_genome_n.tsv files, for n number of reference+strain sets (i.e. number of reference genomes)
starting at 0.

## CAMISIM Configuration File

Finally, this code generates the configuration file needed for CAMISIM to run (with .ini extension). Note that most options have to be
set manually for individual use cases. Overally, this code is helpful for creating the configurations for the communities. Recall that
each reference+strain set represents a community. Having several hundred references can result in a very long time writing the
configurations for the communities. On the other hand, this code is capable of writing the configurations for n number of references.

