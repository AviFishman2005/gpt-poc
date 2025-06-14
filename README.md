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

## Web Interface

A small static web version is available in the `web/` directory. It performs the
same API call in the browser using JavaScript.

Open `web/index.html` locally or host it via GitHub Pages:

1. Commit the contents of `web/` to your repository.
2. In the repository settings on GitHub, enable **GitHub Pages** and select the
   branch containing `web/index.html` as the source.
3. Your page will be served at `https://<user>.github.io/<repo>/`.

Click **Refresh** on the page to fetch the latest data directly from SANS.

