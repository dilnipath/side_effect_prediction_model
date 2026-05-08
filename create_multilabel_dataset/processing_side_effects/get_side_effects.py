import ast

labels_ordered = open("./create_multilabel_dataset/label_order_full.txt").read()
labels_ordered = ast.literal_eval(labels_ordered)

for label in labels_ordered:
    if "blue" in label:
        print(f'"{label}",')