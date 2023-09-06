**UAVid: A Semantic Segmentation Dataset for UAV Imagery** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the drone inspection domain, and in the surveillance, traffic monitoring, and smart city industries. 

The dataset consists of 420 images with 43104 labeled objects belonging to 8 different classes including *tree*, *low vegetation*, *building*, and other: *road*, *static car*, *human*, *moving car*, and *background clutter*.

Images in the UAVid dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 150 (36% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *test* (150 images), *train* (200 images), and *val* (70 images). Alternatively, images could be split into 30 video sequences: ***seq1***, ***seq2***, etc. The dataset was released in 2020 by the University of Twente, Netherlands, Wuhan University, China, and Ohio State University, USA.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/uavid/raw/main/visualizations/horizontal_grid.webm)
