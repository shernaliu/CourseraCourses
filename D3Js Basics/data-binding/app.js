const dataset = [2,4,6,8,10]

d3.select("#viz").selectAll("p") 
.data(dataset)
.join("p")
.text((d,i) => `The data ${d} at this index ${i}`)