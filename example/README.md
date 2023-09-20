# Hướng dẫn sử dụng thư viện TensorFlow Federated (TFF)

## Đoạn script Python [main.py](./main.py) sử dụng thư viện TFF để mô phỏng quá trình huấn luyện mô hình trên các máy khánh một cách phân tán. 

+ Dưới đây là mô tả chi tiết về các chức năng chính của script và các đoạn log để biểu diễn quá trình huấn luyện.
1. Import thư viện TensorFlow và TensorFlow Federated:'
    ```
    import tensorflow as tf
    import tensorflow_federated as tff
    ```
2. Tải dữ liệu mô phỏng từ EMNIST (Extended MNIST dataset). Đoạn mã này tải dữ liệu mô phỏng EMNIST và chuẩn bị dữ liệu cho từng máy khách cho việc huấn luyện:
    ```
    source, _ = tff.simulation.datasets.emnist.load_data()

    def client_data(n):
    return source.create_tf_dataset_for_client(source.client_ids[n]).map(
        lambda e: (tf.reshape(e['pixels'], [-1]), e['label'])
    ).repeat(10).batch(20)
    ```
3. Chọn một tập hợp các máy khách để tham gia vào quá trình huấn luyện. Trong ví dụ này, chọn 3 máy khách:
    ```
    train_data = [client_data(n) for n in range(3)]
    ```
4. Định nghĩa mô hình Keras và đóng gói nó để sử dụng với TFF. Mô hình này có một lớp Dense với 10 đầu ra và hàm kích hoạt softmax:
    ```
    def model_fn():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(10, tf.nn.softmax, input_shape=(784,), kernel_initializer='zeros')
    ])
    return tff.learning.models.from_keras_model(
        model,
        input_spec=train_data[0].element_spec,
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
    ```
5. Thuật toán huấn luyện sử dụng build_weighted_fed_avg từ TFF. Thuật toán này sẽ sử dụng mô hình được định nghĩa trước đó để huấn luyện trên các máy khách. Đồng thời, chọn tối ưu hóa SGD với learning rate 0.1 cho mỗi máy khách:
    ```
    trainer = tff.learning.algorithms.build_weighted_fed_avg(
    model_fn,
    client_optimizer_fn=lambda: tf.keras.optimizers.SGD(0.1))
    ```
6. Khởi tạo trạng thái ban đầu của trainer:
    ```
    state = trainer.initialize()
    ```
7. Thực hiện và ghi log cho một số training round (ví dụ 5 round). Trong mỗi round, train trên máy khách và in ra loss value của từng máy khách:
    ```
    for _ in range(5):
    result = trainer.next(state, train_data)
    state = result.state
    metrics = result.metrics
    print(metrics['client_work']['train']['loss'])
    ```
+ Các đoạn log in ra loss value của từng máy khách trong mỗi vòng lặp huấn luyện, giúp ta theo dõi, đánh giá hiệu suất của mô hình trên từng máy khách.

