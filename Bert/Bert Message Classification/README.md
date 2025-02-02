# Email Classification using BERT

This project demonstrates how to classify emails as spam or ham using the BERT (Bidirectional Encoder Representations from Transformers) model. The model is trained on a dataset of labeled emails and can predict whether a given email is spam or ham.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Evaluation](#evaluation)
- [Prediction](#prediction)
- [Example](#example)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- PyTorch
- Transformers library from Hugging Face
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/email-classification.git
   cd email-classification
   ```

2. Install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your dataset (`spam.csv`) in the project directory.
2. Run the `classification.ipynb` Jupyter notebook to train the model and make predictions.

## Training

The training process involves the following steps:

1. **Load the dataset**: The dataset is loaded from `spam.csv` and preprocessed. The dataset contains two columns: 'Category' and 'Message'. The 'Category' column is renamed to 'label' and the 'Message' column is renamed to 'text'. The labels are then mapped to binary values (`ham` -> 0, `spam` -> 1).
2. **Split the dataset**: The dataset is split into training and validation sets using an 80-20 split. This means 80% of the data is used for training and 20% is used for validation.
3. **Tokenize the data**: The text data is tokenized using the BERT tokenizer. Tokenization is the process of converting text into a format that the BERT model can understand. The tokenizer truncates the text to a maximum length of 128 tokens and pads shorter texts to ensure all inputs have the same length.
4. **Create a custom dataset**: A custom dataset class `EmailDataset` is created to handle the tokenized data. This class inherits from PyTorch's `Dataset` class and overrides the `__getitem__` and `__len__` methods to return individual data samples and the length of the dataset, respectively.
5. **Load pre-trained BERT model**: The pre-trained BERT model is loaded with a classification head using the `BertForSequenceClassification` class from the Transformers library. The classification head is configured to output 2 classes (spam and ham).
6. **Define DataLoader**: DataLoaders are defined for the training and validation datasets. DataLoaders are used to load data in batches during training and validation. The training DataLoader shuffles the data to ensure randomness, while the validation DataLoader does not shuffle the data.
7. **Define optimizer**: The AdamW optimizer is defined to update the model's parameters during training. AdamW is an optimization algorithm that combines the benefits of Adam and weight decay.
8. **Training loop**: The model is trained for a specified number of epochs (3 in this case). During each epoch, the model processes the training data in batches. For each batch, the optimizer gradients are zeroed, the inputs and labels are moved to the appropriate device (GPU or CPU), and the model's outputs are computed. The loss is then backpropagated, and the optimizer updates the model's parameters.
9. **Evaluation**: The model is evaluated on the validation set after each epoch. The model's performance is evaluated using accuracy, which is the ratio of correctly predicted labels to the total number of labels. The accuracy is printed after each epoch.

## Evaluation

The model's performance is evaluated using accuracy on the validation set. The accuracy is calculated as the ratio of correctly predicted labels to the total number of labels in the validation set. The accuracy is printed after each epoch to monitor the model's performance during training.

## Prediction

The `predict_single_text` function can be used to predict whether a single email is spam or ham. This function takes an email text, the trained model, the tokenizer, and the device (GPU/CPU) as inputs and returns the prediction. Here's how it works:

1. **Tokenize the input text**: The input text is tokenized using the BERT tokenizer. The tokenizer truncates the text to a maximum length of 128 tokens and pads shorter texts to ensure all inputs have the same length.
2. **Move inputs to the device**: The tokenized inputs are moved to the appropriate device (GPU or CPU) using the `.to(device)` method.
3. **Set the model to evaluation mode**: The model is set to evaluation mode using the `.eval()` method. This ensures that the model behaves correctly during inference.
4. **Disable gradient calculation**: Gradient calculation is disabled using the `torch.no_grad()` context manager. This is necessary because we are not training the model, so we do not need to compute gradients.
5. **Forward pass**: The model's forward pass is performed using the tokenized inputs. The model outputs logits, which are the raw predictions before applying the softmax function.
6. **Get the predicted class**: The predicted class is obtained by taking the argmax of the logits along the dimension 1. The predicted class is then mapped to "spam" or "ham" based on whether the predicted class is 1 or 0, respectively.

## Example

```python
# Example usage
email_text = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize."
prediction = predict_single_text(email_text, model, tokenizer, device)
print(f"Prediction: {prediction}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
