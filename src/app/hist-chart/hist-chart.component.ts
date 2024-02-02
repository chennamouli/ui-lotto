import { CommonModule } from '@angular/common';
import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatIconModule } from '@angular/material/icon';
import { AgChartsAngularModule } from 'ag-charts-angular';
import { AgChartOptions, AgCharts } from "ag-charts-community";

@Component({
  selector: 'app-hist-chart',
  standalone: true,
  imports: [AgChartsAngularModule, CommonModule, MatIconModule, MatExpansionModule],
  templateUrl: './hist-chart.component.html',
  styleUrl: './hist-chart.component.scss'
})
export class HistChartComponent implements OnInit, OnChanges{
  @Input() data: any[] | undefined;
  @Input() title: string | undefined;

  @Input() xKey: string | undefined;


  public options: AgChartOptions;

  constructor() {
    // this.data = [ { NumberInt: 4, }, { NumberInt: 5, }, { NumberInt: 3, }, { NumberInt: 2, }, { NumberInt: 16, }, { NumberInt: 27, }];
    this.options = {};
  }

  ngOnChanges(changes: SimpleChanges): void {
      this.drawChart();
  }

  ngOnInit(): void {
    // this.drawChart();
  }

  drawChart() {
    this.options = {
      title: {
        text: this.title ?? "Number Histogram",
      },
      autoSize: true,
      data: this.data,
      series: [
        {
          type: "histogram",
          xKey: this.xKey ?? "NumberInt",
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