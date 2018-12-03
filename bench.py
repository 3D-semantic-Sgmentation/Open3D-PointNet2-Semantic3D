import numpy as np
import multiprocessing
import time
import itertools

_map_label_to_color = [
    [255, 255, 255],  # white
    [0, 0, 255],  # blue
    [128, 0, 0],  # maroon
    [255, 0, 255],  # fuchisia
    [0, 128, 0],  # green
    [255, 0, 0],  # red
    [128, 0, 128],  # purple
    [0, 0, 128],  # navy
    [128, 128, 0],  # olive
]


def _label_index_to_color(label_index):
    global labels
    return _map_label_to_color[labels[label_index]]


def _labels_to_colors(labels):
    labels = np.array(labels).astype(np.int32)
    labels = list(labels)
    label_indexes = range(len(labels))
    with multiprocessing.Pool() as pool:
        colors = pool.map(_label_index_to_color, label_indexes)
    return np.array(colors).astype(np.int32)


labels = list(np.random.randint(0, 9, size=(5000000,), dtype=np.int32))

s = time.time()
colors = [_map_label_to_color[l] for l in labels]
colors = np.array(colors).astype(np.int32)
print("time to direct", time.time() - s, flush=True)

s = time.time()
colors_parallel = _labels_to_colors(labels)
print("time to map", time.time() - s, flush=True)

np.testing.assert_array_equal(colors, colors_parallel)
