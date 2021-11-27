from typing import List
from src.common.contract.application.encoder_contract import EncoderContract
from sklearn.preprocessing import LabelEncoder

class Encoder(EncoderContract):

    @staticmethod
    def encode(x: List[List], columns: List[int]) -> List[List]:
        
        for column in columns:
            label_encoder = LabelEncoder()
            x[:, column] = label_encoder.fit_transform(x[:, column])
        
        return x
