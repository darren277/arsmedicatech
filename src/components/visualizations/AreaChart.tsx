import * as d3 from 'd3';
import React, { useEffect } from 'react';

export default function AreaChart({
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

    // Flatten all points for x/y domains
    const allPoints = data.flatMap(series =>
      series.points.filter(p => p.value !== null)
    );
    const parseDate = d3.timeParse('%Y-%m-%d');
    const allParsedPoints = allPoints.map(d => ({
      ...d,
      date: parseDate(d.date) as Date,
    }));
    const metrics = data.map(d => d.metricName);

    // X and Y scales
    const x = d3
      .scaleTime()
      .domain(d3.extent(allParsedPoints, d => d.date) as [Date, Date])
      .range([0, width]);
    const y = d3
      .scaleLinear()
      .domain([
        lowerBound !== undefined && lowerBound !== '' ? lowerBound : d3.min(allParsedPoints, d => d.value as number) ?? 0,
        upperBound !== undefined && upperBound !== '' ? upperBound : d3.max(allParsedPoints, d => d.value as number) ?? 1,
      ])
      .nice()
      .range([height, 0]);
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
      .call(d3.axisBottom(x).ticks(5));
    // Y axis
    svg.append('g').call(d3.axisLeft(y));

    // Draw areas for each metric
    data.forEach(series => {
      const chartData = series.points
        .map(d => ({
          ...d,
          date: parseDate(d.date) as Date,
          value: d.value !== null ? d.value : 0,
        }))
        .filter(d => d.value !== null);
      svg
        .append('path')
        .datum(chartData)
        .attr('fill', color(series.metricName) as string)
        .attr('fill-opacity', 0.3)
        .attr('stroke', color(series.metricName) as string)
        .attr('stroke-width', 2)
        .attr(
          'd',
          d3
            .area<{ date: Date; value: number | null }>()
            .defined(d => d.value !== null)
            .x(d => x(d.date))
            .y0(y(0))
            .y1(d => y(d.value as number))
        );
    });

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
      .style('fill', d => color(d) as string)
      .style('opacity', 0.3);
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
