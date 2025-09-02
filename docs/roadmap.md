# SanFortis‑RxAuth Roadmap

This document outlines planned enhancements and milestones for the
SanFortis‑RxAuth project.  Contributions and suggestions are welcome!  Feel
free to open an issue or pull request.

## Short term (0–3 months)

- [ ] **QR code decoding** – integrate a library like [`pyzbar`](https://pypi.org/project/pyzbar/) or [`opencv-python`](https://pypi.org/project/opencv-python/) to decode QR codes directly from images.  The decoded string should contain the serial number, manufacturer and expiry date in a standardised format.
- [ ] **Data store integration** – connect to a real supply chain ledger or blockchain API for authentic medicine records rather than relying on a static JSON file.
- [ ] **Packaging image analysis** – experiment with simple computer vision techniques to compare packaging features (e.g. colour histograms, logos, font sizes) against trusted templates.
- [ ] **CLI improvements** – add clearer output formatting, error handling and support for batch verification.

## Medium term (3–6 months)

- [ ] **Web UI** – build a lightweight web interface where users can upload a photo of a medicine package, decode the QR code and receive a verification result.
- [ ] **Mobile app prototype** – develop a cross‑platform mobile app (e.g. using React Native or Flutter) for on‑the‑go verification.
- [ ] **Community reporting** – add a mechanism for users to flag suspicious medicines and share anonymised data with regulators.
- [ ] **Multilingual support** – provide localised user interfaces and documentation in multiple languages.

## Long term (6+ months)

- [ ] **Regulatory compliance** – adapt the project to comply with specific regional regulations such as the EU Falsified Medicines Directive or the US Drug Supply Chain Security Act.
- [ ] **Machine learning models** – investigate the use of machine learning to detect subtle printing differences or micro‑defects in packaging that are hard to forge.
- [ ] **Expanded dataset** – work with pharmaceutical partners to access larger datasets of authentic and counterfeit packaging details for research.
