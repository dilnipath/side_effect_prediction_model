import ast


generalized = {
    (
     "worsening pain in a place you injected this medication",
     "pain at the application site",
     "pain in the mouth in the area where you placed this medication"): "pain where the medication was applied",

    (
     "skin redness where this medication was applied",
     "redness at the place where the injection was given"): "redness where the medication was applied",
}
labels_ordered = open("./create_multilabel_dataset/label_order_full.txt").read()
labels_ordered = ast.literal_eval(labels_ordered)

for lst in generalized.keys():
    for side_effect in lst:
        print(side_effect)
        labels_ordered.remove(side_effect)
    labels_ordered.append(generalized[lst])
    
print(labels_ordered)
print(len(labels_ordered))

with open('./create_multilabel_dataset/label_order_full.txt', 'w', encoding="utf-8") as f:
    for item in labels_ordered:
        f.write(f'"{item}",')

