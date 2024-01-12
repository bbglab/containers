#!/usr/bin/env python3

import click
import SigProfilerAssignment as spa
from SigProfilerAssignment import Analyzer as Analyze

@click.command()
@click.option('--samples', help='Path to the samples file')
@click.option('--output', help='Path to the output folder')
@click.option('--input-type', default='matrix', help='Input type (e.g., matrix)')
@click.option('--context-type', default='96', help='Context type (e.g., 96)')
@click.option('--collapse-to-SBS96', is_flag=True, help='Collapse to SBS96')
@click.option('--cosmic-version', default=3.4, help='COSMIC version (e.g., 3.4)')
@click.option('--exome/--no-exome', default=False, help='Exome')
@click.option('--genome-build', default='GRCh37', help='Genome build (e.g., GRCh37)')
@click.option('--signature-database', default=None, help='Path to signature database')
@click.option('--exclude-signature-subgroups', default=None, help='Exclude signature subgroups')
@click.option('--export-probabilities', is_flag=True, help='Export probabilities')
@click.option('--export-probabilities-per-mutation', is_flag=True, help='Export probabilities per mutation')
@click.option('--make-plots', is_flag=True, help='Make plots')
@click.option('--sample-reconstruction-plots', is_flag=True, help='Sample reconstruction plots')
@click.option('--verbose', is_flag=True, help='Verbose mode')
def run_cosmic_fit(samples, output, input_type, context_type, collapse_to_sbs96, cosmic_version,
                   exome, genome_build, signature_database, exclude_signature_subgroups,
                   export_probabilities, export_probabilities_per_mutation, make_plots,
                   sample_reconstruction_plots, verbose):
    Analyze.cosmic_fit(samples, output, input_type=input_type, context_type=context_type,
                       collapse_to_SBS96=collapse_to_sbs96, cosmic_version=cosmic_version,
                       exome=exome, genome_build=genome_build,
                       signature_database=signature_database,
                       exclude_signature_subgroups=exclude_signature_subgroups,
                       export_probabilities=export_probabilities,
                       export_probabilities_per_mutation=export_probabilities_per_mutation,
                       make_plots=make_plots,
                       sample_reconstruction_plots=sample_reconstruction_plots,
                       verbose=verbose)

if __name__ == '__main__':
    run_cosmic_fit()
