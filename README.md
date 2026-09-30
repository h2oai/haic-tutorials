# H2O AI Cloud Code Samples and Tutorials

This repo provides code examples and tutorials demonstrating how to use the H2O AI Cloud from the python API clients.

## Running Locally

These tutorials were explicitly tested last in H2O AI Cloud v26.09.1 and python 3.10+ with the following specific library versions:

```bash
pip install h2o_authn==1.0.0
pip install h2o-engine-manager==1.10.0
pip install h2o-mlops==1.6.4
pip install driverlessai==2.5.0
pip install h2o==3.46.0.11
```

For `3 DriverlessAI: AutoML`

```bash
pip install pandas==3.0.6
pip install scikit-learn==1.9.1
pip install matplotlib==3.11.2
pip install numpy"<2.0.0"
```bash

### Setup your connection

Update the `h2o_ai_cloud.py` file with the connection parameters for your H2O AI Cloud environment:

1. Log in to your H2O AI Cloud environment
1. Click your username or avatar in the H2O AI Cloud navigation bar
1. Navigate to `CLI & API Access` or https://<your cloud url>/cli-and-api-access
1. Use `Use the Python APIs` section `Connect to the platform` to populate the parameters


### Documentation

* H2O AI Cloud user guide: https://docs.h2o.ai/haic/latest/
* Authorization package: https://pypi.org/project/h2o-authn/

* AI Engine Manager product documentation: https://docs.h2o.ai/ai-engine-manager/
* AI Engine Manager python documentation:  https://docs.h2o.ai/ai-engine-manager/py/installation

* Driverless AI product documentation: https://docs.h2o.ai/driverless-ai/1-10-lts/docs/userguide/index.html
* Driverless AI python documentation: https://docs.h2o.ai/driverless-ai/pyclient/docs/html/index.html
* Driverless AI additional examples: https://github.com/h2oai/driverlessai-tutorials/tree/master/dai_python_client

* H2O-3 product documentation: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html
* H2O-3 python documentation: https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/index.html
* H2O-3 additional tutorials: https://github.com/h2oai/h2o-tutorials

* MLOps product documentation: https://docs.h2o.ai/mlops/
* MLOps python documentation: https://docs.h2o.ai/mlops/py-client-installing/

