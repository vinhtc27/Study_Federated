import tensorflow_federated as tff; # Import thư viện tff vào trong chương trình

print(tff.federated_computation(lambda: 'Hello World')()) # Chạy thử chương trình để in ra màn hình Hello World