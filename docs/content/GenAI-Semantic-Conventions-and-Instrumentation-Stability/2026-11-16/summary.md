## Key Topics
- **isNested attribute on duration metric:** Max questioned its value and proposed parking it; Liudmila argued HTTP duration can't replace GenAI-specific duration, and adding an attribute later is breaking, so it blocks stabilization. Max will propose naming options by Wednesday.
- **Issue 703 (end-to-end token usage):** Max proposed a roll-up counter recorded per agent in the lineage at each inference, instead of stamping the main agent name on all metrics. This reduces cardinality and avoids the ambiguity of which "main agent name" to use (ADK, A2A, Agent Runtime).
- **Main agent name trade-offs:** Discussion of whether a main agent attribute or resource/entity attribute is better; Google's Gemini Enterprise has many root agents, complicating cardinality. Liudmila suggested both directions may be compatible. Max will draft a proposal.
- **PR reviews (JSON schema and attribute structure):** Aaron's PR is nearly ready; a separate PR will address None vs. missing handling. Felix questioned a change that merged two attributes into one with subfields, and the group will follow up.

## Action Items
- Max Ind: Prepare naming proposal for the isNested attribute by Wednesday.
- Max Ind: Draft a proposal for the roll-up token usage metric (issue 703) and share cardinality numbers offline.
- Aaron Abbott: Touch up the current PR based on review feedback.
- Aaron Abbott: Reply to Felix about the single-attribute-with-subfields design.
- Liudmila Molkova: Review the current PR again and consider approving with minor changes.
- Liudmila Molkova / Aaron Abbott: Open a separate PR to unify None vs. missing handling in the JSON schema.

## Participants
Mikolaj Knap, Max Ind, Liudmila Molkova, Aaron Abbott, Erin
