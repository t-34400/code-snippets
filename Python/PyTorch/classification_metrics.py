import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def plot_confusion_matrix_with_metrics(classes, target_labels, output_labels):
    num_classes = len(classes)

    cm = confusion_matrix(target_labels, output_labels)
    accuracy = accuracy_score(target_labels, output_labels)
    precision = precision_score(target_labels, output_labels, average="macro")
    recall = recall_score(target_labels, output_labels, average="macro")
    f1 = f1_score(target_labels, output_labels, average="macro")

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    _, ax = plt.subplots()
    ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)

    for i in range(num_classes):
        for j in range(num_classes):
            text = ax.text(j, i, cm[i, j], ha="center", va="center", color="black")

    ax.set_xticks(np.arange(num_classes))
    ax.set_yticks(np.arange(num_classes))
    ax.set_xticklabels(classes)
    ax.set_yticklabels(classes)

    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")

    ax.set_title("Confusion Matrix")

    plt.show()


if __name__ == "__main__":
    # test
    classes = ["Class A", "Class B", "Class C"]
    target_labels = ["Class A", "Class B", "Class C", "Class C"]
    output_labels = ["Class A", "Class B", "Class B", "Class B"]
    plot_confusion_matrix_with_metrics("", target_labels, output_labels)
