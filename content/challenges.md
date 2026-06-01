# Benchmark Challenge: Visual Traffic Sign Mapping

To ground the workshop's research themes in a concrete shared task, we organize a three-track benchmark challenge. The challenge progressively moves from perception to localization to map integration, mirroring the real-world pipeline of reading visual observations into map knowledge. Participants may enter one, two, or all three tracks.

## Track 1: Traffic Sign Segmentation & Tracking
- icon: fa-crosshairs
- description: Given sequences of street-level images, detect, segment, and track all traffic signs across frames. Evaluates instance segmentation quality and temporal consistency under occlusion, motion blur, and varying illumination.
- metrics: MOTA, IDF1, Mask IoU
- prize_1st: TBD
- prize_2nd: TBD
- prize_3rd: TBD

## Track 2: Sign Localization in Geographic Coordinates
- icon: fa-map-pin
- description: Given image sequences and tracklets from Track 1 (or provided as ground-truth input), estimate the latitude and longitude of each tracked sign. Bridges computer vision and geospatial reasoning via camera geometry, GPS/IMU data, and structure-from-motion.
- metrics: Median localization error (meters), Recall at distance thresholds
- prize_1st: TBD
- prize_2nd: TBD
- prize_3rd: TBD

## Track 3: Sign-to-Map Association (Digitization)
- icon: fa-project-diagram
- description: Given localized sign tracklets, existing map data (OpenStreetMap road graph), and aerial/satellite imagery, associate each sign with the correct map element (road segment, intersection, or lane) it governs. This is the core association problem requiring spatial reasoning, graph matching, and multi-modal fusion.
- metrics: Association Precision, Recall, F1 at map-element level
- prize_1st: TBD
- prize_2nd: TBD
- prize_3rd: TBD

## Timeline
- T−8 weeks: Challenge announcement and dataset release (training + validation sets)
- T−6 weeks: Baseline code and evaluation server released
- T−2 weeks: Test set released (no ground truth)
- T−1 week: Submission deadline for predictions and 2-page technical reports
- Workshop day: Results announced; top-3 teams per track present methods (5 min each)

## Note
All winning teams will be invited to present during the Challenge Results session. Top-scoring technical reports will be considered for contributed oral presentation slots. We are exploring additional industry sponsorship for travel grants.
