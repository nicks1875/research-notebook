
To train a robust **Sentiment Expert (Stage 2 Model)**, data curation must prioritize "High-Intensity" events where sentiment is the primary driver of price. 

## 1. Selection Strategy: The "Gold Standard" Basket
Training should focus on highly liquid, large-cap stocks (e.g., S&P 500) to ensure a clear causal link between information and price.

*   **Why Liquidity?** Immediate price reactions provide "Sharper Labels" for the model. High volume filters out individual "bad actors" and leaves the "Wisdom of the Crowd."
*   **The "Diverse 50" Approach:** Train on a basket of ~5 stocks from 10 different sectors (Tech, Finance, Healthcare, Energy, etc.).
    *   *Goal:* Prevent the model from learning "Ticker-Specific" quirks and instead learn "Universal Market Rules."

## 2. Identifying "Golden Windows"
Don't train on random dates. Use a statistical filter to find "Interesting Windows" where the price move was significantly higher than the daily noise.

### The "Interestingness" Score Checklist:
A high-quality training window typically satisfies multiple of these criteria:
1.  **High [[Abnormal Returns]] (AR):** The price move was $> |2\%|$ after stripping market/sector noise.
2.  **Unexpected Volume (Conviction):** Volume is $> 2.5x$ the 30-day average.
3.  **Bid-Ask Spread "Shock" (Urgency):** Sudden widening of the spread indicates market surprise.
4.  **Realized Volatility Spike (Disagreement):** Active trading and "churn" indicate the market is actively processing new info.

### The "Sentiment Recipe" Types:
| Type | Profile | Training Lesson |
| :--- | :--- | :--- |
| **Fundamental Shift** | High AR + High Volume + Low Reversion | Permanent change (SEC/News driven). |
| **Overreaction / Noise**| High AR + High Volume + High Reversion | Transitory "Pump & Dump" (Social driven). |
| **Institutional Drift** | High AR + Low Volume + Low Reversion | Subtle, long-term accumulation (SEC driven). |

## 3. Ground Truth Labeling (The Target)
The model should NOT be trained on raw price changes. It should be trained on **Idiosyncratic Alpha (Residual Return)**.

**Formula:** $AR = R_{stock} - (Beta 	imes R_{market}) - R_{sector}$
*   **Target Windows:** Create three distinct labels for the output vector:
    *   **Alpha_Short (1h):** Captures immediate Social/News "Hype."
    *   **Alpha_Medium (24h):** Captures "Daily Sentiment" impact.
    *   **Alpha_Long (7d):** Captures "Fundamental Drift."

## 4. Temporal Alignment (The Buffer)
Fetch data in "Windows of Influence" centered on the event ($T_0$):
*   **Standard/Earnings Window (48h):** $T_{-24h}$ (Anticipation) to $T_{+24h}$ (Digestion).
*   **Social/Hype Window (6h):** $T_{-1h}$ (Baseline) to $T_{+5h}$ (Reaction).
*   **Macro/Fundamental Window (14d):** $T_{-3d}$ to $T_{+11d}$ (Structural Revaluation).

## 5. Training the "BS Filter" (Uncertainty Learning)
To make the model "Anti-Fragile," specifically include "Bad" or "Misleading" events in the training set:
*   **The Reversion Lesson:** Train on social media spikes that immediately "snap back" to teach the model to lower **Confidence**.
*   **The Contradiction Lesson:** Train on days where Social is "Bullish" but SEC is "Bearish" to teach the model to prioritize **SEC Hooks**.
*   **The Staleness Lesson:** Train on "Old News" (high staleness) that has zero price impact to teach the model about **Sentiment Half-life**.
