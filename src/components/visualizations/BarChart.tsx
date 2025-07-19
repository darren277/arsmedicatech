import * as d3 from 'd3';
import React, { useEffect } from 'react';

export default function BarChart({
  data,
  lowerBound,
  upperBound,
}: {
  data: {
    metricName: string;
    points: { date: string; value: number | null }[];
  }[];
  lowerBound?: number | '';
  upperBound?: number | '';
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ref.current.innerHTML = '';
    if (!data.length) return;

    const margin = { top: 20, right: 30, bottom: 30, left: 40 };
    const width = 500 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    // Flatten all points and get all unique dates
    const allPoints = data.flatMap(series => series.points);
    const allDates = Array.from(new Set(allPoints.map(d => d.date))).sort();
    const metrics = data.map(d => d.metricName);

    // X scale for dates (grouped)
    const x0 = d3.scaleBand().domain(allDates).range([0, width]).padding(0.2);
    // X1 for metrics within each date
    const x1 = d3
      .scaleBand()
      .domain(metrics)
      .range([0, x0.bandwidth()])
      .padding(0.05);
    // Y scale
    const y = d3
      .scaleLinear()
      .domain([
        lowerBound !== undefined && lowerBound !== '' ? lowerBound : 0,
        upperBound !== undefined && upperBound !== '' ? upperBound : d3.max(allPoints, d => d.value ?? 0) ?? 1,
      ])
      .nice()
      .range([height, 0]);
    // Color
    const color = d3.scaleOrdinal(d3.schemeCategory10).domain(metrics);

    const svg = d3
      .select(ref.current)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // X axis
    svg
      .append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x0).tickFormat(d => d as string));
    // Y axis
    svg.append('g').call(d3.axisLeft(y));

    // Draw bars
    svg
      .selectAll('g.date-group')
      .data(allDates)
      .enter()
      .append('g')
      .attr('class', 'date-group')
      .attr('transform', d => `translate(${x0(d as string)},0)`)
      .selectAll('rect')
      .data(date =>
        metrics.map(metric => {
          const series = data.find(d => d.metricName === metric);
          const point = series?.points.find(p => p.date === date);
          return {
            metric,
            value: point && point.value !== null ? point.value : 0,
            date,
          };
        })
      )
      .enter()
      .append('rect')
      .attr('x', d => x1(d.metric) ?? 0)
      .attr('y', d => y(d.value))
      .attr('width', x1.bandwidth())
      .attr('height', d => height - y(d.value))
      .attr('fill', d => color(d.metric) as string);

    // Legend
    const legend = svg
      .selectAll('.legend')
      .data(metrics)
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
  }, [data, lowerBound, upperBound]);

  return <div ref={ref}></div>;
}
