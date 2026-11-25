[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.393)

# Timeseries 2 Network

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes a connectivity matrix (correlation, covariance, partial correlation, tangent or precision) from regional time series with nilearn and saves it as a network (JGFZ) for the brainlife network pipeline.**

Reads a TSV of time series (one column per node) and its JSON node metadata, computes the chosen nilearn ConnectivityMeasure, zeroes the diagonal and writes a weighted network in compressed JSON Graph Format with the column names and metadata as node properties. Use it to turn parcel-wise fMRI time series into a functional connectivity network for later network analyses.

| | |
|---|---|
| 📥 **Inputs** | `generic/timeseries` |
| 📤 **Outputs** | `generic/network` |
| 🐳 **Container** | `filsilva/cxnetwork:0.2.3` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.532](https://doi.org/10.25663/brainlife.app.532) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `timeseries` | `generic/timeseries` | yes | Input time series used to construct the connectivity matrices. TSV with one column per node (column headers become node labels) and a JSON list with one metadata entry per node. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `generic/network` | Network generated from the connectivity matrix |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `method` | enum | `correlation` | Measure of similarity used to create the connectivity matrix. [1] G. Varoquaux et al. “Detection of brain functional-connectivity difference in post-stroke patients using group-level covariance modeling, MICCAI 2010. Options: `correlation`, `covariance`, `partial correlation`, `tangent`, `precision`. |

</details>

📚 **References used by this App:**
- Avesani P. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Bassett D. S., Sporns O. Network neuroscience. Nature Neuroscience 20(3):353 (2017). [doi:10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

<!-- brainlife-app:end -->

This simple app calculates a similarity matrix from time series and convert it to a network datatype (JGFZ) so it can be used in the network pipeline.


### Authors
- [Filipi N. Silva](https://filipinascimento.github.io)

### Contributors
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)
- [Josh Faskowitz](https://faskowit.github.io/) 


### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)


### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)



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

