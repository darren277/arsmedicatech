import * as d3 from 'd3';
import React, { useEffect } from 'react';

export default function Heatmap({
  data,
}: {
  data: { metricName: string; points: { date: string; value: number }[] }[];
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ref.current.innerHTML = '';
    if (!data.length || !data[0].points.length) return;

    // For now, use only the first metric
    const metric = data[0].metricName;
    const points = data[0].points;

    // Try to extract hour from date if present (e.g., '2024-06-01T14:00')
    const parseDateTime = d3.timeParse('%Y-%m-%dT%H:%M');
    const parseDate = d3.timeParse('%Y-%m-%d');
    const allDates = Array.from(
      new Set(points.map(p => p.date.slice(0, 10)))
    ).sort();
    // Try to get hours if present, else just use a single row
    let allHours: string[] = [];
    let hasHour = false;
    points.forEach(p => {
      if (p.date.length > 10 && p.date.includes('T')) hasHour = true;
    });
    if (hasHour) {
      allHours = Array.from(
        new Set(
          points.map(p => {
            const dt = parseDateTime(p.date);
            return dt
              ? dt.getHours().toString().padStart(2, '0') + ':00'
              : '00:00';
          })
        )
      ).sort();
    } else {
      allHours = ['all'];
    }

    // Build a matrix: rows = hours, cols = dates
    const matrix = allHours.map(hour =>
      allDates.map(date => {
        let value = 0;
        if (hasHour) {
          const match = points.find(p => {
            const dt = parseDateTime(p.date);
            return (
              dt &&
              dt.getHours().toString().padStart(2, '0') + ':00' === hour &&
              p.date.slice(0, 10) === date
            );
          });
          value = match ? match.value : 0;
        } else {
          const match = points.find(p => p.date.slice(0, 10) === date);
          value = match ? match.value : 0;
        }
        return value;
      })
    );

    const margin = { top: 40, right: 20, bottom: 40, left: 60 };
    const cellSize = 28;
    const width = allDates.length * cellSize + margin.left + margin.right;
    const height = allHours.length * cellSize + margin.top + margin.bottom;

    const svg = d3
      .select(ref.current)
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Color scale
    const allValues = matrix.flat();
    const color = d3
      .scaleSequential(d3.interpolateYlOrRd)
      .domain([d3.min(allValues) ?? 0, d3.max(allValues) ?? 1]);

    // Draw cells
    svg
      .selectAll('g.row')
      .data(matrix)
      .enter()
      .append('g')
      .attr('class', 'row')
      .attr('transform', (d, i) => `translate(0,${i * cellSize})`)
      .selectAll('rect')
      .data(d => d)
      .enter()
      .append('rect')
      .attr('x', (d, j) => j * cellSize)
      .attr('width', cellSize)
      .attr('height', cellSize)
      .attr('fill', d => color(d));

    // X axis (dates)
    svg
      .append('g')
      .selectAll('text')
      .data(allDates)
      .enter()
      .append('text')
      .attr('x', (d, i) => i * cellSize + cellSize / 2)
      .attr('y', -8)
      .attr('text-anchor', 'middle')
      .attr('font-size', 12)
      .text(d => d);

    // Y axis (hours)
    svg
      .append('g')
      .selectAll('text')
      .data(allHours)
      .enter()
      .append('text')
      .attr('x', -8)
      .attr('y', (d, i) => i * cellSize + cellSize / 2)
      .attr('text-anchor', 'end')
      .attr('alignment-baseline', 'middle')
      .attr('font-size', 12)
      .text(d => d);

    // Legend
    const legendWidth = 100;
    const legendHeight = 12;
    const legendSvg = svg
      .append('g')
      .attr('transform', `translate(0,${allHours.length * cellSize + 20})`);
    const legendScale = d3
      .scaleLinear()
      .domain(color.domain() as [number, number])
      .range([0, legendWidth]);
    const legendAxis = d3
      .axisBottom(legendScale)
      .ticks(5)
      .tickFormat(d3.format('.2f'));
    // Gradient
    const defs = svg.append('defs');
    const gradientId = 'heatmap-gradient';
    const gradient = defs
      .append('linearGradient')
      .attr('id', gradientId)
      .attr('x1', '0%')
      .attr('x2', '100%')
      .attr('y1', '0%')
      .attr('y2', '0%');
    for (let i = 0; i <= 100; i++) {
      gradient
        .append('stop')
        .attr('offset', `${i}%`)
        .attr('stop-color', color(legendScale.invert((i / 100) * legendWidth)));
    }
    legendSvg
      .append('rect')
      .attr('width', legendWidth)
      .attr('height', legendHeight)
      .style('fill', `url(#${gradientId})`);
    legendSvg
      .append('g')
      .attr('transform', `translate(0,${legendHeight})`)
      .call(legendAxis)
      .selectAll('text')
      .attr('font-size', 10);
    // Label
    legendSvg
      .append('text')
      .attr('x', legendWidth / 2)
      .attr('y', legendHeight + 24)
      .attr('text-anchor', 'middle')
      .attr('font-size', 12)
      .text(metric);
  }, [data]);

  return <div ref={ref}></div>;
}
