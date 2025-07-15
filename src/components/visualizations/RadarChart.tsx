import * as d3 from 'd3';
import React, { useEffect } from 'react';

export default function RadarChart({
  data,
  date,
}: {
  data: { metricName: string; points: { date: string; value: number }[] }[];
  date?: string; // Optional: show snapshot for a specific date
}) {
  const ref = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ref.current.innerHTML = '';
    if (!data.length) return;

    // Prepare data: for each metric, get the value for the selected date (or most recent)
    const metrics = data.map(d => d.metricName);
    const values = data.map(series => {
      let point;
      if (date) {
        point = series.points.find(p => p.date === date);
      }
      if (!point) {
        // Use most recent value
        point = [...series.points].sort((a, b) =>
          b.date.localeCompare(a.date)
        )[0];
      }
      return point ? point.value : 0;
    });

    const numAxes = metrics.length;
    const angleSlice = (Math.PI * 2) / numAxes;
    const maxValue = Math.max(...values, 1);
    const minValue = 0;
    const radius = 120;
    const width = 350;
    const height = 350;
    const centerX = width / 2;
    const centerY = height / 2;

    const svg = d3
      .select(ref.current)
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr('transform', `translate(${centerX},${centerY})`);

    // Draw grid (concentric circles)
    const levels = 5;
    for (let level = 1; level <= levels; level++) {
      const r = (radius / levels) * level;
      svg
        .append('circle')
        .attr('cx', 0)
        .attr('cy', 0)
        .attr('r', r)
        .attr('fill', 'none')
        .attr('stroke', '#ccc')
        .attr('stroke-dasharray', '2,2');
    }

    // Draw axes
    metrics.forEach((metric, i) => {
      const angle = i * angleSlice - Math.PI / 2;
      const x = Math.cos(angle) * radius;
      const y = Math.sin(angle) * radius;
      svg
        .append('line')
        .attr('x1', 0)
        .attr('y1', 0)
        .attr('x2', x)
        .attr('y2', y)
        .attr('stroke', '#888');
      // Axis label
      svg
        .append('text')
        .attr('x', x * 1.1)
        .attr('y', y * 1.1)
        .attr('text-anchor', x > 0 ? 'start' : x < 0 ? 'end' : 'middle')
        .attr(
          'alignment-baseline',
          y > 0 ? 'hanging' : y < 0 ? 'baseline' : 'middle'
        )
        .attr('font-size', 12)
        .text(metric);
    });

    // Draw data polygon
    const color = d3.scaleOrdinal(d3.schemeCategory10).domain(metrics);
    const points = values.map((v, i) => {
      const angle = i * angleSlice - Math.PI / 2;
      const r = ((v - minValue) / (maxValue - minValue)) * radius;
      return [Math.cos(angle) * r, Math.sin(angle) * r];
    });
    svg
      .append('polygon')
      .attr('points', points.map(p => p.join(',')).join(' '))
      .attr('fill', color('polygon') as string)
      .attr('fill-opacity', 0.3)
      .attr('stroke', color('polygon') as string)
      .attr('stroke-width', 2);
    // Draw data points
    points.forEach((p, i) => {
      svg
        .append('circle')
        .attr('cx', p[0])
        .attr('cy', p[1])
        .attr('r', 4)
        .attr('fill', color(metrics[i]) as string);
    });
  }, [data, date]);

  return <div ref={ref}></div>;
}
