
Proposed second stage is to feed the sentiment from each respective model output into an Aggregation Layer to align the time ranges on different text sources

This handles the issue that each text source has a different frequency (SEC filings once per year / once per quarter, while news and social media text will be throughout the day at unpredictable and aligned times

Example: If 500 tweets come in between 2:00 PM and 2:05 PM,  a rule must "squash" those 500 vectors into a single representative vector for that 5-minute window before the final model sees it. Without this, the final model will be overwhelmed by social media and "starved" for SEC data.