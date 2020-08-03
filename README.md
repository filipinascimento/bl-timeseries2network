[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.393)

# Conmat 2 Network
This simple app converts a conmat datatype to a network datatype (JGFZ) so it can be used in the network pipeline.

### Authors
- [Filipi N. Silva](filsilva@iu.edu)

<!-- ### Contributors
- Franco Pestilli (franpest@indiana.edu) -->

### Funding
[![NIH-1R01EB029272-01](https://img.shields.io/badge/NIH-1R01EB029272_01-blue.svg)](https://www.nibib.nih.gov/node/113361)


## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.393](https://doi.org/10.25663/brainlife.app.393) via the "Execute" tab.

### Running Locally (on your machine)
Singularity is required to run the package locally.

1. git clone this repo.

```bash
git clone <repository URL>
cd <repository PATH>
```

2. Inside the cloned directory, edit `config-sample.json` with your data or use the provided data.

3. Rename `config-sample.json` to `config.json` .

```bash
mv config-sample.json config.json
```

4. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

A sample dataset is provided in folder `data` and `config-sample.json`

## Output

The output is a network file containing all the properties from the conmat.


<!-- #### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.  -->

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install the python packages defined in `environment.yml`, then you can run the code directly from python using:  

```bash
./main.py config.json
```

