import * as d3 from 'd3';
import React, { useEffect } from 'react';

// Multi-metric LineChart component using d3
export default function LineChart({
  data,
}: {
  data: { metricName: string; points: { date: string; value: number }[] }[];
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ref.current.innerHTML = '';
    if (!data.length) return;

    const margin = { top: 20, right: 30, bottom: 30, left: 40 };
    const width = 500 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    const svg = d3
      .select(ref.current)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Flatten all points for x/y domains
    const allPoints = data.flatMap(series => series.points);
    const parseDate = d3.timeParse('%Y-%m-%d');
    const allParsedPoints = allPoints.map(d => ({
      ...d,
      date: parseDate(d.date) as Date,
    }));

    // X and Y scales
    const x = d3
      .scaleTime()
      .domain(d3.extent(allParsedPoints, d => d.date) as [Date, Date])
      .range([0, width]);
    const y = d3
      .scaleLinear()
      .domain([
        d3.min(allParsedPoints, d => d.value) ?? 0,
        d3.max(allParsedPoints, d => d.value) ?? 1,
      ])
      .nice()
      .range([height, 0]);

    // X axis
    svg
      .append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x).ticks(5));

    // Y axis
    svg.append('g').call(d3.axisLeft(y));

    // Color scale
    const color = d3
      .scaleOrdinal(d3.schemeCategory10)
      .domain(data.map(d => d.metricName));

    // Draw lines for each metric
    data.forEach(series => {
      const chartData = series.points.map(d => ({
        ...d,
        date: parseDate(d.date) as Date,
      }));
      svg
        .append('path')
        .datum(chartData)
        .attr('fill', 'none')
        .attr('stroke', color(series.metricName) as string)
        .attr('stroke-width', 2)
        .attr(
          'd',
          d3
            .line<{ date: Date; value: number }>()
            .x(d => x(d.date))
            .y(d => y(d.value))
        );
      // Dots
      svg
        .selectAll(`dot-${series.metricName}`)
        .data(chartData)
        .enter()
        .append('circle')
        .attr('cx', d => x(d.date))
        .attr('cy', d => y(d.value))
        .attr('r', 3)
        .attr('fill', color(series.metricName) as string);
    });

    // Legend
    const legend = svg
      .selectAll('.legend')
      .data(data.map(d => d.metricName))
      .enter()
      .append('g')
      .attr('class', 'legend')
      .attr('transform', (d, i) => `translate(0,${i * 20})`);

    legend
      .append('rect')
      .attr('x', width - 18)
      .attr('width', 18)
      .attr('height', 18)
      .style('fill', d => color(d) as string);

    legend
      .append('text')
      .attr('x', width - 24)
      .attr('y', 9)
      .attr('dy', '.35em')
      .style('text-anchor', 'end')
      .text(d => d);
  }, [data]);

  return <div ref={ref}></div>;
}
