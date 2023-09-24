# Get labels
def get_labels(label_path):
    
    with open(label_path) as f:
        return json.load(f)
