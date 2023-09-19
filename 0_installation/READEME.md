# Install TensorFlow Federated (Ubuntu 20.04)
    
## Tự build thư viện TensorFlow Federated Python từ [repository](https://github.com/tensorflow/federated.git) gốc trên github của TFF

- Ta có thể tự custom lại code bên trong thư viện và có được bản cài đặt riêng của mình.
- Có thể sử dụng được version mới nhất của TFF (nightly build) chứ không phải version đã được release.

1. Cài đặt python cho ubuntu
    ```
    sudo apt update
    sudo apt install python3-dev python3-pip  
    ```
2. Cài đặt [Bazel](https://bazel.build/install).
    Công cụ cần thiết sử dụng để biên dịch Tensorflow Federated.
3. Clone repo của TFF.
    ```
    git clone https://github.com/tensorflow/federated.git
    cd "federated"
    ```
4. Tạo môi trường ảo cho python.
    ```
    python3 -m venv "venv"
    source "venv/bin/activate"
    pip install --upgrade "pip"
    pip install numpy
    ```
5. Build thư viện TensorFlow Federated thành package Python tại máy.
    ```
    mkdir "/tmp/tensorflow_federated"
    bazel run //tensorflow_federated/tools/python_package:build_python_package -- \
    --output_dir="/tmp/tensorflow_federated"
    ```
6. Thoát khỏi môi trường ảo python.
    ```
    deactivate
    ```
7. Tạo một dự án mới như thư mục này.
    ```
    mkdir "0_installation"
    cd "0_installation"
    ```
8. Tạo một môi trường ảo mới cho python.
    ```
    python3 -m venv "venv"
    source "venv/bin/activate"
    pip install --upgrade "pip"
    ```
9. Cài thư viện TensorFlow Federated vừa build vào môi trường ảo bằng pip.
    ```
    pip install --upgrade "/tmp/tensorflow_federated/"*".whl"
    ```
10. Kiểm tra thư viện TensorFlow Federated đã cài đặt thành công chưa.
+ Tạo tệp [main.py](./main.py) với script python sau:
    ```
    import tensorflow_federated as tff; 
    print(tff.federated_computation(lambda: 'Hello World')())
    ```
+ Chạy script để kiểm tra xem quá trình cài đặt có thành công không
    ```
    python3 main.py
    ```