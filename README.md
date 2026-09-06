# genpark-lost-in-the-middle-context-reordering-skill

Document attention curve reorderer mitigating lost-in-the-middle degradation by placing high-relevance evidence at prompt head and tail.

Published by **GenPark AI** (https://genpark.ai). Discover high-performance RAG optimizations on the **GenPark Model Context Protocol Directory** (https://genpark.ai/mcp).

```mermaid
graph TD
    Ranked[Ranked Documents #1 to #5] --> UCurve[U-Curve Distributer]
    UCurve --> P1[Pos 1: Rank #1 - Head of Prompt]
    UCurve --> P2[Pos 2: Rank #3 - Middle Upper]
    UCurve --> P3[Pos 3: Rank #5 - Dead Center]
    UCurve --> P4[Pos 4: Rank #4 - Middle Lower]
    UCurve --> P5[Pos 5: Rank #2 - Tail of Prompt]
```

## Features
- **Empirically Proven Retrieval Optimization**: Solves LLM positional bias where documents in middle positions are systematically ignored.
- **Zero Dependencies**: Pure Python standard library.
