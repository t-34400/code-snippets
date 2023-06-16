import matplotlib.pyplot as plt
from sklearn import tree

def export_metrics(model, output_test_filepath, output_graph_filepath, class_names, feature_names):
    importance_text = "Feature Importance:\n"
    importances = model.feature_importances_

    for i, importance in enumerate(importances):
        importance_text += f"{feature_names[i]}: {importance}\n"
    print(importance_text)

    oob_error = 1 - model.oob_score
    oob_text = f"OOB Error: {oob_error}"
    print(oob_text)

    plt.figure()
    plt.bar(feature_names, importances)
    plt.xlabel("Feature")
    plt.ylabel("Importance")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(output_graph_filepath)

    plt.figure()
    tree.plot_tree(model.estimators_[0], feature_names=feature_names, class_names=class_names, filled=True)
    plt.tight_layout()
    plt.show()


    with open(output_test_filepath, "w") as f:
        f.write(oob_text + "\n\n")
        f.write(importance_text)
