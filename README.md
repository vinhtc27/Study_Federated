# Study TensorFlow Federated

## Trịnh Công Vinh - 20021478 - K65N-CLC - UET - VNU.

## Giới thiệu chung về Thư viện [TFF](https://www.tensorflow.org/federated):

TensorFlow Federated (TFF) là một thư viện mã nguồn mở dành cho việc học máy và các tính toán khác trên dữ liệu phân tán. TFF đã được phát triển để hỗ trợ nghiên cứu mở và thử nghiệm về [Federated Learning](https://blog.research.google/2017/04/federated-learning-collaborative.html), một phương pháp trong học máy mà một mô hình chia sẻ tổng quát (shared global model) được huấn luyện trên nhiều máy khách tham gia, giữ dữ liệu huấn luyện của họ tại địa phương. 
+ Ví dụ: FL đã được sử dụng để huấn luyện các [mô hình dự đoán cho bàn phím di động](https://arxiv.org/abs/1811.03604) mà không cần tải lên máy chủ dữ liệu nhạy cảm về việc gõ phím của người dùng.

## Kiến trúc của TFF bao gồm 2 thành phần chính:
+ [Federated Learning](https://www.tensorflow.org/federated/federated_learning) (FL): là lớp ngoài cung cấp high-level interfaces để kết nối các mô hình học máy Keras hoặc non-Keras machine learning models hiện có vào trong TFF. Ta có thể thực hiện các công việc cơ bản như huấn luyện phân tán (federated learning) hoặc đánh giá (evaluation) mà không cần phải nghiên cứu chi tiết về các thuật toán học máy phân tán (federated learning algorithms).

+  [Federated Core](https://www.tensorflow.org/federated/federated_core) (FC): là lớp cung cấp low-level interfaces để implement một cách chính xác các thuật toán phân tán có thể tùy chỉnh, bằng cách kết hợp TensorFlow với các thao tác giao tiếp phân tán (distributed communication operators) trong một môi trường lập trình hàm có kiểu dữ liệu mạnh (strongly-typed). Lớp này cũng đóng vai trò là lõi để xây dựng TFF.

## Báo cáo sản phẩm môn Thực tập doanh nghiệp (2223H_INT4002_70):

+ Repo này là hướng dẫn Việt hóa cơ bản về cách cài đặt, ví dụ và sử dụng cơ bản các tính năng của thư viện TensorFlow Federated.

+ Cách hướng dẫn sẽ đi chính vào cách sử dụng các high-level interface (FL) cung cấp bởi TFF

## Các nguồn tài liệu tham khảo:

+ Mã nguồn chính thức của thư viện TFF của Tensorflow: [github](https://github.com/tensorflow/federated)

+ Mã nguồn áp dụng TFF nghiên cứu Federated Learning của Google: [github](https://github.com/google-research/federated)

+ Các video hướng dẫn về TFF: [video1](https://www.youtube.com/watch?v=yERlX7KmIao) | [video2](https://www.youtube.com/watch?v=JBNas6Yd30A&t=3818s)