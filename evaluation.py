import json
import datasets


with open('coco_prefix_prediction.json', 'r') as f:
    prediction = json.load(f)

with open('evaluation_dataset.json', 'r') as f:
    ground_truth = json.load(f)

gold_references = []
model_predictions = []
for key in ground_truth:
    row = []
    for caption in ground_truth[key]:
        row.append(caption.split())
    gold_references.append(row)
    model_predictions.append(prediction[key].split())


metric = datasets.load_metric('bleu')


final_score = metric.compute(predictions=model_predictions, references=gold_references)
print(final_score)
# output final score to a file named evaluation.txt
with open('evaluation.txt', 'a') as f:
    f.write("\n\nScore for model:")
    f.write(str(final_score))
