# Constant-velocity null-intercept benchmark (19 November 2026)

Three independent diagnostics: (1) solve the Minkowski null-intercept equation |r+v t|=c t for a receiver with constant 3-velocity; (2) compute the emission point-ahead unit vector and its angular separation from the instantaneous line of sight; (3) compute a central finite-difference sensitivity of light time to each initial position coordinate.

Run from the repository root: `python -m pytest -q research_tools/tests/test_endpoint_audit_20261119.py`.

Units are metres, metres per second and seconds. This is a flat-spacetime, inertial, one-way benchmark with a stationary emitter and a receiver moving at constant subluminal velocity. It does **not** include Earth rotation, gravitational delay, Gaia/JPL ephemerides, acceleration, time standards, covariance, pointing errors or round-trip acquisition. Numerical gradients depend on finite-difference step and are not propagated uncertainty intervals. No FTL communication or new astrometric measurement is implied. Related to issues #2 and #5 but does not complete their acceptance criteria.

Research lead and requested Git author: Biswajit Jana. Python implementation developed with AI coding assistance and requires independent scientific review.
