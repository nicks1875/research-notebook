import yfinance as yf
import streamlit as st
import pandas as pd

from itertools import chain

# S&P Stocks to Train on:
# NVDA - Nvidia - Information Technology sector
# AAPL - Apple Inc - Information Technology sector
# MSFT - Microsoft - Information Technology sector
# AVGO - Broadcom - Information Technology sector
# MU - Micron Technology - Information Technology sector

# BRK.B - Berkshire Hathaway - Financials
# JPM - JPMogran Chase - Financials
# V - Visa Inc. - Financials
# MA - Mastercard - Financials
# BAC - Bank of America - Financials

# GOOGL - Alphabet Inc (Class A) - Communication Services
# META - Meta Platforms - Communication Services
# NFLX - Netflix - Communication Services
# TMUS T-Mobile-US - Communication Services
# VZ - Verizon - Communication Services

# AMZN - Amazon - Consumer Discretionary
# TSLA - Tesla Inc - Consumer Discretionary
# HD - Home Depot - Consumer Discretionary
# MCD McDonald's - Consumer Discretionary
# TJX - TJX Companies - Consumer Discretionary

# LLY - Lilly (Eli) - Health Care
# JNJ - Johnson & Johnson - Health Care
# ABBV - AbbVie - Health Care
# MRK - Merck & Co. - Health Care
# UNH - UnitedHealth Group - Health Care

# GE - GE Aerospace - Industrials
# CAT - Caterpillar Inc. - Industrials
# RTX - RTX Corporation - Industrials
# GEV - GE Vernova - Industrials
# BA - Boeing - Industrials

# WMT - Walmart - Consumer Staples
# COST - Costco - Consumer Staples
# PG - Procter & Gamble - Consumer Staples
# KO - Coca-Cola Company - Consumer Staples
# PM - Philip Morris International - Consumer Staples

# XOM - ExxonMobil - Energy
# CVX - Chevron Corporation - Energy
# COP - ConocoPhilips - Energy
# WMB - Williams Companies - Energy
# SLB - Schlumberger - Energy

# NEE - NextEra Energy - Utilities
# CEG - Constellation Energy - Utilities
# SO - Southern Company - Utilities
# DUK - Duke Energy - Utilities
# AEP - American Electric Power - Utilities

# LIN - Linde plc - Materials
# NEM - Newmont - Materials
# FCX - Freeport-McMoRan - Materials
# SHW - Sherwin-Williams - Materials
# ECL - Ecolab - Materials

def main():

    st.text('This sentiment dataset collects the 5 largest stocks from each sector (as of 02/28/25) in the S&P500')
    sector_data = {
        "Information Technology": ["NVDA", "AAPL", "MSFT", "AVGO", "MU"],
        "Financials": ["BRK.B", "JPM", "V", "MA", "BAC"],
        "Communication Services": ["GOOGL", "META", "NFLX", "TMUS", "VZ"],
        "Consumer Discretionary": ["AMZN", "TSLA", "HD", "MCD", "TJX"],
        "Health Care": ["LLY", "JNJ", "ABBV", "MRK", "UNH"],
        "Industrials": ["GE", "CAT", "RTX", "GEV", "BA"],
        "Consumer Staples": ["WMT", "COST", "PG", "KO", "PM"],
        "Energy": ["XOM", "CVX", "COP", "WMB", "SLB"],
        "Utilities": ["NEE", "CEG", "SO", "DUK", "AEP"],
        "Materials": ["LIN", "NEM", "FCX", "SHW", "ECL"]
    }

    rows = []
    for sector, tickers in sector_data.items():
        for ticker in tickers:
            rows.append({"Stock Symbol": ticker, "Sector": sector})

    s_and_p_500_tickers_df = pd.DataFrame(rows)
    st.title("S&P 500 Tickers by Sector")
    st.dataframe(s_and_p_500_tickers_df, use_container_width=True, hide_index=True)

    # for ticker_symbol in s_and_p_500_tickers:
    #     ticker = yf.Ticker(ticker_symbol)

if __name__ == "__main__":
    main()
