import time
import json



def stream_data(text):

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


def get_prompts_dict(json_path='configurations/prompt.json'):
    """
    Load the JSON file containing prompts and return a dictionary 
    where the keys are prompt names and the values are the prompt texts.
    
    Args:
        json_path (str): Path to the JSON file containing the prompts.
        
    Returns:
        dict: A dictionary with prompt names as keys and prompt texts as values.
    """
    # Load the JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Create a dictionary with names as keys and prompts as values
    prompts_dict = {item['name']: item['prompt'] for item in data['prompts']}
    
    return prompts_dict


def add_prompt_to_json(new_name, new_prompt, json_path='configurations/prompt.json'):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    if data['prompts']:
        new_id = max(item['id'] for item in data['prompts']) + 1
    else:
        new_id = 1
    
    new_entry = {
        "id": new_id,
        "name": new_name,
        "prompt": new_prompt
    }
    data['prompts'].append(new_entry)
    
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)