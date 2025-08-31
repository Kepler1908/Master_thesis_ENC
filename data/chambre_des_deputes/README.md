# Chambre Dataset Processing

This repository contains the processed results generated from the raw dataset and indexing scripts.  

## Data Generation
- **Input file:** `\data\raw_data\raw_data_chambre.csv`  
- **Script used:** `\scripts\lightrag_indexing.py`  
- **Output:** Indexed data and graph representations  

## Visualization
To visualize the knowledge graph:
1. Open the file **`graph_chunk_entity_relation.graphml`**
2. Use [Gephi](https://gephi.org/) (recommended) for interactive exploration

## Notes
- Make sure Gephi is installed on your system.  
- The `.graphml` file can be customized with filters, layouts, and styling options inside Gephi.  

* The original vdb_entites.json is too big, to obtain the orginal file, run **`vdb_entities_merge.py`**




