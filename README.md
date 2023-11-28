# H2O AI Cloud Code Samples and Tutorials

This repo provides code examples and tutorials demonstrating how to use the H2O AI Cloud from the python API clients.

## Running Locally

These tutorials were explicitly tested last in H2O AI Cloud v22.07.0 and python 3.7+ with the following specific library versions:

```bash
pip install h2o_authn==0.1.1
pip install https://enterprise-steam.s3.amazonaws.com/release/1.8.12/python/h2osteam-1.8.12-py2.py3-none-any.whl
pip install https://s3.amazonaws.com/artifacts.h2o.ai/releases/ai/h2o/mlops/rel-0.56.1/2/h2o_mlops_client-0.56.1%2Bdd66f93.rel0.56.1.2-py2.py3-none-any.whl
pip install https://h2o-release.s3.amazonaws.com/h2o/rel-zumbo/2/Python/h2o-3.36.1.2-py2.py3-none-any.whl

```
### Setup your connection

Update the `h2o_ai_cloud.py` file with the connection parameters for your H2O AI Cloud environment:

1. Log in to your H2O AI Cloud environment
1. Click your username or avatar in the H2O AI Cloud navigation bar
1. Navigate to `CLI & API Access`
1. Use the variables from the `Accessing H2O AI Cloud APIs` section to populate the parameters


### Documentation

* H2O AI Cloud user guide: https://docs.h2o.ai/haic/latest/
* Authorization package: https://pypi.org/project/h2o-authn/
* Steam product documentation: https://docs.h2o.ai/steam/index.html
* Steam python documentation: https://docs.h2o.ai/enterprise-steam/latest-stable/docs/python-docs/index.html
* Driverless AI product documentation: https://docs.h2o.ai/driverless-ai/1-10-lts/docs/userguide/index.html
* Driverless AI python documentation: https://docs.h2o.ai/driverless-ai/pyclient/docs/html/index.html
* Driverless AI additional examples: https://github.com/h2oai/driverlessai-tutorials/tree/master/dai_python_client
* H2O-3 product documentation: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html
* H2O-3 python documentation: https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/index.html
* H2O-3 additional tutorials: https://github.com/h2oai/h2o-tutorials
* MLOps product documentation: https://docs.h2o.ai/mlops/
* MLOps python documentation: https://docs.h2o.ai/mlops/py-client-installing/

