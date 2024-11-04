import os
import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

################ function to run the model
def run_model(context, query, **generator_args):
    input_ids = tokenizer.encode(context + "<sep>" + query, return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    return output

################ model and tokenizer
model_name_or_path = "persiannlp/mt5-small-parsinlu-sentiment-analysis"
tokenizer = MT5Tokenizer.from_pretrained(model_name_or_path)
model = MT5ForConditionalGeneration.from_pretrained(model_name_or_path)

################ dataset directory
dataset_dir = "./playwright_venv/drpezeshkian/1850279442444333246"
output_file = os.path.join(dataset_dir, "inference_result.txt")

################ inference process
#### twitt text as query
with open(os.path.join(dataset_dir, "1.txt"), "r", encoding="utf-8") as f:
    query = f.read().strip()
print("query:")
print(query)

#### comments of the post as context
with open(output_file, "w", encoding="utf-8") as out_f:
    
    out_f.write("Query for the model: (the tweet post text)\n")
    out_f.write(query + "\n\n") # write the query at the beginning of the file

    
    for i in range(2, len(os.listdir(dataset_dir)) + 1): # iterate through all comment and get the model response on them
        file_path = os.path.join(dataset_dir, f"{i}.txt")
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                context = f.read().strip()
            
            result = run_model(context, query) # feed the query and each context to the model

            print(f"Context from {i}.txt:")
            print(context)
            print("result of the model inference:")
            print(result[0])
            print("---------------------------------------------")
            
            out_f.write(f"Context from {i}.txt:\n{context}\n") # write context and result to the output file
            out_f.write("Result:\n" + result[0] + "\n")
            out_f.write("------------------------------------------------------------\n")
