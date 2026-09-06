"""
Demonstration of genpark-lost-in-the-middle-context-reordering-skill
"""

from client import LostInMiddleReordererClient

def main():
    reorderer = LostInMiddleReordererClient()

    raw_docs = [
        {"id": "doc_1", "score": 0.95, "title": "Critical Primary Evidence"},
        {"id": "doc_2", "score": 0.90, "title": "Secondary Strong Evidence"},
        {"id": "doc_3", "score": 0.85, "title": "Supporting Fact A"},
        {"id": "doc_4", "score": 0.80, "title": "Supporting Fact B"},
        {"id": "doc_5", "score": 0.75, "title": "Marginal Evidence C"}
    ]

    optimized = reorderer.reorder_documents(raw_docs)

    print("=== REORDERED U-CURVE ATTENTION PASSAGES ===")
    for idx, d in enumerate(optimized):
        pos = "HEAD" if idx == 0 else ("TAIL" if idx == len(optimized) - 1 else f"POS_{idx}")
        print(f"[{pos}] ID: {d['id']} | Score: {d['score']} | {d['title']}")

if __name__ == "__main__":
    main()
