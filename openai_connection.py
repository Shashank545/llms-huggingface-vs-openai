import os
import openai
openai.organization = "org-QsOUFZKIAN0b5QxWV9v4ca4T"
openai.api_key = "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"
results = openai.Model.list()
# print(results["data"][0])
# print(list(results.keys))
model_id_list = []
for res in results["data"]:
    print(res["id"])
    model_id_list.append(res["id"])
print(f"Number of supported models are : {len(model_id_list)}")
# print(model_id_list)
