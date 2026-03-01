
**Overview**

Built on top of [[Natural Language Processing]]

Classifying data / text as "positive", "negative", or "neutral". The overall feeling conveyed by a piece of text is known as polarity.

In the Financial domain, classification can be tricky because potential negative keywords and connotation may be viewed as positive:

"Company X cuts costs and lays off 10% of workforce" - could be viewed as "negative" by a sentiment model but may be viewed but market may see it as positive (a cost savings)

There is a need to use Domain-specific NLP models to properly categorization news articles.

**[[Financial Sentiment Models]]**:


### Challenges
- Lack of labeled news data
- Difficulty in mapping news publishing to time window for predictions. News doesn't come out on timed intervals but rather at "random"
- a general sentiment score may not be very useful for finance, especially for articles with multiple stocks listed. Fine grained sentiment needs to be conducted (See Aspect Based Sentiment Analysis)

### Methods

- [[Rule-Based Sentiment Analysis]]
- [[Machine Learning Sentiment Analysis]]

### Future Research

- **Entity-Level Sentiment (The "Noise" Problem):** Research Aspect-Based Sentiment Analysis (ABSA). How to extract sentiment specifically for a target ticker when the surrounding context is about a broader sector downturn.

- **Retail vs. Institutional Sentiment Disparity:** Investigate Sentiment Arbitrage and the lead-lag relationship. Does a spike in Reddit "hype" (Retail) precede or follow a change in institutional news sentiment?

- **The Temporal Decay of Sentiment:** Research Sentiment Half-life. Determine how many hours/days a "Highly Positive" news event remains a valid feature before it is "priced in" or stale.

- **Event-Specific Sentiment Weighting:** Explore Weighted Sentiment by Event Type. Compare the predictive power of sentiment regarding a "CEO Change" versus a "New Product Launch."

### Data sources
- Corporate Reports & Earnings Reports
- [[SEC Forms]]
- Financial News
- Reddit
- Twitter

Is there a way to categorize how much weight and noise from each source? Maybe a different model is used for various types?
