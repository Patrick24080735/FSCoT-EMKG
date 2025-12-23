import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.mixture import GaussianMixture

def induce_relations(texts, n_components=11):
    """
    Step 1: Encode O&M knowledge using MiniLMv2.
    Step 2: Assign embeddings to Gaussian distributions using GMM.
    """
    # Load pre-trained MiniLMv2 model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings
    embeddings = model.encode(texts)
    
    # Fit Gaussian Mixture Model
    gmm = GaussianMixture(n_components=n_components, random_state=42)
    gmm.fit(embeddings)
    
    # Get cluster labels
    labels = gmm.predict(embeddings)
    return labels, gmm

# Example usage:
# o_m_texts = ["Battery failure leads to engine halt", "Tire pressure low..."]
# clusters, model = induce_relations(o_m_texts)