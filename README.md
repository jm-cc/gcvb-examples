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
- Given the input, the user can generate a *base*, that base can then be used for multiple *runs*. Each run compares with the reference and allows to check that everything is in order (or not). A run can launch a subset of the test of a base through filter options.

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

## default_values.yaml

This file shows how it is possible to set default values and how they are propagated.
It is possible to define a "default_values" mapping that will fill some fields in the Tests, Tasks and Validations nodes.

How to see how values are overrided, use the sub-command list that propagate default values.
```
python -m gcvb --yaml-file default_values.yaml list
```

## validation_example.yaml

This example file shows the three ways to do a validation.
- Using an absolute reference (configuration_independent).
- Using a reference that is configuration dependent (configuration_dependent)
- Using a comparison vith a file. (file_comparison)

When comparing to a file, the id of the validation is *{dir}-{ref}* where *dir* is the folder inside 
the references folder and *ref*, the id in the *ref.yaml* file.

```
data
└── validation_example
    ├── input
    └── references
        └── base
            ├── ref1
            ├── ref2
            └── ref.yaml
```

In this example, the scripts *custom_scripts/diff.py* and *custom_scripts/add_custom_metrics.py* are used to fill the database.

```
#To run this example and get a quick report : 
python -m gcvb --yaml-file validation_example.yaml generate
python -m gcvb compute
python -m gcvb report
```


## template_example.yaml

It is also possible to generate test using a template. Some value can be replaced inside the yaml file and in some input files also.

In a test, the node *template_files* indicate where to find the files to be added. Like references, multiple templates can be associated with a test case.

```
├── data
│   └── template_example
│       ├── input
│       ├── references
│       └── templates
│           └── afolder
│               ├── A.txt
│               └── B.txt
```

As usual, you can see which test will be generated using the subcommand *list*.

## Modify a yaml input file with a python program.

You may want to modify an input yaml file with a program. Or use an empty one and create your gcvb base using only a python script.

It is possible to do so using the *--modifier* options and a module that implements "modify", a function that takes and returns a dict corresponding to the gcvb input. An example of such a script is *getting_started/custom_scripts/modifier_example.py* which just change the id of the tests. The input passed as parameter comes after the template expansion.

You can experiment this feature with this command line in the getting started folder:
```
python -m gcvb --yaml-file validation_example.yaml --modifier "custom_scripts.modifier_example" list
```