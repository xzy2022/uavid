The authors of the **UAVid: A Semantic Segmentation Dataset for UAV Imagery** dataset discussed the significance of semantic segmentation, a crucial aspect of visual scene understanding, with applications in fields such as robotics and autonomous driving. They noted that the success of semantic segmentation owes much to large-scale datasets, particularly for deep learning methods. While several datasets existed for semantic segmentation in complex urban scenes, capturing side views of objects from mounted cameras on driving cars, there was a dearth of datasets capturing urban scenes from an oblique Unmanned Aerial Vehicle (UAV) perspective. Such oblique views provide both top and side views of objects, offering richer information for object recognition. To address this gap, the authors introduced the UAVid dataset, which presented new challenges, including variations in scale, moving object recognition, and maintaining temporal consistency.

The UAVid dataset comprised 30 video sequences capturing high-resolution images from oblique UAV perspectives. A total of 300 images were densely labeled with annotations for eight semantic classes. The authors also provided several deep learning baseline methods with pre-training.

They considered various factors when creating the dataset, including the oblique view from the UAV platform, high resolution, consecutive labeling, complex and dynamic scenes, data variation across 30 different places, and the use of modern lightweight drones for data collection.

The authors highlighted the higher scene complexity of the UAVid dataset compared to existing UAV semantic segmentation datasets, particularly in terms of the number of objects and object configurations. They noted that their dataset was moderately sized but had a comparable or larger number of labeled pixels compared to well-known semantic segmentation datasets.

They defined eight semantic classes for the dataset:

1. *building*: living houses, garages, skyscrapers, security booths, and
   buildings under construction. Freestanding walls and fences are not
   included.
2. *road*: road or bridge surface that cars can run on legally. Parking
   lots are not included.
3. *tree*: tall trees that have canopies and main trunks.
4. *low vegetation*: grass, bushes and shrubs.
5. *static car*: cars that are not moving, including static buses, trucks,
   automobiles, and tractors. Bicycles and motorcycles are not included.
6. *moving car*: cars that are moving, including moving buses, trucks,
   automobiles, and tractors. Bicycles and motorcycles are not included.
7. *human*: pedestrians, bikers, and all other humans occupied by different activities.
8. *clutter*: all objects not belonging to any of the classes above.

The car class was deliberately divided into moving car and static car. Moving car is such a special class designed for moving object segmentation. Other classes can be inferred from their appearance and context, while the moving car class may need additional temporal information in order to be appropriately separated from static car class. Achieving high accuracy for both static and moving car classes is one possible research goal for the dataset.

The authors described their annotation methodology, which included pixel-level, super-pixel level, and polygon-level annotation methods. These methods allowed annotators to efficiently label objects with different characteristics, such as trees with sawtooth boundaries and buildings with straight boundaries. The labeling tool also provided video play functionality for annotators to inspect object motion.

Lastly, they detailed the dataset splits, dividing the 30 video sequences into training, validation, and test splits. The data was split at the sequence level, ensuring that each split represented the scene variability adequately. The test split contained withheld labels for benchmarking purposes, while the training and validation splits were made publicly available, comprising a total of 200 labeled images. The size ratios among the splits were maintained at 3:1:2 (training:validation:test).
