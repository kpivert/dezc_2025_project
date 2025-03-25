---
theme: dashboard
title: Nephrologist dashboard
toc: false
---

```js
const nephs_state = FileAttachment("data/nephrologists_state.csv").csv({typed: true});
```

```js
// const states = topojson.feature(us, us.objects.states)

```

```js
Inputs.table(nephs_state)
```

```js

Plot.plot({
  y: {
    grid: true
  },
  marks: [
    Plot.ruleY([0]),
    Plot.barY(nephs_state, {x: "State", y: "Nephrologists", sort: {x: "y", reverse: true}, tip: true})
  ]
})

```


```js
// Plot.plot({
//   projection: "albers-usa", // Set the projection
//   marks: [
//     Plot.geo(states, {stroke: "black"}) // Add county boundaries using the geo mark
//   ]
// })
```