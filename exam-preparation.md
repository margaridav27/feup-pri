Objectives based on the [moodle's study guide](https://docs.google.com/document/u/1/d/e/2PACX-1vTjdHdtrahXgr26A92oW9aQsf1YpoTUoXeL3p-g-xnDHff-QzHIyKPRK8My1RnWCMcmmNBRLh_I6D7v/pub).

# Information Processing

### Distinguish between data, metadata, and information.

- **Data** is a measurement of something, a fact known by direct observation. 
- **Metadata** is data about data, i.e. data that provides information about one or more aspects of the data. 
- **Information** is data that has been processed, organized and structured and has context/meaning, thus enabling decision making.

### Identify and describe the phases of a typical information lifecycle.

Create/Generate -> Collect -> Record/Store -> Process -> Distribute/Transmit -> Consume/Use -> Recycle/Erase

The life cycle of information typically includes the following phases:
- **Occurrence**: discover, design, author, etc;
- **Transmission**: networking, accessing, retrieving, transmitting, etc;
- **Processing and Management**: collecting, validating, modifying, indexing, classifying, ltering, sorting,
storing, etc;
- **Usage**: monitoring, explaining, planning, forecasting, decision-making, educating, learning, etc;

### Describe typical data processing patterns, pipelines and frameworks, e.g. ETL, EtlT, OSEMN.

- **ETL** (Extract, Transform, Load) is a data integration process that extracts data from a source system, transforms it into a format that is more suitable for analysis, and loads it into a target system. 
- **OSEMN** (Obtain, Scrub, Explore, Model, iNterpret) is a data science process that is used to analyze data and extract insights from it. 
- **ELT** (Extract, Load, Transform) is a data integration process that extracts data from a source system, loads it into a target system, and then transforms it. The sub-pattern **EtLt** introduces a transformation stp before the loading, typically associated with data cleaning tasks.

The ELT patterns allows for a clean split of responsabilities between the data engineers and data scientists. The data engineers are responsible for the EL part, while the data analysts are responsible for the T part.

### Describe the challenges associated with data processing.

- **Ownership** - know what data you have access to and what you can do whit it;
- **Ingestion interface and structure** - how do you get the data and in what form is in;
- **Volume** - in each step of the pipeline, volume needs to be taken into account; high
and low volume are dificult to define and depend on available infrastructures and algorithms;
- **Cleanliness and validity** - duplicate data, missing or incomplete data, encoding, etc;
- **Latency and bandwidth of the source** - need to consider internal update requirements
and also source system limits, speed, timeouts, etc;
- **Data selection** - is the author trustable, is the data updated.

### Identify and describe challenges and techniques related to: data cleaning, data preparation, and data presentation.

**Data cleaning**: identify and fix data quality issues
- missing/inconsistent/outdated values
- outliers
- duplicates
- mislabling/enconding/precision problems
- etc

**Data preparation**:
- **Data cleaning**: identify and fix data quality issues
- **Data transformation**: trasnform data into a format that is more suitable for analysis or manipulation
    - normalization of values to a comparable scale
    - scaling values to the same range
    - non-linear transformations to deal with skewness
    - discretization or binning
- **Data synthesis**: create new data from existing data
- **Data integration**: combine data from multiple sources
- **Data reduction**: eliminate data from the collection
    - filtering
    - sampling
    - aggregation

**Data presentation**: present data in a user-friendly format
- charts (suitable for numeric data)
    - bar/stacked bar/line/pie charts
    - box/scatter plots
    - histograms 
    - etc
- time series or timelines (help represent observations over time)
- maps (focus on geographical data)
- interactive (where control is given to the user to explore different paths or options)
- words (representing highlights of textual descriptions)
    - word clouds
    - etc

### Describe the importance of data pipelines and how Makefiles can be used to implement them.

- **Data pipelines** are a sequence of data processing elements connected in series, where the output of one element is the input of the next one. They are used to automate data processing tasks, and are typically used to process large amounts of data. Data pipelines must be designed to be robust, scalable, fault-tolerant and easily maintainable.
- **Makefiles** are a simple way to define a data pipeline, by defining targets and
rules to execute. They are typically used to automate the build process of a software project, but can also be used to automate data processing tasks. The underlying abstraction is of a dependency graph, where tasks depend on the execution of other tasks. Additionally, Make is able to automatically decide what to execute based on direct or indirect dependencies to files that have changed.

# IR Taks & Systems

### What is the difference between information retrieval and data retrieval?

- **Information retrieval** consists in finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers). It can be defined as a software program that deals with the organization, storage, retrieval, and evaluation of information from document repositories.

- **Data retrieval**, on the other hand, is the process of identifying and retrieving data from a database, based on a query provided by an user or an application.

### Give examples of IR and data retrieval systems.

- **IR system**: any common search engine (Google, Bing, Yahoo, etc)
- **DR system**: any database system (MySQL, PostgreSQL, MongoDB, etc)

### Give some examples of retrieval tasks evaluated in TREC.

Some examples are:
- clinical trials track
- conversational assistance track
- deep learning track
- etc (more can be found in this [link](https://trec.nist.gov/pubs/call2022.html))

### What are the modules of an IR system?

- crawling process
- indexing process
- retrieval and ranking process

# IR Concepts

### What is a document, a collection, a term, a bag of words?

- **Document**: is the indexing unit of an IR system. It is a piece of information that is stored in the collection and that is retrieved by the system. It can be a web page, a news article, a book, a scientific paper, etc.
- **Collection**: is a set of documents that are stored in the IR system and over which the retrieval is performed.
- **Term**: is the basic unit of information in an IR system. It is the smallest unit of text that can be indexed and searched for. It is usually a word, but can also be a phrase, a sentence, a paragraph, etc.
- **Bag of Words**: is a representation of a document as a set of terms. It is the most common representation of a document in IR systems. In a BoW model, the ordering of terms is ignored, and the only information that is kept is the presence/frequency of each term in the document.

### Define stemming.

Stemming refers to a heuristic process that chops off the ends of words in the hope of  reducing in ectional forms.

### What is an inverted index, a vocabulary, a postings list?

- **Inverted Index**: is a data structure that maps terms to the documents in which they appear.
- **Vocabulary**: is the set of terms that are indexed in the IR system.
- **Postings list**: is the list of documents that contain a given term (and, optionally, the positions in which the term appears in each document).

### What is an information need, a query, a results list?

- **Information Need**: is the user's goal in using an IR system. It is the reason why the user is using the system.
- **Query**: is the user's request to the IR system. It is the information that the user provides to the system to express the information need.
- **Results List**: is the list of documents that are returned by the IR system to satisfy the information need.

### What is a relevant result in a results list?

A document is relevant if it addresses the stated information need, not because it just
happens to contain all the words in the query. Unless the tool is perfect, only some of the retrieved results are going to be perceived by the user as actually containing information of value with respect to their personal information need.

# Vector Model

### What is the bag of words model for a document?

**Bag of Words** is a representation of a document as a set of terms. It is the most common representation of a document in IR systems. In a BoW model, the ordering of terms is ignored, and the only information that is kept is the presence/frequency of each term in the document.

### What is term frequency, collection frequency, document frequency, inverse document frequency?

- **Term Frequency (tf<sub>t,d</sub>)**: number of occurences of the term t in the document d.
- **Collection Frequency (cf<sub>t</sub>)**: number of occurences of the term t in the collection.
- **Document Frequency (df<sub>t</sub>)**: number of documents in the collection that contain the term t.
- **Inverse Document Frequency (idf<sub>t</sub>)**: is the inverse of the document frequency (N/df<sub>t</sub>, where N is the total number of documents in the collection). The rarer the term in a collection, the higher its idf.

### How do you calculate tf-idf weights?

**tf-idf<sub>t,d</sub> = tf<sub>t,d</sub> x idf<sub>t</sub>**

tf-idf<sub>t,d</sub> assigns to a term t a weight in a document d that is:
- highest when t occurs many times within a small number of documents (high tf, high idf);
- lower when the term occurs fewer times in a document, or occurs in many
documents (low tf, high idf or low idf);
- lowest when the term occurs in virtually all documents (low idf).

### How do you rank documents in the vector model?

The ranking of documents in the vector model is based on the cosine similarity between the query and the documents. 

The cosine similarity between two vectors is defined as:

**sim(d<sub>1</sub>,d<sub>2</sub>) = (d<sub>1</sub> . d<sub>2</sub>) / (||d<sub>1</sub>|| ||d<sub>2</sub>||)**

where d<sub>1</sub> and d<sub>2</sub> are two vectors, and d<sub>1</sub> . d<sub>2</sub> is the dot product of the two vectors.

# Evaluation

### What is precision, recall, interpolated precision?

- **Precision**: is the fraction of retrieved items that are relevant.
    - P = #(relevant items retrieved) / #(retrieved items)
    - P = TP / (TP + FP)
- **Recall**: is the fraction of relevant items that are retrieved.
    - R = #(relevant items retrieved) / #(relevant items)
    - R = TP / (TP + FN)
- **Interpolated Precision**: is the precision at a given recall level, or the maximum precision obtained for all recall levels above a given recall level.

### What is precision at k, R-precision?

- **Precision at k (P@k)**: is the precision of the top-k results in a ranked list of results.
- **R-precision**: is the precision at the recall level of R.

### Name the components of a test collection.

To measure the effectiveness of a search system in the standard way, three things are needed:
- A document collection;
- A test suite of information needs, expressible as queries;
- A set of relevance judgments, typically a binary assessment of either relevant or non-relevant for each query-document pair.

### Why is a set of relevance judgments considered a “ground truth” for IR?

The relevance judgments are considered a ground truth because they are the only way to assess the effectiveness of a search system. Only if one assumes that the relevance judgments are correct, can one evaluate the effectiveness of a search system, using the appropriate evaluation metrics.

### What is an average 11-point precision-recall graph for a set of queries?

??

### What is MAP, and do you calculate it for a set of queries in a test collection?

The Average Precision (AvP) is the average of the precision value obtained for the set of top k documents existing after each relevant document is retrieved. Given a set of queries, the Mean Average Precision (MAP) is the mean over the AvP values. 

This is one of the most commonly used measures in IR.

# Web Search

1. **What are informational, transactional and navigational information needs?**

2. **Name some differences between web search and enterprise search.**

3. **How do you index images?**

4. **Give examples of ranking signals used by search engines.**

5. **What are the SCC, IN and OUT components in the view of the web as a bowtie?**

# Link Analysis

1. **What are in-links and out-links for a web page?**

2. **How is anchor text used in web search?**

3. **Calculate PageRank values for a set of linked documents.**

4. **Calculate Hub and Authority values for a set of linked documents.**

# Query Processing

1. **Describe and distinguish between the two query processing techniques — document-at-a-time and term-at-a-time.**

2. **In what contexts is query transformation / expansion advantageous?**

3. **What techniques can be used to apply transformations / expansions to user queries?**

4. **Identify and describe query expansions techniques, such as relevance feedback or pseudo-relevance feedback.**

# Entity-oriented Search

1. **What is entity-oriented search? What is necessary to implement it?**

2. **Describe the challenges and techniques associated with building entity descriptions, entity ranking, entity linking.**

3. **Describe the data sources typically required for entity oriented search and its characteristics.**

# Search User Interfaces

1. **Identify and describe user interface techniques and elements that can be used to improve user experience in using search systems.**

2. **Describe how user interaction innovations and experiments can be evaluated.**

3. **What are design principles and heuristics?**

# Learning to Rank and Neural IR

1. **What is Learning to Rank?**

2. **Which are the main approaches in LTR? How do they differ in terms of input and output data?**

3. **What is Neural Information Retrieval?**

4. **How can neural models be used in the retrieval process?**

5. **What are word embeddings?**

6. **What is the difference between Learning to Rank and Neural Information Retrieval?**
