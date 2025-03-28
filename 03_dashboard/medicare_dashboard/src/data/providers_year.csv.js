import {csvFormat} from "d3-dsv";
import {runQuery} from "./google-bigquery.js";

const years = await runQuery(`
  select
    *
  from
    \`dezc-final-project-medicare.medicare.medicare_providers_year\`;
`);

process.stdout.write(csvFormat(years));