# User Stories 

## Story #1 
**User:** Dr.Julia is a univerisity professor specializing in Latin literature.  
**Goal:**  Dr. Julia wants to analyze the meter of verses in the Aeneid to teach students about the usage of dactylic hexameter. 
**Needs and Desires:** Dr. Julia needs a reliable and precise tool for metrical analysis that can automatically identify and parse dactylic patterns. She values accuracy, and the ability to generate detailed, exportable reports for classroom examples. 
**Skill Level:** She's an expert in Latin poetry with intermediate programming skills, familiar with Python but not advanced with NLP libraries.   

 ## Story #2 
**User:** Sonia is a graduate student in Classics.   
**Goal:** Sonia wants to use Carmina to analyze the meter in several latin poetry pieces specifically looking at deviations from traditional dactylic hexameter.  
**Needs and Desires:** Sonia wants a flexible tool that can identify metrical variations and provide simple visualizations for research presentations. She values a user-friendly interface and documentation that explains the function of a parameter.  
**Skill Level:** She is proficient in Latin, beginner in programming, with limited experience in NLP and Python packages.  

## Story #3 
**User:** Maria is a high school Latin teacher.   
**Goal:** Maria wants Carmina to help her demonstrate metrical patterns of poetry of Ovid to her students as part of an introductory Latin poetry course.  
**Needs and Desires:** She wants a straightforward tool that provides clear outputs such as labeling each foot in a line of poetry. She values simplicity over complexity, preferring a few well-documented functions over extensive customization.   
**Skill Level:** Maria is proficient in Latin, minimal programming experience; requires a tool that works with simple commands and minimal setup.   

## Story #4 
**User:** Dr. Roberto is a digital humanities researcher focused on Latin poetry.   
**Goal:**  Dr. Roberto wants to conduct metrical analysis on Latin poetry collections to identify broader trends in meter across authors.
**Needs and Desires:** He needs a tool that allows for batch processing of texts, with customizable parameters for different poetic meters. Dr. Roberto values customization and the ability to integrate Carmina’s outputs with other data analysis tools. 
**Skill Level:** Advanced user with strong programming skills, familiar with Python and NLP concepts. 

## Story #5 
**User:** Sarah is an undergraduate majoring in Classics and minoring in Data Science. 
**Goal:** Sarah wants to analyze metrical patterns in selected poems for her final project, aiming to understand the influence of meter on thematic elements in Latin literature. 
**Needs and Desires:** She needs a tool that offers guided usage with example datasets and has an intuitive API that makes it easy to analyze smaller sections of text. She values accessible documentation and error messages that provide clear troubleshooting information. 
**Skill Level:** Intermediate Latin knowledge, beginner Python skills, familiar with basic functional programming but not object-oriented programming.

## 1. Metrical Analysis of Latin Verses
As a Classics researcher
I want to automatically identify the meter and foot structure of Latin verses
So that I can perform metrical analysis on poems without manually scanning each line.

## 2. Rhythm Pattern Mapping Across Stanzas
As a Classics researcher interested in rhythmic variation
I want a tool that maps rhythm and stress patterns across multiple stanzas
So that I can identify rhythmic shifts and recurring patterns that contribute to the poem’s overall structure and mood.

## 3. Visualizing Rhythm and Stress Patterns
As a Latin poetry researcher interested in auditory analysis
I want a feature to visualize the rhythm and stress patterns of a poem
So that I can understand the poem’s auditory impact and perform better prosodic analysis.

## 4. Comparative Metrical Analysis Across Poems

As a Latin poetry scholar
I want to compare metrical patterns across multiple poems or authors
So that I can analyze stylistic variations in metrical choices and determine if certain meters correlate with specific themes or genres.

## 5. Foot Structure Visualization and Analysis
As a student learning Latin poetry structure
I want to visualize each foot’s structure within a line
So that I can better understand the function and rhythm of different feet in Latin meter.

## Undergrad student

Virgil is an undergrad Latin major working on his poetry composition homework. He wants to use the `carmina` package to scan the epic he's written to verify that his lines are all in dactylic hexameter. He'd like the function to go line-by-line and output exactly which syllables are short and which are long. He's never taken a programming class before because all his time has been spent on his Latin degree.

## Grad student

Cicero is working on his PhD. He wants to use the `carmina` package to track instances of the same phrase in the speeches he's analyzing. He's also interested in figuring out how often the speeches use hypotactic versus paratactic sentence structure. He's taken a few programming classes and understands how procedural programming works in Python.

## DH Scholar

Vitruvius is interested in looking at alliteration across dactylic hexameter. He doesn't know much Latin, but he does know how to use Python for text analysis. He's done alliteration studies in other natural languages.

## DH Scholar 2

Hypatia is working with Vitruvius's lab, but she's more interested in looking at alliterative figures within the same line. She's better versed in Latin and Python.

## New Latin Student

Julius is new to Latin epic, but he doesn't know a lot about scansion. However, his Latin class has a scansion assignment due tomorrow, and he doesn't know how to do it! On the other hand, he does know some Python, and he's familiar enough with Latin to know how to read it. He'll try to use the hexameter scansion function from `carmina` to finish his homework.
