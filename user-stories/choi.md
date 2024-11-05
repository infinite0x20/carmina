# User Stories

## Undergrad student

Virgil is an undergrad Latin major working on his poetry composition homework. He wants to use the `carmina` package to scan the epic he's written to verify that his lines are all in dactylic hexameter. He'd like the function to go line-by-line and output exactly which syllables are short and which are long. He's never taken a programming class before because all his time has been spent on his Latin degree.

## Grad student

Cicero is working on his PhD. He wants to use the `carmina` package to track instances of the same phrase in the speeches he's analyzing. He's also interested in figuring out how often the speeches use hypotactic versus paratactic sentence structure. He's taken a few programming classes and understands how procedural programming works in Python.


# Use Cases

## Authentication

Users input the text they want to work with. They use functions on the text to produce the output, which is just the desired analytics. There are almost no interactive components.

## Data Validation
Files need to be XML or .txt and they'll need to be in Latin (assuming dactylic hexameter, but this will be verified through the scansion)
