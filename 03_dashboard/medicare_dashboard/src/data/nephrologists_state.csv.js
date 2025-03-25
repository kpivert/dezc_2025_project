import {csvFormat} from "d3-dsv";
import {runQuery} from "./google-bigquery.js";

const rows = await runQuery(`
  select
    rndrng_prvdr_state_abrvtn as State,
    count(1) as Nephrologists
  from
    \`dezc-final-project-medicare.medicare.providers\`
  where rndrng_prvdr_type = "Nephrology"
  group by State;
`);

process.stdout.write(csvFormat(rows));