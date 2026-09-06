"""
Attention Curve Reordering to Eliminate Lost-in-the-Middle Degradation.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any

class LostInMiddleReordererClient:
    """
    Reorders ranked retrieval passages into a U-shaped attention distribution:
    - Highest ranked document goes to prompt beginning (head)
    - Second highest goes to prompt end (tail)
    - Lower ranked documents populate middle regions where attention fades
    """

    def reorder_documents(self, documents: List[Dict[str, Any]], score_key: str = "score") -> List[Dict[str, Any]]:
        """
        Takes list of documents with similarity scores and returns reordered list
        following U-curve attention optimization (Liu et al., 2023).
        """
        if len(documents) <= 2:
            return list(documents)

        # Sort strictly descending by relevance score
        sorted_docs = sorted(documents, key=lambda d: d.get(score_key, 0.0), reverse=True)

        reordered = [None] * len(sorted_docs)
        head_idx = 0
        tail_idx = len(sorted_docs) - 1

        for i, doc in enumerate(sorted_docs):
            if i % 2 == 0:
                reordered[head_idx] = doc
                head_idx += 1
            else:
                reordered[tail_idx] = doc
                tail_idx -= 1

        return reordered
