
### Model Training

The final model will need to be trained with ground truth labeled data in order to improve its prediction capability.

Capturing text sources and comparing it to timestamps for *raw* price of a stock will not work well, due to many other hidden factors / noise that are obscuring the model training . In other words, the training data needs to isolate the influence of sentiment as much as possible. We will need to try and isolate [[Abnormal Returns]] 

For gathering training data, events related to sentiment that had the largest impact on the market should also be prioritized instead of picking any random time interval. Examples may include:
 - Earnings Days (SEC/News focus)
 - Product Launches (News/Social focus)
 - FDA/Legal Rulings (SEC focus)

### Collecting Training Data

In order to create higher quality training data, the following effects on the price of a stock need to be isolated and removed:

- Remove the "Market" layer  (Beta) - a metric measuring a specific stock's volatility—or systematic risk—compared to the overall market.
	Example: If the S&P 500 goes up 2% and your stock goes up 2%, the sentiment for your stock might actually be Neutral. The stock just moved because the whole world moved.

- Remove the "Sector" layer (Sector Momentum) - rate at which a specific trading signal or predictive model loses its edge—and therefore its profitability—over time. Remove the part of the price move that was caused by the Sector (e.g., all semiconductor stocks moving together) to find the Idiosyncratic Alpha (the move unique to a ticker)
	Example: NVIDIA releases great news, all AI stocks (AMD, Intel) might go up. That isn't the stock's sentiment; it's Sector Momentum.

- Remove the "Technical" layer (Mean Reversion) - theory that asset prices, historical returns, or even economic indicators will eventually return to their long-term average—or "mean."

After removing these three components, the remainder is the Unexplained Residual, also known as [[Abnormal Returns]]. This is what the final model will be trained on.