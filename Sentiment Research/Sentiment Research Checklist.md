

This note tracks the technical and theoretical research required of the sentiment portion of the stock prediction modeling

## 1. Data Curation & Pre-Processing (Immediate TODOs)
- [ ] **Develop the "Interest Filter" Script:** Use `yfinance` to identify "Golden Windows" (High Abnormal Return + High Volume) for a basket of 50 S&P 500 stocks (5 different stocks from 10 sectors)
- [ ] **Implementation of "Aggregation Layer":** Design the logic for "squashing" high-frequency social media sentiment into 5-minute time-step vectors (Mean vs. Sum vs. Exponentially Weighted).
- [ ] **Historical "Noise" Dataset:** Curate a specific set of "Fake News" or "Overreaction" events (e.g., social media rumors that were later debunked) to train the model's **Confidence** and **Divergence** metrics.

## 2. Model Architecture & Training (Medium-Term)
- [ ] **The "BS Filter" (Uncertainty Learning):** Research techniques for training the model to output **Aleatoric Uncertainty** (identifying when the input data is intrinsically noisy or contradictory).
- [ ] **Multi-Horizon Alpha Optimization:** Experiment with the optimal "Look-ahead" windows for Short-term (1h), Medium-term (24h), and Long-term (7d) Alpha predictions.
- [ ] **Latent Embedding Visualization:** Research tools (like UMAP or t-SNE) to visualize the 16-dimension **Context (Indices 2-17)** vector. Can we see "Islands" of market regimes (Bull vs. Bear)?
- [ ] **Dynamic Attention (The Hooks):** Research the most effective "Gating Mechanisms" to allow the model to automatically prioritize SEC filings over Social Media during earnings weeks.

## 3. Theoretical Research Topics
- **[[Abnormal Returns]] Fine-tuning:** Investigate more complex "Factor Models" (Fama-French) to better isolate the "Sentiment Residual" from market and size factors.
- **Sentiment Half-life (Temporal Decay):** Quantify the exact decay rates ($\lambda$) for different sources. Does a tweet decay faster in a "High Volatility" regime than a "Low Volatility" one?
- **Cross-Sector Sentiment Transfer:** Measure the "Loss of Accuracy" when a model trained purely on Big Tech is applied to Healthcare or Energy. Is a universal sentiment model possible, or are sector-specific models mandatory?
- **Entity-Level Sentiment (ABSA):** Research how to extract sentiment for a target ticker when the surrounding text is about a sector-wide downturn (e.g., "Apple is doing well, but the Smartphone market is shrinking").

## 4. Systems Integration
- [ ] **MCP AI Agent Interface:** Design the "Translation Layer" that turns the **Hooks** and **Divergence** scores into human-readable analyst reports.
- [ ] **Isolated Dimension Scaling:** Define the output vectors for the other "Expert" models (Flow, Contextual/Macro, Time Series) so they can be merged into the Global Master Model.
