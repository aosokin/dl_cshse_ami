import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


CELL_LENGTH = 4
IMAGE_HEIGHT, IMAGE_WIDTH = 2 * CELL_LENGTH + 5, CELL_LENGTH + 4


def vertical_stroke(rightness, downness):
    """
    Return a 2d numpy array representing an image with a single vertical stroke in it.
    `rightness` and `downness` are values from [0, 1] and define the position of the vertical stroke.
    """
    i = (downness * (CELL_LENGTH + 1)) + 2
    j = rightness * (CELL_LENGTH + 1) + 1
    x = np.zeros(shape=(IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.float64)
    x[i + np.arange(CELL_LENGTH), j] = 1.
    return x

def horizontal_stroke(downness):
    """
    Analogue to vertical_stroke, but it returns horizontal strokes.
    `downness` is here a value in [0, 1, 2].
    """
    i = (downness * (CELL_LENGTH + 1)) + 1
    x = np.zeros(shape=(IMAGE_HEIGHT, IMAGE_WIDTH), dtype=np.float64)
    x[i, 2 + np.arange(CELL_LENGTH)] = 1.
    return x


BASE_STROKES = np.asarray(
    [horizontal_stroke(k) for k in range(3)] + 
    [vertical_stroke(k, l) for k in range(2) for l in range(2)])

DIGITS_STROKES = np.array([
    [0, 2, 3, 4, 5, 6], 
    [5, 6], 
    [0, 1, 2, 4, 5], 
    [0, 1, 2, 5, 6], 
    [1, 3, 5, 6], 
    [0, 1, 2, 3, 6], 
    [0, 1, 2, 3, 4, 6], 
    [0, 5, 6], 
    np.arange(7), 
    [0, 1, 2, 3, 5, 6]
])


def random_digits(strokes=BASE_STROKES, digit_as_strokes=DIGITS_STROKES, fixed_label=None):
    label = fixed_label if fixed_label is not None else np.random.choice(len(digit_as_strokes))
    combined_strokes = strokes[digit_as_strokes[label], :, :].sum(axis=0)
    return combined_strokes, label


class LcdDigits(Dataset):
    def __init__(self, n_examples):
        digits, labels = zip(*[random_digits() for _ in range(n_examples)])
        self.digits = np.asarray(digits, dtype=np.float64)
        self.labels = np.asarray(labels)
    
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, idx):
        digit_with_channel = self.digits[idx][np.newaxis, :, :]
        
        return torch.from_numpy(digit_with_channel).float(), torch.from_numpy(np.array([self.labels[idx]]))

