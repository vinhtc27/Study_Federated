# Install TensorFlow Federated

## There are a few ways to set up your environment to use TensorFlow Federated (TFF):

- The easiest way to learn and use TFF requires no installation; run the TensorFlow Federated tutorials directly in your browser using Google Colaboratory.

- To use TensorFlow Federated on a local machine, install the TFF package with Python's pip package manager.

- If you have a unique machine configuration, build the TFF package from source .

## Install TensorFlow Federated using pip

1. Install the Python development environment.

```
sudo apt update
sudo apt install python3-dev python3-pip
```

2. Create a virtual environment.

```
python3 -m venv "venv"
source "venv/bin/activate"
pip install --upgrade "pip"
```

Note: To exit the virtual environment, run deactivate.

3. Install the released TensorFlow Federated Python package.

```
pip install --upgrade tensorflow-federated
```

4. Test Tensorflow Federated.

```
python -c "import tensorflow_federated as tff; print(tff.federated_computation(lambda: 'Hello World')())"
```
