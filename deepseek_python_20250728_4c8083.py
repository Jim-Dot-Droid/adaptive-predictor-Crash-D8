# Import Streamlit FIRST
import streamlit as st

# Then try Plotly imports
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("Plotly not available - using simple text display")

# Other imports
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# Rest of your app code...
# [Keep all your existing code after the imports]