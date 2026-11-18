"""
Script: fetch_mgnify_studies.py
Author: Anjali Prabha
Description: Queries the EMBL-EBI MGnify API using mgnipy to retrieve 
             metagenomic raw-read studies processed with Pipeline v6, 
             filters for specific biomes (e.g., Human gut), and exports 
             the summary metadata to a CSV file.
Reference: Concepts learned from EMBL-EBI MGnify Training Webinar (Nov 2026).
"""

import pandas as pd
from mgnipy import MGnify


def fetch_v6_metagenomic_studies(target_biome="Human gut", output_csv="mgnify_v6_studies.csv"):
    # Initialize MGnify API client
    mg = MGnify()
    
    print("Fetching studies processed with MGnify Pipeline v6...")
    studies = mg.studies(has_analyses_from_pipeline="V6")
    studies.get_all()
    
    # Convert search results into a Pandas DataFrame
    df = studies.search_results.to_pandas(expand_nested_dicts=True)
    
    if df.empty:
        print("No studies found.")
        return
    
    # Filter for studies matching the target biome (if biome column exists)
    if "biomes" in df.columns:
        filtered_df = df[df["biomes"].astype(str).str.contains(target_biome, case=False, na=False)]
    else:
        filtered_df = df

    # Select key columns for clean reporting
    selected_cols = [col for col in ["accession", "study_name", "samples_count", "biomes"] if col in filtered_df.columns]
    clean_df = filtered_df[selected_cols]
    
    # Save results to CSV
    clean_df.to_csv(output_csv, index=False)
    print(f"Saved {len(clean_df)} '{target_biome}' studies to {output_csv}")
    return clean_df


if __name__ == "__main__":
    # Example: Fetch Human gut metagenomic studies and save to CSV
    results = fetch_v6_metagenomic_studies(target_biome="Human gut")
    if results is not None:
        print(results.head())
