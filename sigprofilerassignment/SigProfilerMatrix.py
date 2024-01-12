#!/usr/bin/env python3

import click
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen


@click.command()
@click.option('--project', required=True, help='Unique name given to the current samples')
@click.option('--reference_genome', required=True, help='Reference genome')
@click.option('--path_to_input_files', required=True, help='Path where the input vcf files are located')
@click.option('--exome', is_flag=True, default = False, help='Flag to use only the exome or not')
@click.option('--bed_file', default=None, help='BED file that contains a list of ranges to be used in generating the matrices')
@click.option('--chrom_based', is_flag=True, default = False, help='Flag to create the matrices on a per chromosome basis')
@click.option('--plot', is_flag=True, default = False, help='Flag to generate the plots for each context')
@click.option('--tsb_stat', is_flag=True, default = False, help='Performs a transcriptional strand bias test for the 24, 384, and 6144 contexts. The output is saved into the output/TSB directory')
@click.option('--seqinfo', is_flag=True, default = False, help='Flag to generate the sequence information plot')
@click.option('--cushion', default=100, help='Length of the flanking regions around the genomic features')
@click.option('--gs', is_flag=True, default = False, help='Flag that performs a gene strand bias test')


def run_sigprofiler_matrix(project, reference_genome, path_to_input_files, exome, bed_file, chrom_based, plot, tsb_stat, seqinfo, cushion, gs):
    matGen.SigProfilerMatrixGeneratorFunc(project=project,
                                    reference_genome=reference_genome,
                                    path_to_input_files=path_to_input_files,
                                    exome= exome,
                                    bed_file=bed_file,
                                    chrom_based=chrom_based,
                                    plot=plot,
                                    tsb_stat=tsb_stat,
                                    seqInfo=seqinfo,
                                    cushion=cushion,
                                    gs=gs)

if __name__ == '__main__':
    run_sigprofiler_matrix()


