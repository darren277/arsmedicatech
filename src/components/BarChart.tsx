import * as d3 from 'd3';
import { useEffect, useState } from 'react';

const BarChart = () => {
  const [data, setData] = useState([
    {
      name: 'A',
      value: 50,
    },
    {
      name: 'B',
      value: 20,
    },
    {
      name: 'C',
      value: 40,
    },
    {
      name: 'D',
      value: 70,
    },
  ]);

  useEffect(() => {
    const w = 960 / 2;
    const h = 500 / 2;

    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = w - margin.left - margin.right;
    const height = h - margin.top - margin.bottom;

    const x = d3.scaleBand().range([0, width]).padding(0.1);
    const y = d3.scaleLinear().range([height, 0]);

    const svg = d3
      .select('.bar-chart')
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

    x.domain(
      data.map(function (d) {
        return d.name;
      })
    );
    y.domain([
      0,
      d3.max(data, function (d) {
        return d.value;
      }) ?? 0,
    ]);

    svg
      .selectAll('.bar')
      .data(data)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', function (d) {
        return x(d.name) ?? 0;
      })
      .attr('width', x.bandwidth())
      .attr('y', function (d) {
        return y(d.value);
      })
      .attr('height', function (d) {
        return height - y(d.value);
      });

    svg
      .append('g')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(x));

    svg.append('g').call(d3.axisLeft(y));
  }, [data]);

  return <div className="bar-chart"></div>;
};

export default BarChart;
