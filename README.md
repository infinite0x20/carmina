# carmina
CSE 583 Final Project

**Project Members:**
- Suh Young Choi
- Hui-Hsuan Chan
- Elizabeth Nova
- Simon Dovan Nguyen


**Why carmina?**
> *Carmina* is the Latin word for songs or poems. It's a working title, and I don't mind changing it further down the line.

## Goals
- To create a Python package for Classicists to automate reading processes for analyzing poetry

## Values
- Little to no Python knowledge should be required to work with the package
- Readability and comprehensibility to someone who doesn't know a lot of coding in general
- Minimal to no object-oriented programming
- Possibly notebook-based applications (Colab?)
- Focus on File I/O and function calling
- Have as few dependencies as possible outside of base Python

## Immediate Tasks
Specific tasks will be given their own issues and assignees. Here is a high-level summary for what we want to achieve. Immediate tasks are things that we might be able to do more easily, or things that later tasks will build on.

### File Read-in
We need to be able to parse XML files into some useable format, probably a string. We can use XMLs from Perseus as a guide.

### Scansion - Dactylic Hexameter
One of the hallmarks of poetic analysis is being able to scan lines of poetry, or determine their meter. This function, when given an input, should be able to parse a line and return the scansion of that line.

## Intermediate Tasks

### Text Matching
Finding same instances of the same character string in the text. This may be a stepping-stone for more advanced text matching that accounts for inflected forms.

### Meter Matching
Builds off the first scansion function to return lines that have the same metrical scheme.

## Stretch Goals

### Scansion - Other meters
Expanding the `scansion` function to include other meters, like elegaic couplet, iambic trimeter, etc.

### Graphical Interface
Doing away with the low-level code altogether and creating a site/app where users can input their files and work with a UI instead.

## Repository Organization
To be updated as more files are added
