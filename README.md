# gcvb-examples

Collection of simple example of gcvb usage. It contains multiple yaml file and some fake data for tests.

## General philosophy

Input : 
- The "data" folder contains the input files and references.
- A config.yaml file contains relevant information for the current computing environment used.
- Multiple yaml files can then be use to indicate which tests to launch, store the references to detect a regression.

Output :
- a gcvb.db sqlite3 database that contains the metrics stored during runs, but also files you want to keep for each run.
- a "results" folder where the computation are actually computed.

Process :
- Given the input, the user can generate a *base*, that base can then be used for multiple *runs*. Each run compares with the reference and allows to check that everything is in order (or not).

gcvb is an executable python module, with subcommands. It must be launch in the folder containing the input.

To access the help :
```
python -m gcvb -h
```

## Getting started

The folder data contains the input data and the references for the different tests cases. It is possible to use sub-folders to organize the input data.
Each data folder must contain an "input" and a "references" folder. A "template" folder is optional.

config.yaml is a special file that is necessary to run gcvb. It contains value for :
- the "machine_id", a string identifying the current configuration being tested.
- the "submit_command", the command used to launch the job scripts that will be created by gcvb. Can be sh or bash if no job scheduler is used.
- executable which is a mapping of mapping containing link for executables used by the gcvb base. If an executable is not present in this mapping, the system default will be used.

## simple_example.yaml

A single pack containing only one test with two tasks. No validation included. Contains a description of the different fields expected by gcvb.

How to run this example : 
```
# inside the getting_started folder, create a base :
python -m gcvb --yaml-file simple_example.yaml generate
# then, you can launch a run associated to the last base created :
python -m gcvb compute
```