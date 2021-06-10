import React, { Component } from "react";
import Chart from "react-apexcharts";

class LineGraph extends Component {
  constructor(props) {
    super(props);

    this.state = {
      options: {
        stroke: {
          width: 1.5
        },
        chart: {
          id: "basic-bar",
          width: "100%"
        },
        xaxis: {
          categories: ['May 2020', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr 2021'],
        }
      },
      series: [
        {
          name: "Portfolio (%)",
          data: ['57%', '75%', '87%', '80%', '98%', '115%', '110%', '130%', '140%', '127%', '120%', '133%']
        },
        {
          name: "Benchmark (%)",
          data: ['73%', '87%', '90%', '110%', '105%', '127%', '105%', '110%', '119%', '123%', '129%', '139%']
        }
      ]
    };
  }

  render() {
    return (
      <div className="app">
        <div className="row">
          <div className="mixed-chart">
            <Chart
            options={this.state.options}
            series={this.state.series}
            type="line"
            width="100%"
            />
          </div>
        </div>
      </div>
    );
  }
}

export default LineGraph;