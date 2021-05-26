# AWS Community Builder Member Map

This is the source code and other supporting files associated with the AWS Community Builder Member Map.

This was a quick proof of concept, I'm sure there are many ways this can be improved.

## Directories

- `geocoder`: A script to geocode a list of addresses into the json needed by the various maps
- `geochart`: Show counts of members on a Google Geochart
- `markers`: Show counts of members as clustered markets on Google Map

## API Keys

This requires a Google API Key with the Javascript Maps API enabled. The geocoder script also requires the Geocoding API enabled.

You can do a find/replace on `<YOUR API KEY>` to update the code with your specific API Key.

## Demonstration

You can see a demonstration of these maps that show the the home-base locations of the 1000+ active AWS Community Builders as of May 2021 at the following URLs:

- http://acbmap.humbleg.com/markers/
- http://acbmap.humbleg.com/geochart/
