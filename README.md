[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.393)

# Conmat 2 Network
This simple app converts a conmat datatype to a network datatype (JGFZ) so it can be used in the network pipeline.


### Authors
- [Filipi N. Silva](https://filipinascimento.github.io)

### Contributors
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)


### Funding
We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

2. Costa, L. da F., Francisco A. Rodrigues, Gonzalo Travieso, and Paulino Ribeiro Villas Boas. "Characterization of complex networks: A survey of measurements." Advances in physics 56, no. 1 (2007): 167-242.[https://doi.org/10.1080/00018730601170527](https://doi.org/10.1080/00018730601170527)


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

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install the python packages defined in `environment.yml`, then you can run the code directly from python using:  

```bash
./main.py config.json
```

