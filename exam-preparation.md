Questions of [moodle's study guide](https://docs.google.com/document/u/1/d/e/2PACX-1vTjdHdtrahXgr26A92oW9aQsf1YpoTUoXeL3p-g-xnDHff-QzHIyKPRK8My1RnWCMcmmNBRLh_I6D7v/pub).

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

Stemming refers to a heuristic process that chops off the ends of words in the hope of reducing in ectional forms.

### What is an inverted index, a vocabulary, a postings list?

- **Inverted Index**: is a data structure that maps terms to the documents in which they appear.
- **Vocabulary**: is the set of terms that are indexed in the IR system.
- **Postings list**: is the list of documents that contain a given term (and, optionally, the positions in which the term appears in each document).

### What is an information need, a query, a results list?

- **Information Need**: is the user's goal in using an IR system. It is the reason why the user is using the system.
- **Query**: is the user's request to the IR system. It is the information that the user provides to the system to express the information need.
- **Results List**: is the list of documents that are returned by the IR system to satisfy the information need.

### What is a relevant result in a results list?

A document is relevant if it addresses the stated information need, not because it just happens to contain all the words in the query. Unless the tool is perfect, only some of the retrieved results are going to be perceived by the user as actually containing information of value with respect to their personal information need.

# Vector Model

### What is the bag of words model for a document?

**Bag of Words** is a representation of a document as a set of terms. It is the most common representation of a document in IR systems. In a BoW model, the ordering of terms is ignored, and the only information that is kept is the presence/frequency of each term in the document.

### What is term frequency, collection frequency, document frequency, inverse document frequency?

- **Term Frequency (tf<sub>t,d</sub>)**: number of occurences of the term t in the document d.
- **Collection Frequency (cf<sub>t</sub>)**: number of occurences of the term t in the collection.
- **Document Frequency (df<sub>t</sub>)**: number of documents in the collection that contain the term t.
- **Inverse Document Frequency (idf<sub>t</sub>)**: is the inverse of the document frequency (N/df<sub>t</sub>, where N is the total number of documents in the collection). IDF is perceived as a measure of how rare a term is in the collection of documents - the higher the idf, the rarer the term.

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

### Why is the idf of a term always finite? (Manning, 6.8)

The idf of a term if the inverse of the df. The only scenario in which the idf of a term is infinite is when the df of the term is 0. However, this is not possible, since the df of a term is always at least 1, otherwise, the term wouldn't even be part of the vocabulary.

### What is the idf of a term that occurs in every document? Compare this with the use of stop word lists. (Manning, 6.9)

One can deduce this by two means:

- considering that idf measures how rare a term is in the collection of documents, simply by this definition one can conclude that the idf of a term that occurs in every document is 0, because it is not rare at all;
- considering the formula of the idf, one can also conclude that the idf of a term that occurs in every document is 0, because the df will equal to N and so log(N/df) = log(1) = 0.

### Can the tf-idf weight of a term in a document exceed 1? (Manning, 6.11)

Yes, if a term appears very frequently in a document and is rare in the collection of documents, the tf-idf weight of the term in that document could be very high, possibly exceeding 1.

# Evaluation

### What is precision, recall, interpolated precision?

- **Precision**: is the fraction of retrieved items that are relevant.
  - P = #(relevant items retrieved) / #(retrieved items)
  - P = TP / (TP + FP)
- **Recall**: is the fraction of relevant items that are retrieved.
  - R = #(relevant items retrieved) / #(relevant items)
  - R = TP / (TP + FN)
- **Interpolated Precision**: is the precision at a given recall level, or the maximum precision obtained for all recall levels above a given recall level. The higher the interpolated precision at a certain recall level, the more accurate the model's predictions are.

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

By definition, a 11-point precision-recall curve is a graph plotting the interpolated precision of an IR system at 11 standard recall levels, that is, {0.0,0.1,0.2,...,1.0}.

### What is MAP, and do you calculate it for a set of queries in a test collection?

The Average Precision (AvP) is the average of the precision value obtained for the set of top k documents existing after each relevant document is retrieved. Given a set of queries, the Mean Average Precision (MAP) is the mean over the AvP values.

This is one of the most commonly used measures in IR.

![Screenshot from 2023-01-07 16-42-31](https://user-images.githubusercontent.com/55671968/211161416-368b0150-8425-4d12-8495-30b1ef509628.png)

# Web Search

### What are informational, transactional and navigational information needs?

- **Informational**: is the need to find general information about a topic.
- **Navigational**: is the need to find a specific resource.
- **Transactional**: is the need to perform a transaction on the web, such as purchasing a product, downloading a file, etc.

### Name some differences between web search and enterprise search.

Web search and enterprise search are both types of search engines, but they are designed to meet different needs and are used in different contexts. Some of the key differences between web search and enterprise search are:

|                   | Web search                                                                                                                                                       | Enterprise search                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Scope             | are designed to search the entire World Wide Web                                                                                                                 | are designed to search within a specific organization or enterprise                                      |
| Content           | index a wide range of content types (e.g. web pages, images, videos, news articles)                                                                              | typically index a more limited set of content types (e.g. documents, emails, database records)           |
| Users             | are used by a broad audience of users                                                                                                                            | are typically used by employees within an organization                                                   |
| Accessibility     | are generally publicly accessible                                                                                                                                | are typically restricted to employees or other authorized users                                          |
| Relevance ranking | use complex algorithms to rank search results based on factors such as the relevance of the content, the authority of the webpage, and the user's search history | may use similar algorithms, but the ranking may be customized for the specific needs of the organization |
| Security          | generally do not have to worry about security issues                                                                                                             | must be able to protect sensitive information                                                            |

### How do you index images?

There are several ways that images can be indexed in IR systems:

- **Text-based indexing**: In this method, the images are automatically annotated with text tags based on the content of the images. The text tags are then used to index the images in the same way that text documents are indexed.
- **Visual feature indexing**: In this method, images are indexed based on the visual features they contain, such as color, shape, texture, and layout. These features are typically extracted automatically using computer vision algorithms.
- **Image metadata indexing**: In this method, images are indexed based on metadata associated with the images, such as the date the image was taken, the camera used to take the image, and the location where the image was taken.
- **Textual metadata indexing**: In this method, images are indexed based on textual metadata associated with the images, such as the file name, the caption associated with the image, and the tags associated with the image.
- **Hybrid indexing**: In this method, a combination of the above methods is used to index images. For example, an image may be indexed using both text-based and visual feature indexing.

### Give examples of ranking signals used by search engines.

Signals can be organized in different types:

- **Content**: related to the text itself and consider HTML semantics
- **Structural**: related to the link structure of the web
- **Usage**: related to the feedback provided by the users, for example through clicks, geographical location, technological context, etc

Signals can also be distinguised according to other dimensions:

- **User-dependent**: depend on the user's characteristics
- **Query-dependent**: depend on the user's query
- **Document-dependent**: depend on a single document
- **Collection-dependent**: depend on information from the complete collection

### What are the SCC, IN and OUT components in the view of the web as a bowtie?

The SCC (strongly connected component) is a subset of the web that is made up of pages that can be reached from each other through a series of links. These pages form a kind of "loop" within the web, such that it is possible to get from any page in the SCC to any other page in the SCC by following links.

The user can navigate from any page in IN to any page in SCC, by following hyperlinks. Likewise, he can navigate from any page in SCC to any page in OUT. However, it is not possible to navigate from a page in SCC to any page in IN, or from a page in OUT to a page in SCC (or, consequently, IN).

Together, the SCC, IN, and OUT components form the "bowtie" structure of the web, with the SCC representing the central "knot" of the bowtie and the IN and OUT components representing the "ends" of the bowtie.

# Link Analysis

### What are in-links and out-links for a web page?

- **In-links** are links that point to a particular web page from other web pages. For example, if web page A has a link to web page B, then the link from web page A to web page B is an in-link for web page B.
- **Out-links** are links that a particular web page makes to other web pages. For example, if web page A has a link to web page B, then the link from web page A to web page B is an out-link for web page A.

Both in-links and out-links can be important for search engines when they are trying to understand the content and relevance of a web page. **In-links can help search engines understand how popular and important a particular web page is**, and **out-links can help search engines understand what the web page is about** and how it is related to other pages on the web.

### How is anchor text used in web search?

Anchor text is the visible, clickable text in a hyperlink. In web search, anchor text is used to provide context about the content of the linked page and can help search engines understand the relevance and topic of the linked page.

For example, consider the following hyperlink:

"Learn more about the history of chocolate"

In this case, the anchor text is "Learn more about the history of chocolate." If a search engine encounters this hyperlink while crawling the web, it may use the anchor text to help determine the topic of the linked page and how relevant it is to a particular search query.

Anchor text is just one factor that search engines consider when ranking pages in search results, but it can be an important one, especially when the anchor text is relevant and descriptive of the content on the linked page. The collection of all anchor texts can be explored with standard IR techniques, and incorporated as an additional features in an inverted index and is, in fact, an important feature for image search.

# Query Processing

### Describe and distinguish between the two query processing techniques — document-at-a-time and term-at-a-time.

- **Document-at-a-time**: calculates complete scores for documents by processing all term lists, one document at a time. At the end all documents are sorted according to their score.

- **Term-at-a-time**: accumulates scores for documents by processing term lists one at a time. When all terms are processed, the accumulators contain the final scores of all matching documents.

One advantage of document-at-a-time query processing is that it can handle complex queries more easily, since it can examine the entire document to determine whether it matches the query. However, it can be slower than term-at-a-time query processing, since it has to examine each document in the index.

On the other hand, term-at-a-time query processing is generally faster than document-at-a-time query processing, since it only has to examine the index and not the actual documents. However, it can be less effective at handling complex queries, since it only looks at individual terms and not the overall content of the documents.

### In what contexts is query transformation/expansion advantageous?

Query transformation/expansion, is the process of modifying a search query to improve the relevance of the search results. There are several contexts in which this can be advantageous:

- **Ambiguity**: if a search query is ambiguous or has multiple meanings, query transformation can be used to disambiguate the query and improve the relevance of the search results.
- **Synonyms**: if a search query does not include all of the relevant terms for a particular topic, query transformation can be used to add synonyms or related terms to the query to improve the coverage of the search results.
- **Misspellings**: if a search query includes misspellings or typos, query transformation can be used to correct the misspellings and improve the accuracy of the search results.
- **Vocabulary mismatch**: if the vocabulary used in a search query does not match the vocabulary used in the documents being searched, query transformation can be used to map the query terms to the appropriate terms used in the documents.

### What techniques can be used to apply transformations/expansions to user queries?

There are several techniques that can be used to transform/expand user queries:

- **Synonym expansion**: involves adding synonyms or related terms to the query.
- **Stemming**: involves reducing words to their base form, or stem, in order to capture variations of a word.
- **Phrase expansion**: involves adding common phrases or collocations to the query.
- **Proximity expansion**: involves adding terms to the query that are frequently found near the original query terms in the documents being searched.
- **Concept expansion**: involves adding terms to the query that are related to the original query terms conceptually.

### Identify and describe query expansions techniques, such as relevance feedback or pseudo-relevance feedback.

- **Relevance feedback** aims to improve the accuracy of search results by taking into account the relevance of the documents that a user has clicked on or otherwise indicated are relevant by providing explicit feedback.
- **Pseudo relevance feedback** uses automatically generated, rather than user-provided, relevance judgments to improve the accuracy of search results. This can be useful in cases where it is difficult to obtain relevance judgments from users.
- **Implicit relevance feedback** uses a user's search behavior, such as the documents they click on or the queries they submit, to infer their relevance preferences and improve the accuracy of search results. Implicit feedback is less reliable than explicit feedback, but is more useful than pseudo relevance feedback, which contains no evidence of user judgements.

# Entity-oriented Search

### What is entity-oriented search? What is necessary to implement it?

Entity-oriented search is the search paradigm of organizing and accessing information centered around entities, and their attributes and relationships.

To implement entity-oriented search, the following is typically necessary:

- **Entity recognition**: recognize and extract entities from the text of the documents being searched. This can be done using natural language processing (NLP) techniques such as named entity recognition (NER).
- **Entity indexing**: index the entities extracted from the documents, so that they can be searched efficiently.
- **Entity ranking**: rank the entities in the search results based on their relevance to the search query.
- **Entity-aware query processing**: process queries that are expressed in terms of entities, rather than just individual keywords.

### Describe the challenges and techniques associated with building entity descriptions, entity ranking and entity linking.

**Entity Descriptions**:

- The goal of constructing entity descriptions is to estimate a term count associated with each entity.
- Entity descriptions can be assembled by considering the textual content, from a document collection, in which the entities occurs.
- One challenge associated with building entity descriptions is determining which information about the entity is most relevant and useful to include in the description.
- Techniques such as collaborative filtering, user modeling, and user feedback can be used to tailor the entity descriptions to the needs and preferences of the users.

**Entity Ranking**:

- With the term-based entity representations, one now needs to rank entities with respect to their relevance to a search query. This can be viewed as a the problem of assigning a score to each entity in the catalog.
- One challenge associated with entity ranking is determining which entities are most relevant to a particular search query. This can be difficult, as different users may have different definitions of relevance, and the same entity may be relevant for different reasons in different contexts.
- Techniques such as machine learning, natural language processing, and information retrieval can be used to automatically assess the relevance of entities based on various features such as their content, context, and user feedback.

**Entity Linking**:

- Entity linking is the task of recognizing entity mentions in text and linking them to the corresponding entries in a knowledge base.
- One challenge associated with entity linking is determining which entity a particular mention of an entity in a document refers to. This can be difficult, as there may be multiple entities with similar names or descriptions, and the mention of the entity may not provide enough context to distinguish between them.
- Techniques such as entity disambiguation, named entity recognition, and knowledge base reasoning can be used to identify the correct entity based on various features such as the context in which the entity is mentioned, the relationships between the entities, and the properties of the entities.

### Describe the data sources typically required for entity oriented search and its characteristics.

Entity-oriented search typically requires data sources that contain information about entities, such as their names, descriptions, relationships, and properties. Some examples include:

- **Knowledge bases**: structured collections of information (structured data) about entities and their relationships.
- **Web pages**: unstructured collections of text and other content (unstructured data) that can be found on the web. Web pages can be a good source of information about entities, but the information may be scattered and unstructured, and may require additional processing to extract and structure the entity-related information.
- **Social media**: can be a good source of information about entities, but the information may be noisy, biased, or unreliable.
- **Enterprise data**: structured collections of information (structured data) about entities that are specific to a particular organization or domain, such as customer records or product catalogs.

# Search User Interfaces

### Identify and describe user interface techniques and elements that can be used to improve user experience in using search systems.

There are several user interface (UI) techniques and elements that can be used to improve the user experience in using search systems, including:

- **Autocomplete**: suggesting search terms or phrases as the user types can save time and help users find what they're looking for more quickly.
- **Filters**: allowing users to narrow down their search results by applying filters can help them find more relevant results and improve their overall search experience.
- **Sort options**: providing options to sort search results can help users find the most relevant or up-to-date results for their search.
- **Related searches**: showing users a list of related searches can help them discover new and relevant content, and can also help them refine their search if their initial search was not successful.
- **Search suggestions**: providing users with suggested search terms or phrases can help them discover new content and refine their search.
- **Synonym support**: allowing users to search for synonyms of their search terms can help them find more relevant results and improve their overall search experience.
- **Faceted search**: applying multiple filters at once can help them find more relevant results and improve their overall search experience.

### Describe how user interaction innovations and experiments can be evaluated.

- **IR style**: systems are evaluated within a TREC-style environment, based on datasets, specific tasks, and known best results for each task (calculated by human experts).
- **Empirical**: observing and recording actual user performance. Common measurements used in empirical user studies are the number of searches, the number of terms per search, the number of results visited, search times, task accuracy, etc. Qualitative methods such as interviews, surveys and observations are also possible.
- **Analytical**: collecting data on how users interact with the system, and then analyzing that data to identify patterns and trends, and ultimately identify areas for improvement.

### What are design principles and heuristics?

1. **Visibility** - keep the user informed about what is happening at any given time.
2. **Language** - adopt language that the user can understand.
3. **Control and freedom** - do not block users in a hole or fixed pathway, instead provide mechanisms to recover from them.
4. **Consistency** - adopt a consistent design that follows the same conventions.
5. **Error prevention** - make it hard to do unproductive things, i.e. avoid the need to
   undo actions.
6. **Support recognition** - help users not have to remember what they have done or
   need to do.
7. **Flexibility and efficiency** - provide features and shortcuts that allow users to be more productive and efficient.
8. **Aesthetics and minimalism** - keep design simple and minimalist.
9. **Clear error messages** - provide informative and useful error messages.
10. **Help and documentation** - provide help as documentation, FAQs, and examples.

# Learning to Rank and Neural IR

### What is Learning to Rank?

Learning to Rank (LtR) is a machine learning technique used to improve the performance of search engines and other information retrieval systems, which involves training a model to predict the relevance of a document to a given query, based on features of the document and query.

In a typical learning to rank setup, the model is trained using a labeled dataset that consists of query-document pairs, along with a relevance label indicating how relevant the document is to the query. The model is then able to predict the relevance of new query-document pairs, based on the features of the query and document.

### Which are the main approaches in LTR? How do they differ in terms of input and output data?

There are many different approaches to learning to rank, including pointwise, pairwise, and listwise methods. These methods differ in how they handle the ranking of multiple documents for a given query, and in how they define the loss function used to train the model.

|               | Pointwise                                                                                                                            | Pairwise                                                                                                                                                             | Listwise                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Input         | query-document pairs, along with a relevance label indicating the relevance of the document to the query                             | query-document pairs, along with a relevance label indicating the relative ordering of the documents for the query (e.g. (q,d,d’) — d is more relevant to q than d’) | entire group of documents associated with a query, i.e. ranking lists                                                                         |
| Output        | relevance degree of each single document (e.g., R/NR)                                                                                | pairwise preferences (ranging from 1 to -1) between document pairs                                                                                                   | full document predicted ranking for query                                                                                                     |
| Advantages    | it is relatively simple to implement, as it only requires predicting the relevance of individual documents                           | it can handle the ranking of multiple documents for a given query more directly, compared to pointwise methods, which treat each document independently              | it can directly optimize for the overall ranking of documents for a given query, rather than just the relative ordering of pairs of documents |
| Disadvantages | it may not be as effective at ranking multiple documents for a given query, as it does not directly optimize for the overall ranking | it can be more computationally expensive, as it requires training on all pairs of documents for a given query                                                        | it can be more difficult to implement, as it requires the model to learn to assign relevance scores to individual documents                   |

### What is Neural Information Retrieval?

Neural Information Retrieval (NIR) deals with the use of neural network models for tasks such as document ranking and recommendation. It aims to improve the effectiveness and efficiency of IR systems by leveraging the ability of neural networks to process large amounts of data and learn complex patterns. NIR models are often used in situations where traditional information retrieval techniques are insufficient, such as when dealing with large collections of unstructured or partially structured data. Unlike LtR approaches that train ML models over a set of hand-crafted features, NIR models accept the raw text of a query and document as input.

### How can neural models be used in the retrieval process?

- **Document ranking**: can be used to score and rank documents based on their relevance to a given query. This is typically done by training a neural network to predict the relevance of a document given the query and other relevant information, such as the content of the document and its metadata.

- **Query expansion**: can be used to generate additional terms or phrases that are related to a given query, in order to improve the recall of the retrieval system. This can be done by training a neural network to predict related terms given a query and a collection of documents.

- **Document representation**: can be used to generate compact, dense representations of documents, known as document embeddings, which can be used as input to other information retrieval tasks such as document classification or ranking. Document embeddings can be learned by training a neural network to predict the contents of a document given a small set of summary information.

- **Query suggestion**: can be used to generate suggestions for queries that are related to a given input query. This can be done by training a neural network to predict queries that are likely to be related to a given input query, based on the co-occurrence of queries in a large dataset of search logs.

- **Recommendation**: can be used to generate recommendations of documents or other items based on their relevance to a given query or the preferences of a user. This can be done by training a neural network to predict the relevance of items given a query or user profile, and ranking the items accordingly.

### What are word embeddings?

A word embeddings are numerical vectors that represent the semantic meaning of a given term sequence. One of the key benefits of using word embeddings is that they can capture the semantic relationships between words, which is important for many NLP tasks.

### What is the difference between Learning to Rank and Neural Information Retrieval?

Learning to rank (LtR) is a machine learning approach to ranking problems, where a model is trained to predict the relevance of a document to a given query. The goal is to rank the documents in a list such that the most relevant documents are presented to the user first. Neural Information Retrieval (NIR) is a subfield of IR that focuses on the use of neural network models for IR tasks. NIR aims to improve the performance of IR systems by leveraging the capabilities of neural networks to learn complex relationships between queries and documents, and to handle large amounts of data.

There are some key differences between learning to rank and NeuIR:

- LtR is primarily concerned with ranking documents based on their relevance to a given query, whereas NIR is a broader field that encompasses a range of IR tasks such as document retrieval, question answering, and recommendation systems.

- LtR typically involves the use of traditional machine learning algorithms (e.g. gradient boosting, random forests) to learn a ranking function, whereas NIR involves the use of neural network models.

- LtR is often used in the context of web search engines, where the goal is to rank webpages based on their relevance to a user's query. NIR can be applied to a wide range of IR tasks and is not limited to web search.

# Other Important Formulas

### Precision (P)

Fraction of retrieved items that are relevant.

~~~
  P = #(relevant items retrieved) / #(retrieved items)
  P = TP / (TP + FP)
~~~

### Recall (R)

Fraction of relevant items that are retrieved.

~~~
  R = #(relevant items retrieved) / #(relevant items)
  R = TP / (TP + FN)
~~~

### Average Precision (AvP)

Average of the precision value obtained for the set of top k documents existing after each relevant document is retrieved. 

### Mean Average Precision (MAP)

Mean over the AvP values.

### F-Measure (F)

![Screenshot from 2023-01-09 16-08-48](https://user-images.githubusercontent.com/55671968/211355200-b4193f36-0194-4ede-aea4-02a1a0a0499d.png)

### Interpolated Precision (P<sub>interp</sub>)

![image](https://user-images.githubusercontent.com/55671968/211355456-5eb0e738-dd96-4e2c-a814-83cc570b7fc8.png)

### Inverse Document Frequency (idf<sub>t</sub>)

![Screenshot from 2023-01-09 16-11-33](https://user-images.githubusercontent.com/55671968/211355267-673462f6-9f37-4899-968f-e0604ccac73d.png)

### Term Frequency - Inverse Document Frequency (tf-idf<sub>t,d</sub>)

![Screenshot from 2023-01-09 16-11-46](https://user-images.githubusercontent.com/55671968/211355393-2864d1eb-101d-4c8a-b9dd-3c6b80f56496.png)



