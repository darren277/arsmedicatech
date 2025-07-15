import * as d3 from 'd3';
import React, { useEffect } from 'react';

// LineChart component using d3
export default function LineChart({
  data,
  metricName,
}: {
  data: { date: string; value: number }[];
  metricName: string;
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    // Clear previous chart
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

    // Parse dates
    const parseDate = d3.timeParse('%Y-%m-%d');
    const chartData = data.map(d => ({
      ...d,
      date: parseDate(d.date) as Date,
    }));

    // X and Y scales
    const x = d3
      .scaleTime()
      .domain(d3.extent(chartData, d => d.date) as [Date, Date])
      .range([0, width]);
    const y = d3
      .scaleLinear()
      .domain([
        d3.min(chartData, d => d.value) ?? 0,
        d3.max(chartData, d => d.value) ?? 1,
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

    // Line
    svg
      .append('path')
      .datum(chartData)
      .attr('fill', 'none')
      .attr('stroke', '#2563eb')
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
      .selectAll('dot')
      .data(chartData)
      .enter()
      .append('circle')
      .attr('cx', d => x(d.date))
      .attr('cy', d => y(d.value))
      .attr('r', 3)
      .attr('fill', '#2563eb');
  }, [data, metricName]);

  return <div ref={ref}></div>;
}
