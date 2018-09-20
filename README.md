# ufo2to3

A Python script that upconverts UFO typeface source files from the UFO v2 to UFO v3 specification.  Built with the defcon library.

## Dependencies

- Python 3 interpreter
- [defcon](https://github.com/typesupply/defcon) Python library

## Usage

### Install Dependency

```
$ pip3 install defcon
```

### Convert UFO source from version 2 to version 3

**NOTE**: The script writes the new source files **in place** so please work in a separate branch or with copies of your original files if you want to maintain the original source files!

Download the ufo2to3.py script that is located in the root of this repository.  Execute the script with the Python 3 interpreter using one or more UFO source directories as arguments to the script:

```
$ python3 ufo2to3.py [UFO source path 1] ... [UFO source path n]
```


The script prints a success message upon completion of the upconversion of your source files.  Note that, in most cases, you will see a very large diff against your previous file state after this conversion.  This is expected and normal behavior.

## License

[MIT License](LICENSE)