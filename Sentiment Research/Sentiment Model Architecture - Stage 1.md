

 Feed three three models in parallel using different methods. Output a standardized vector that is the same for each. An initial proposed vector output is:

| Index | Category    | Example Value      | Interpretation                                                                                                                                                                                                                                  |
| ----- | ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | Positive    | 0.1                | Probability the text is positive                                                                                                                                                                                                                |
| 1     | Negative    | 0.85               | Probability the text is negative                                                                                                                                                                                                                |
| 2     | Neutral     | 0.05               | Probability the text is neutral                                                                                                                                                                                                                 |
| 3     | Confidence  | 0.92               | Models internal certainty about the predicted sentiment label (what the model thinks about a text source after reading)                                                                                                                         |
| 4     | Reliability | 0.99 / 0.15 / 0.85 | Static weight of how much to trust each sentiment source (what the model thinks about a text source before reading). SEC Filings would have highest reliability, followed by news, and then social media having a relatively low "trust" value. |

   * Model 1: The "Signal" (SEC Filings, Earnings Transcripts)
       * Characteristics: High density, low frequency, legally binding.
       * Processing: Use LLMs (like GPT-4 or Llama-3) to extract specific sections like Risk Factors or MD&A. Don't just score sentiment; extract "Sentiment Shifts" (e.g., "Management is more cautious about debt than last quarter").
       * Weight: Primary driver for long-term (weeks/months) price targets.


   * Model 2: The "Context" (Financial News, Reuters, Bloomberg)
       * Characteristics: High frequency, professional, often redundant.
       * Processing: Use FinBERT for standardized sentiment scoring. Use Aspect-Based Sentiment Analysis (ABSA) to ensure a general "market crash" headline isn't unfairly penalizing a specific ticker that is actually showing strength.
       * Weight: Secondary driver; confirms or contradicts the "Signal."


   * Model 3: The "Noise" (Twitter, Reddit)
       * Characteristics: Extremely high frequency, high noise, reflects "Retail Impulse."
       * Processing: Use specialized models (like VADER or RoBERTa-Social) that understand emojis, slang, and sarcasm. Focus on Volume Volatility (sudden spikes in mentions) rather than  individual post sentiment.
       * Weight: Tertiary; best for predicting short-term (minutes/hours) volatility and "hype cycles."

#### Advantages
- Models with standardized output are "hot-swappable". Creating a better model for parsing public reddit posts / twitter can be plugged in or a better model parsing 10-k filings be swapped in.

- Uniformity in inputs for Stage 2 model - master model taking in stage 1 inputs doesn't need to deal with individual sources, it only needs to understand the standard vector produced by first stage models

- Allows master model to discern between which inputs from which stage 1 model are more important: "The SEC model says -0.80 (Negative), but the Twitter model says +0.95 (Positive). Which one is more reliable right now?"

