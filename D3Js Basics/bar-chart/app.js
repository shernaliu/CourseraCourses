async function barChart(){
    const dataset = await d3.csv("bodypart-injury-clean.csv")
    console.log(dataset)

    const width = 600
    const height = 600

    const margin = {top: 20, right: 30, bottom: 30, left: 40}

    const wrapper = canvas.append("g").style("transform", `translate(${margin.left}px , ${margin.top}px)`)

    const canvas = d3.select("#viz").append("svg").attr("width", width).attr("height", height)

    const xScale = d3.scaleBand()
                    .domain(["Arm", "Head", "Hand", "Leg", "Other"])
                    .range([0, width - margin.left])
                    .padding(0.5)

    // d3.extent calculates min and max value of an array. + sign cast from str to int
    const yScale = d3.scaleLinear()
                    .domain(d3.extent(dataset, d => +d.Total))
                    .range([height, 0]) // since coord in svg is inverted, our range is inverted as well.

    console.log(xScale("Leg"))
    console.log(yScale(1700))

    const barRect = wrapper.append("g")
                    .selectAll("rect")
                    .data(dataset)
                    .join("rect")
                    .attr('x', d => xScale(d.BodyRegion))
                    .attr('y', d => yScale(+d.Total))
                    .attr('width', xScale.bandwidth())
                    .attr('height', d => height - yScale(+d.Total))
                    .attr('fill', 'teal')

    const yAxis = d3.axisLeft().scale(yScale)
    wrapper.append("g").call(yAxis)
}

barChart()