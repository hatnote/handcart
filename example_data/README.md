# taxon_treatments_2010s.csv

## Description

This file contains c. 10K records containing taxonomic and bibliographic data for taxa described in the 2010s and the publications in which their descriptions occur. Each record corresponds to a taxon "treatment", i.e., the section of a publication in which a taxon is formally named and described or redescribed.

## Source

The data comes from TreatmentBank (http://tb.plazi.org/GgServer/search) maintained by Plazi (http://plazi.org), and was extracted from pdf versions of publications.

## Sample Data
```
DocDoi,DocIsbn,DocIssn,BibAuthor,BibTitle,BibYear,BibDecade,BibSource,BibFirstPage,BibLastPage,TreatmentID,TaxonName,TaxonRank,Kingdom,Phylum,Class,Order,Family,Genus,Species,TaxonStatus
10.11646/zootaxa.4088.2.6,,1175-5326,"Aarvik, Leif","Redefinition and revision of African Cosmetra Diakonoff, 1977 (Lepidoptera: Tortricidae) with description of six new species",2016,2010,Zootaxa,245,256,http://treatment.plazi.org/id/A279021FFF91FFCDAE821588FE598409,Cosmetra juu,species,Animalia,Arthropoda,Insecta,Lepidoptera,Tortricidae,Cosmetra,juu,sp. nov.
10.11646/zootaxa.4088.2.6,,1175-5326,"Aarvik, Leif","Redefinition and revision of African Cosmetra Diakonoff, 1977 (Lepidoptera: Tortricidae) with description of six new species",2016,2010,Zootaxa,245,256,http://treatment.plazi.org/id/A279021FFF98FFC2AE8210C9FA478694,"Cosmetra tumulata (Meyrick, 1908)",species,Animalia,Arthropoda,Insecta,Lepidoptera,Tortricidae,Cosmetra,tumulata,comb. nov.
```

## Field Definitions

- DocDoi: The CrossRef or Zenodo/DataCite DOI of the parent publication
- DocIsbn: The ISBN of the parent publication (if available)
- DocIssn: The ISSN of the parent publication (if available)
- BibAuthor: The author(s) of the parent publication; if there are multiple authors, names are separatd by semicolons 
- BibTitle: The title of the parent publication
- BibYear: The year of publication of the parent publication in YYYY format
- BibDecade: The decade in which the publication was published in YYYY format (e.g., '1990' for 1990s) 
- BibSource: The Journal or Series Title in which the parent publication was published 
- BibFirstPage: The first page on which the parent publication occurs in its journal issue, volume, etc.
- BibLastPage: The last page on which the parent publication occurs in its journal issue, volume, etc.
- TreatmentID: The Plazi assigned HTTP URI serving as a GUID for the taxon treatment. Corresponds to wikidata item Q20644485. NOTE: the URI will dereference to an HTML representation. XML and RDF representations are available by appending '.xml' and '.rdf' respectively. 
- TaxonName: The verbatim form of the Taxon name
- TaxonRank: The taxonomic rank (e.g., species) of the taxon described in the treatment
- Kingdom: The kingdom in which the described taxon is classified
- Phylum: The phylum in which the described taxon is classified
- Class: The class in which the described taxon is classified
- Order: The order in which the described taxon is classified
- Family: The family in which the described taxon is classified
- Genus: The genus in which the described taxon is classified
- Species: The species in which the described taxon is classified
- TaxonStatus: The status (e.g. "n. sp." or "new species") of the described taxon
