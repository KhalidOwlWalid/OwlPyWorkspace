If you are interested in creating a python package yourself, I personally enjoy using the `setup.py` implementation where your basic setup should look like the following:

```shell
my_new_custom_package/
├── my_new_custom_package/
│   ├── __init__.py
│   ├── data/
│   │   └── example.txt
│   └── main.py
├── MANIFEST.in
├── setup.py
└── README.md
```

## setup.py
The setup.py contains all of the metadata of your packages along with the necessary packages that should be included.

```
include_package_data=True
```
This line ensures that all of the non-python files you have included in the MANIFEST.in gets included in the distribution build.

To find out if your non-python files were included, run the following command:

```shell
python3 setup.py sdist
```

This then generates a `dist` directory in your root directory, in which it then includes a `tar.gz` file which you can extract for your application. You can check if your non-python files are indeed included by extracting the file.