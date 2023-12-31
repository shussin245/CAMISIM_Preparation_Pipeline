# -*- coding: utf-8 -*-
"""CAMISIM_Config_Files.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11kWA4sdfER3r_pfj2RlpAnnmKV7Sbym9
"""

import configparser

num_genomes_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51]
size_list = []
for n in range(0, 1000):
  size = (num_genomes_list[n]*10000)/1000000000
  size = f'{size:.5f}'
  size_list.append(size)
print(size_list)

for n in range(0, 1000):
  # Create a ConfigParser object
  config = configparser.ConfigParser()

  config.add_section('Main')
  config.set('Main', 'max_processors', '8')
  config.set('Main', 'phase', '0')
  config.set('Main', 'output_directory', f'/output/ref_{n}')
  config.set('Main', 'temp_directory', '/tmp')
  config.set('Main', 'gsa', 'True')
  config.set('Main', 'pooled_gsa', 'False')
  config.set('Main', 'anonymous', 'False')
  config.set('Main', 'compress', '1')
  config.set('Main', 'dataset_id', 'RL')

  config.add_section('ReadSimulator')
  config.set('ReadSimulator', 'type', 'art')
  config.set('ReadSimulator', 'samtools', '/input/tools/samtools-1.3/samtools')
  config.set('ReadSimulator', 'readsim', '/input/tools/art_illumina-2.3.6/art_illumina')
  config.set('ReadSimulator', 'profile', 'mbarc')
  config.set('ReadSimulator', 'error_profiles', '/input/tools/art_illumina-2.3.6/profiles/')
  config.set('ReadSimulator', 'base_profile_name', '')
  config.set('ReadSimulator', 'profile_read_length', '')
  config.set('ReadSimulator', 'fragments_size_mean', '270')
  config.set('ReadSimulator', 'fragment_size_standard_deviation', '27')

  config.add_section('CommunityDesign')
  config.set('CommunityDesign', 'size', f'{size_list[n]}')
  config.set('CommunityDesign', 'number_of_samples', '1')
  config.set('CommunityDesign', 'num_communities', '1')
  config.set('CommunityDesign', 'ncbi_taxdump', '/input/tools/ncbi-taxonomy_20170222.tar.gz')
  config.set('CommunityDesign', 'strain_simulation_template', '/input/scripts/StrainSimulationWrapper/sgEvolver/simulation_dir/')

  config.add_section('community0')
  config.set('community0', 'metadata', f'/input/Config_Files/metadata_{n}.tsv')
  config.set('community0', 'id_to_genome_file', f'/input/Config_Files/id_to_genome_{n}.tsv')
  config.set('community0', 'genomes_total', f'{num_genomes_list[n]}')
  config.set('community0', 'num_real_genomes', f'{num_genomes_list[n]}')
  config.set('community0', 'max_strains_per_otu', '1')
  config.set('community0', 'ratio', '1')
  config.set('community0', 'mode', 'differential')
  config.set('community0', 'log_sigma', '2')
  config.set('community0', 'log_mu', '1')
  config.set('community0', 'view', 'no')

  # Specify the file name
  file_name = f'config_{n}.ini'

  # Write the configuration to the INI file
  with open(file_name, 'w') as config_file:
    config.write(config_file)

  print(f"INI file '{file_name}' has been created.")
