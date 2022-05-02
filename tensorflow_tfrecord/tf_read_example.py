import tensorflow as tf
raw_dataset = tf.data.TFRecordDataset("data/train.record")

for raw_record in raw_dataset.take(1):
    example = tf.train.Example()
    example.ParseFromString(raw_record.numpy())
    print(example)