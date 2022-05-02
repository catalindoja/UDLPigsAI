There should be a followed pattern of folders for the scripts to work well.

Images:
    train
    test

data:

this way the images folder will have both the images and the pascal VOC files in it.

This in turn is used by xml_to_csv.py to create the test_labels.csv and train_labels.csv.

Finally the generate_tfrecord.py will use both CSVs together with the images to create the tfrecords.