import { CommonModule } from '@angular/common';
import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { AgChartsAngularModule } from 'ag-charts-angular';
import { AgChartOptions, AgCharts } from "ag-charts-community";

@Component({
  selector: 'app-hist-chart',
  standalone: true,
  imports: [AgChartsAngularModule, CommonModule],
  templateUrl: './hist-chart.component.html',
  styleUrl: './hist-chart.component.scss'
})
export class HistChartComponent implements OnInit, OnChanges{
  @Input() data: any[] | undefined;


  public options: AgChartOptions;

  constructor() {
    // this.data = [ { Num1: 20, }, { Num1: 25, }];
    this.options = {};
  }

  ngOnChanges(changes: SimpleChanges): void {
      this.drawChart();
  }

  ngOnInit(): void {
    this.drawChart();
  }

  drawChart() {
    this.options = {
      title: {
        text: "Number Histogram",
      },
      data: this.data,
      series: [
        {
          type: "histogram",
          xKey: "NumberInt",
          xName: "Numbers",
        },
      ],
      axes: [
        {
          type: "number",
          position: "bottom",
          title: { text: "Number" },
          tick: { interval: 2 },
        },
        {
          type: "number",
          position: "left",
          title: { text: "Number repetitions" },
        },
      ],
    };
  }


}