# Research website: interface and reproducibility record

Research lead: Biswajit Jana | October 2026

The research website must communicate the physical question, the difference between modelled and built apparatus, the reproducible numerical results, and explicit falsification criteria. It is a research record rather than a product announcement.

## Visual system

- Dark astronomical background, ice blue/cyan for validated calculation and warm amber for assumptions.
- Raster PNG figures for the landing page; text, equations and sources remain in accessible HTML.
- A visual is an illustration unless backed by a simulation or a measured instrument record. Do not label conceptual astronomy images as actual observations.
- Responsive navigation, reduced-motion support, keyboard focus and restrained scroll reveals.
- Static HTML, CSS and JavaScript. No runtime CDN, build service or API key required for readers.

The implementation follows design principles from [Motion](https://motion.dev/docs/react-scroll-animations), [Framer](https://www.framer.com/dictionary/framer-motion), [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), and [21st.dev](https://21st.dev/). These are design references. The site does not import those services, copy third-party components or require their JavaScript packages.

## Pages and reproducible sources

1. The observatory landing page explains the question, electronic and optical chain and live idealized photon-counting model.
2. The technical report documents light-time, active optics, pointing, Poisson/Pulse-position modulation, quantum no-signalling and hypothetical GR models.
3. A historical archive preserves the original Beyond the Light Cone work and explicitly flags unresolved chat citations.
4. The linked GitHub source and automated checks are the scientific audit trail.

The dynamic simulator exports its parameter state and seeded synthetic output as JSON. Neither webpage accesses live detectors nor are interactive controls actual spacecraft commands.

## Verification and limitations

Automated website checks validate local page links, original PNG headers and JavaScript syntax. They do not replace visual checks on mobile browsers, colour-contrast assessment, screen-reader testing or source-level review of physics.

The newer browser report is a report in website form. Keep native text accessible, test every math expression, preserve primary bibliographic sources, and avoid generic executive summaries or claims unsupported by experiments.

**Long-term requirement:** Future hardware papers should include pin-level drawings, qualified parts lists, interface-control documents, calibration timestamps, detector data and independently repeatable results. Current illustrations and electrical blocks are not fabricated circuits.
