
Each code area has a separate environment created with uv:

```
	cd Code\XXX
	uv init
	uv venv
	# For adding dependencies
	uv add xxx
	# To run the streamlit app in a code area, use:
	streamlit run main.py
```

To start an existing environment:

```
.venv\Scripts\activate
streamlit run main.py
```