import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.feature_extraction.text import CountVectorizer

class SimplePatternRecognizer(nn.Module):
    def __init__(self, input_size):
        super(SimplePatternRecognizer, self).__init__()
        self.fc = nn.Linear(input_size, 2)  # 2 sınıf (Örüntü var / yok)

    def forward(self, x):
        return self.fc(x)

def detect_pattern(text):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([text]).toarray()

    model = SimplePatternRecognizer(input_size=X.shape[1])
    model.eval()

    with torch.no_grad():
        output = model(torch.tensor(X, dtype=torch.float32))
    
    return "Örüntü tespit edildi!" if torch.argmax(output) == 1 else "Örüntü bulunamadı."
