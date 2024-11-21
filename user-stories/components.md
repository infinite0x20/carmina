# Components

## Language Verification Logic
**What it does:**  Verifies that the text is in Latin  
**Inputs:**  A `.txt` or `.xml` file  
**Outputs:**  True or false (true if text is Latin, false otherwise)  
**Components:**  Reader that verifies that the text is in Latin, likely against Logeion (online Latin dictionary site).  
**Side effects?**  Will work as part of the larger Data Validation Logic

## Data Validation Logic
**What it does:** Verfies the text is in latin, in a txt or xml.file, and reads as poetry.  
**Inputs:** Must be able to read the file and have be able to create a xml or txt.file copy/version of the file.  
**Outputs:** Outputs results to another file xml or txt format that is downloadable to the user.  
**Components:** A verification reader that helps verify the language is latin. This will come from an external database (aka the dictionary site we referred back to).  
**Side effects?** Not sure. 

## File Parser
**What it does:** Converts the input .txt or .xml file into a structured, machine-readable format for further analysis. Ensures the file is properly segmented into lines of text, identifies headers or metadata, and formats content for compatibility with the scansion function.
**Inputs:** A .txt or .xml file containing Latin text (validated by the Data Validation Logic).
**Outputs:** A structured file or object containing parsed lines of text (e.g., a list or data frame where each line is an element).
**Components:**
**File Reader:** Reads the raw input file.
Line Segmenter: Breaks the content into lines, ignoring empty lines or non-poetic metadata.
Metadata Extractor: Optionally identifies and stores non-poetic metadata (e.g., author, title).
Side effects? If the input file has formatting issues, parsing errors may occur, requiring fallback mechanisms or error messages for the user.

## Scansion Function
**What it does:**  Given a file of dactylic hexameter, returns the scansion and feet of each line  
**Inputs:**  A parsed Latin file  
**Outputs:**  Another file that shows the original text and the scansion  
**Components:**  This is one of the functions that we will write as part of the package. Needs to be able to read lines from a parsed file and apply the scanning algorithm to determine the placement of long and short syllables.  
**Side effects?**  Probably will not affect other functions, but is dependent on proper parsing and verification
