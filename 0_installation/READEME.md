# Install TensorFlow Federated (Ubuntu 20.04)

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
    
## Build the TensorFlow Federated Python package from source

Building a TensorFlow Federated Python package from source is helpful when you want to:

- Make changes to TensorFlow Federated and test those changes in a component that uses TensorFlow Federated before those changes are submitted or released.
- Use changes that have been submitted to TensorFlow Federated but have not been released.

1. Install the Python development environment.
    ```
    sudo apt update
    sudo apt install python3-dev python3-pip  # Python 3
    ```
2. Install [Bazel](https://bazel.build/install).
    Build tool used to compile Tensorflow Federated.
3. Clone the Tensorflow Federated repository.
    ```
    git clone https://github.com/tensorflow/federated.git
    cd "federated"
    ```
4. Create a virtual environment.
    ```
    python3 -m venv "venv"
    source "venv/bin/activate"
    pip install --upgrade "pip"
    pip install numpy
    ```
5. Build the TensorFlow Federated Python package.
    ```
    mkdir "/tmp/tensorflow_federated"
    bazel run //tensorflow_federated/tools/python_package:build_python_package -- \
    --output_dir="/tmp/tensorflow_federated"
    ```
6. Exit the virtual environment
    ```
    deactivate
    ```
7. Create a new project (like this folder)
    ```
    mkdir "0_installation"
    cd "0_installation"
    ```
8. Create a new virtual environment.
    ```
    python3 -m venv "venv"
    source "venv/bin/activate"
    pip install --upgrade "pip"
    ```
9. Install the TensorFlow Federated Python package.
    ```
    pip install --upgrade "/tmp/tensorflow_federated/"*".whl"
    ```
10. Test Tensorflow Federated.
    + create [main.py](./main.py) file with script
        ```
        import tensorflow_federated as tff; 
        print(tff.federated_computation(lambda: 'Hello World')())
        ```
    + run script to test if installation was successful
        ```
        python main.py
        ```