# Jupyter Book Maker

Generates a book-like structure to a collection of Jupyter notebooks.

## Description

It adds a Table of Contents to a given "Table of Contents" file, and adds a header and top and bottom navigator cells to each notebook.

When the collection of notebooks is changed, it is used to update the structure.

## How it works

The code works on a collection of indexed notebooks in a directory and builds a Table of Contents out of the them, which is added to a specified file. It also adds a header and top and bottom navigator cells to each notebook. 

The notebooks should be of one the following forms:
- 'dd.dd-notebookname.ipynb', where 'd' is any digit from 0 to 9;
- 'dd.-notebookname.ipynb', where 'd' is as above;
- 'AX.dd-notebookname.ipynb', where 'd' is as above, 'A' is the uppercase letter 'A' and 'X' is any uppercase letter;
- 'AX.-notebookname.ipynb', where the symbols are as above;
- 'BX.dd-notebookname.ipynb', where 'B' is the upper case letter 'B' and the rest is as above; or
- 'BX.-notebookname.ipynb', where the symbols are as above.

The filenames are read as regular expressions and three groups are extracted from them, as separated by the first two dots. The first group is essentially for the Chapter and the second group is for the  Section number. There are some special cases:
- When the first group is '00', the notebook appears in the beginning and is not numbered. This is useful for the 'Table of Contents', the  'Preface', and the 'Introduction', for instance. 
- When the second group is the empty string '', the section is not numbered. This is useful for 'Part', which does not increase the chapter or section numbers.
- When the first group starts with 'A', it is assumed to be for an Appendix, in which the second letter 'X' is the letter of the Appendix. 
- When the first group starts with 'B', the notebook appears at the end and is not numbered. This is useful for the 'Bibliography', and 'Index' for instance.

The Table of Contents and the navigators follow the lexicographical order, so '' < 'dd' < 'AX' < 'BX', for instance.

## Available functions

The two main functions in this module are
- 'make_book()': adds the Table of Contents, header, and navigators from the data provided in the arguments.
- 'make_book_from_configfile()': adds the Table of Contents, header, and navigators from the data stored in a YAML configuration file given as argument.
The latter function simply reads the parameters from the configuration file and passes them to the 'make_book()' function.

The 'make_book()' function calls the following functions in this module, which take care of each of the features of the bookmaker:
- 'add_contents()': adds the Table of Contents to a selected 'Index' file.
- 'add_book_header()': adds a header to each notebook with a provied book info.
- 'write_navbars()': adds navigation bars to the top and bottom of each notebook.

Each of these later three functions can be called separately, if only one of the features is desired.

When running 'jupyterbookmaker.py' as script, it expects the filename of the configuration file and call the function 'make_book_from_configfile()'.

Look at the documentation for more information on each of these functions and for the other functions available on this package.

## Usage

See the examples in the 'tests' directory:
- From a 'bash' terminal at the 'tests' subdirectory, execute
'''bash
../jupyterbookmaker/jupyterbookmaker.py config1.yml
'''
or any of the other config files. This runs the 'jupyterbookmaker.py' as a script.
- An example of using 'jupyterbookmaker' as a module is in '/tests/makebook_test.py'
- One can also use the module from a jupyter notebook.

## Requirements

It uses the standard libraries
- [re](https:/docs.python.org/3/library/re.html)
- [os](https:/docs.python.org/3/library/os.html)
- [itertools](https:/docs.python.org/3/library/itertools.html)
- [sys](https:/docs.python.org/3/library/sys.html)

Besides the 'libraries in the standard implementation, it requires the 'nbformat' library to interact with the jupyter notebooks,
- [nbformat](https://pypi.org/project/nbformat/),
and the 'yaml' library to read '.yml' configuration files,
- [yaml](https:/docs.python.org/3/library/yaml.html).

## Background

It is based on the three modules in the subdirectory `tools` of the 
[Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) 
by [Jake VanderPlas](http://vanderplas.com/).

It was first derived and modified to be used in the classroom notes for the course [Modelagem Matemática](https://github.com/rmsrosa/modelagem_matematica) of the [Instituto de Matemática of the Universidade Federal do Rio de Janeiro (IM-UFRJ)](https://www.im.ufrj.br).
