
**Goals**
- Build isolated dedicated models for each dimension of data and output a standardized embedding / sub-prediction, then feed this into master model that learns weights of sub-models (Ensemble Model)
- Build RAG dataset from various dimensions of data and with model prediction output
- Use with MCP AI agent to interpret the final results. Should advise user on the "why" of what price predictions and allow further interrogation

**Dimensions**
- [[Sentiment]]: News, Reddit, X - Captures market psychology. What the public "thinks" and "feels" about a stock
-
- Time Series: OHLCV - Open, High, Low, Close, Volume, Volatility "raw" numbers for a given stock - Tracks momentum and allows statistical modeling
-
- Contextual: P/E, Interest Rates - Captures "value" and macro environment
-
- Flow: Options, Dark Pools - Captures institutional intent
-
- Alternative / Real world: Web Traffic, Foot Traffic, etc. - Captures real world performance linked to a stock ticker. Can be used to predict trends in news / market prior to it breaking.

