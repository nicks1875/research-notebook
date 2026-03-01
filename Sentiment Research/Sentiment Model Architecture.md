
![[Ensemble-Model-Architecture.drawio.svg]]

Sentiment model acts as an "expert" in analyzing institutions and markets mood on a given stock, outputting this proposed vector:
### Model Output

| Index  | Category    | Example Value    | Interpretation                                                            |
| ------ | ----------- | ---------------- | ------------------------------------------------------------------------- |
| 0      | Alpha       | 0.012            | Predicts a 1.2% price increase                                            |
| 1      | Confidence  | 0.85             | High certainty in this prediction                                         |
| 2 - 17 | Context     | [-0.1, 0.4, ...] | Machine "fingerprint" of the news / social state. [[Latent Embeddings]]   |
| 18     | SEC Hook    | 0.70             | Contribution of SEC filings sentiment                                     |
| 19     | News Hook   | 0.20             | Contribution of news sentiment                                            |
| 20     | Social Hook | 0.10             | Contribution of social media sentiment                                    |
| 21     | Divergence  | 0.05             | How much each of the three sources disagrees - how far apart opinions are |
| 22     | Staleness   | 0.15             | Measures average age of the signals currently in model's memory           |

Where the hooks (index 18-20) are the contribution of each respective input model,  (dynamic attention weights), calculated in real time by the model. Also known as the  [[Model Attention]].

These weights are used my the MCP AI Agent to help "see" and explain how the model arrived at its prediction and how much emphasis it placed on each inputs

Another way of looking at the various parts at the output vector:

| Layer  | Component(s)              | For Whom?      | Purpose                                                                                      |
| ------ | ------------------------- | -------------- | -------------------------------------------------------------------------------------------- |
| Top    | Alpha / Confidence        | The Trade      | Tells you what to do (direction & size)                                                      |
| Middle | Hooks (SEC, News, Social) | Human Operator | Tells you why it arrived at its answer for transparency and trust                            |
| Bottom | Context (Embeddings)      | Machine        | Tells the global model the "vibe" or "market regimes". Allows it to discover hidden patterns |

### [[Sentiment Model Architecture - Stage 1]]

### [[Sentiment Model Architecture - Stage 2]]

### [[Sentiment Model Architecture - Stage 3]]

