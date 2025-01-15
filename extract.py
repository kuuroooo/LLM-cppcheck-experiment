import json
import os

input_file = "primevul_train.jsonl" 
output_dir = "extracted_c_snippets"

os.makedirs(output_dir, exist_ok=True)

with open(input_file, "r") as infile:
    for i, line in enumerate(infile):
        if i < -1 or i > 20:  
            continue
        record = json.loads(line)
        func_code = record.get("func")
        if func_code:
            output_path = os.path.join(output_dir, f"snippet_{i}.c")
            with open(output_path, "w") as outfile:
                outfile.write(func_code)
            print(f"Snippet {i} saved to {output_path}")
print(f"Snippets saved in {output_dir}/")
