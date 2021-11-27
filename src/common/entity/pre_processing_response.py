from typing import List

class PreProcessingResponse():
    X: List
    Y: List[List]
    Y_training: List[List]
    Y_test: List[List]
    lines_test: int
    lines_training: int
    lines_total: int
