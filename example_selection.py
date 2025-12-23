import random

def calculate_f1(prediction, ground_truth):
    # Simplified F1 calculation logic
    return 0.85 # Placeholder

def example_selection_loop(candidate_pool, k=5):
    """
    Algorithm 1: Performance-oriented few-shot selection.
    """
    results = []
    
    # Step 1: Random Initialization
    for example in candidate_pool:
        # Step 2: Model Prediction (Mock LLM call) 
        # prediction = call_llm(example, prompt)
        
        # Step 3: Performance Evaluation (Calculate F1)
        score = calculate_f1(example['output'], example['ground_truth'])
        results.append({'example': example, 'f1': score})
    
    # Step 4: Optimized Selection (Rank and select top-k) 
    results.sort(key=lambda x: x['f1'], reverse=True)
    return [res['example'] for res in results[:k]]