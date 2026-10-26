# Writing and visual conventions

Research notes in this repository should read like laboratory papers, not marketing decks. Use **Abstract**, **Problem**, **Model**, **Experiment**, **Results**, **Discussion**, **Limitations** and **References** when those headings fit the study. Drop the generic “Executive summary”, “Key takeaways”, promotional adjectives and inflated significance claims.

Include equations, SI units, assumptions, statistical intervals, negative results, links to source data, and a reproducibility command. Distinguish simulations from measurements, valid code from independently verified physical models, and past shared predictions from actually received new information. Avoid long ornamental prose and repetitive “not just X but Y” constructions.

For the research viewer, prefer a restrained type hierarchy, readable diagrams, purposeful transitions, keyboard navigation, reduced-motion support, and controls that select actual computed results. The current [Motion](https://motion.dev) library is a possible *future* React implementation dependency; it is not necessary for a portable offline viewer. Framer, 21st.dev and UI/UX Pro Max are visual references, not sources to copy without checking licensing.

References supplied by the researcher:
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (style guidance, not a reliable detector of provenance)
- [Motion](https://motion.dev/)
- [Framer Motion background](https://www.framer.com/dictionary/framer-motion)
- [Framer motion components](https://www.framer.com/community/marketplace/components/tags/motion/)
- [UI/UX Pro Max skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [21st.dev](https://21st.dev/)

No code, instrument or experimental result may be called flight-qualified without independent validation.
## Equation and reference rendering checks

- In GitHub Markdown, use dollar-delimited inline mathematics and double-dollar block mathematics. GitHub renders these with MathJax. Do not leave raw escaped bracket expressions in reader-facing reports.
- In browser HTML pages, use native MathML or a self-contained checked renderer; offline pages must still display equations.
- Strip unresolvable chat citation tokens from reader-facing editions. Preserve archival provenance and say clearly which sources await verification; do not invent replacement citations.
- Every numerical interactive control must change a real reproducible calculation or explicitly inspect a frozen dataset. Mark idealised conditions and timing; no imitation 'live telemetry' where none exists.
- Test default browser layout with JavaScript disabled, at mobile width, and with reduced-motion settings. Avoid hiding primary text behind animation until a script runs.

Design references supplied for exploration: [Motion](https://motion.dev/), [Framer motion](https://www.framer.com/dictionary/framer-motion), [motion components](https://www.framer.com/community/marketplace/components/tags/motion/), [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [21st.dev](https://21st.dev/). These are visual references, not dependencies or permission to copy protected components.

[Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) is an editorial prompt to avoid generic phrasing, not a detector of who wrote a passage. Maintain transparent scientific attribution and factual provenance.
