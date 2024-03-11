**UAVid: A Semantic Segmentation Dataset for UAV Imagery** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the drone inspection domain, and in the surveillance, traffic monitoring, and smart city industries. 

The dataset consists of 420 images with 43104 labeled objects belonging to 8 different classes including *tree*, *low vegetation*, *building*, and other: *road*, *static car*, *human*, *moving car*, and *background clutter*.

Images in the UAVid dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 150 (36% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *train* (200 images), *test* (150 images), and *val* (70 images). Additionally, every image contains the id of its video ***sequence*** (total 30). The dataset was released in 2020 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">University of Twente, Netherlands</span>, <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">Wuhan University, China</span>, and <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">Ohio State University, USA</span>.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/uavid/raw/main/visualizations/horizontal_grid.webm)
