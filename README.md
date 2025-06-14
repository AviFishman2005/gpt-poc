# Threat Intelligence Platform Proof of Concept

This repository contains a minimal threat intelligence platform that fetches live attack data from the [SANS Internet Storm Center](https://isc.sans.edu/). It includes a simple command-line interface and tests.

## Daily Attacked

Run the following to display the country that was most attacked today:

```bash
python3 -m threat_intel.platform
```

The script prints the ISO country code, its flag, and the number of targets reported for that country.

## GUI Interface

A minimal Tkinter interface is available to display the same data. Launch it with:

```bash
python3 -m threat_intel.ui
```

Click **Refresh** to retrieve the latest information.

