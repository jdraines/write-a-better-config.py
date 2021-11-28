# Write a Better config.py

This is a very basic example demonstrating the techniques described in my
Medium article, [Write a Better config.py](https://johndanielraines.medium.com/write-a-better-config-py-1a443cf5bb36).

That article suggests the 3 following techniques and gives explanation and code
block examples:

  * Move your information into a structured text file (json/yaml/etc.)
  * Use properties in your config class to control mutability
  * Implement runtime configurables as environmental variables

The code block examples in the article presume a more complex (if ambiguous) application
than the example application shown in this repo. This example application is a
classic command line "Hello World", which uses a `config.yaml` provide settings
for text color and style formatting.

If this package is installed (for example, by running `python setup.py develop`),
then the main module can be executed with the command `python -m hello_world`.

Note the documentation in the `hello_world/config.py` file, which describes the
various default locations that a `config.yaml` can be placed.