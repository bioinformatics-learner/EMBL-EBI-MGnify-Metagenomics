# Microbial Metagenomics with MGnify: Raw-Reads Analysis Notes

* **Training Event:** EMBL-EBI Live Training Webinar[span_2](start_span)[span_2](end_span)
* **Topic:** Microbial metagenomics with MGnify: what can metagenomic raw reads tell us?[span_3](start_span)[span_3](end_span)
* **Speaker:** Timothy Rozday (EMBL-EBI)[span_4](start_span)[span_4](end_span)
* **Date:** November 18, 2026[span_5](start_span)[span_5](end_span)
* **Author:** Anjali Prabha

---

## 1. Raw-Reads Analysis vs. Metagenomic Assembly
* **Amplicon vs. Shotgun Metagenomics:**
  * *Amplicon sequencing (e.g., 16S rRNA):* Targets a single marker gene to answer **"Who is there?"**[span_6](start_span)[span_6](end_span)
  * *Metagenomic sequencing:* Sequences fragments from all DNA in a sample to answer **"What are they doing? (+ who is there)"**[span_7](start_span)[span_7](end_span).
* **Computational Efficiency:** Direct raw-read profiling is **~7x faster** than metagenomic assembly (~3.6 CPU-hours and ~9 GB peak memory vs. ~27 CPU-hours and ~35 GB peak memory for assembly)[span_8](start_span)[span_8](end_span).
* **Capturing Low-Abundance Taxa:** Metagenomic assemblies only capture a subset of raw reads—for complex environments like soil and marine samples, only **~8%** of QC-passing reads assemble into contigs[span_9](start_span)[span_9](end_span). Raw-read analysis preserves the remaining microbial diversity[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).

---

## 2. Origin of Metagenomic Reads & Sequencing Noise
* **Workflow:** Sample collection $\rightarrow$ DNA Extraction (lysis & purification) $\rightarrow$ Library Prep (fragmentation, adding adapters/barcodes, optional PCR) $\rightarrow$ Sequencing (FASTQ output with base calls + quality scores)[span_12](start_span)[span_12](end_span).
* **Signal vs. Confounders:** Raw FASTQ reads contain true **biological signals** mixed with extraction/PCR bias, host DNA contamination, sequencing errors (noise), and technical artefacts (adapters, phiX)[span_13](start_span)[span_13](end_span).

---

## 3. The MGnify Raw-Reads Analysis Pipeline (`RawR`)
MGnify uses an open-source, containerized **Nextflow** pipeline (`github.com/EBI-Metagenomics/raw-reads-analysis-pipeline`) consisting of five core stages[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span):

1. **Fetch:** Download raw sequencing runs from the European Nucleotide Archive (ENA) and standardize formats[span_16](start_span)[span_16](end_span).
2. **Quality Control (`fastp`):**
   * Trims sequencing adapters and polyG tails (common in two-color Illumina sequencers)[span_17](start_span)[span_17](end_span).
   * Drops low-quality reads (>40% bases below Q15), reads with >5 undetermined bases (`N`), and short reads (<15 bases post-trimming)[span_18](start_span)[span_18](end_span).
3. **Host Decontamination (`bwa-mem2` / `minimap2`):**
   * Removes **Human (GRCh38)** and **phiX** control reads[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span).
   * *Important Limitation:* Non-human host DNA (e.g., chicken) and lab kit contaminants are **not** removed[span_21](start_span)[span_21](end_span).
4. **Taxonomic Profiling:**
   * **SILVA (SSU/LSU rRNA genes):** Broad reference database (53,301+ named species across Bacteria, Archaea, and Eukaryotes)[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span). Detects **3–6x more taxa per run** (higher recall)[span_24](start_span)[span_24](end_span).
   * **mOTUs3 (10 single-copy marker genes):** Higher taxonomic precision (Median Bray-Curtis distance vs. truth = `0.04` compared to `0.26` for SILVA) and avoids gene copy-number bias[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span).
5. **Reporting:** Generates **MultiQC** summary reports, interactive **Krona** taxonomy plots, and **TSV** abundance tables[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span).

---

## 4. Using MGnify Data & API Resources
* **Repository Scale:** Holds >47,000 raw-read analyses across 800+ studies (~132 Tbp of sequence data) spanning human gut, marine, soil, and engineered biomes[span_29](start_span)[span_29](end_span).
* **Connecting Literature to Data:** Published metagenomic studies can be located directly in MGnify using their **ENA Accession IDs** (`PRJ...`, `ERP...`, `SRP...`)[span_30](start_span)[span_30](end_span)[span_31](start_span)[span_31](end_span).
* **Programmatic Access (`mgnipy`):** The `mgnipy` Python wrapper enables automated metadata retrieval and cross-study queries via the MGnify REST API[span_32](start_span)[span_32](end_span).

---

## 5. Key Resources & Links
* **MGnify Portal:** [www.ebi.ac.uk/metagenomics](https://www.ebi.ac.uk/metagenomics)[span_33](start_span)[span_33](end_span)
* **Documentation & API Examples:** [docs.mgnify.org](https://docs.mgnify.org)[span_34](start_span)[span_34](end_span)[span_35](start_span)[span_35](end_span)
* **RawR Pipeline Source Code:** [github.com/EBI-Metagenomics/raw-reads-analysis-pipeline](https://github.com/EBI-Metagenomics/raw-reads-analysis-pipeline)[span_36](start_span)[span_36](end_span)[span_37](start_span)[span_37](end_span)
