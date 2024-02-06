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
export class HistChartComponent implements OnInit, OnChanges {
  @Input() data: any[] | undefined;
  @Input() title: string | undefined;

  @Input() xKey: string | undefined;

  public prob_dict!: any;

  public options: AgChartOptions;

  constructor() {
    // this.data = [ { NumberInt: 4, }, { NumberInt: 5, }, { NumberInt: 3, }, { NumberInt: 2, }, { NumberInt: 16, }, { NumberInt: 27, }];
    this.options = {};
  }

  ngOnChanges(changes: SimpleChanges): void {
    this.drawChart();
    this.prob_dict = this.calculateProbability(this.data ?? []);
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

  calculateProbability(data: any[]) {
    // Count the frequency of each number
    let frequencyCount:any = {};
    let totalCount = 0;
    data.forEach((obj: any) => {
      let num = obj.NumberInt;
      if (num >= 1 && num <= 35) {
        frequencyCount[num] = (frequencyCount[num] || 0) + 1;
        totalCount++;
      }
    });
    // Calculate the probability of each number
    let probabilities:any = [];
    for (let num = 1; num <= 35; num++) {
      if (frequencyCount[num]) {
        let tempNum = frequencyCount[num] * 100 / totalCount;
        tempNum = parseInt(tempNum.toFixed(2));
        // probabilities[num] = parseFloat(tempNum.toFixed(2));
        probabilities.push({'number': num, 'probability': tempNum});
      } else {
        // probabilities[num] = 0; // Set probability to 0 for numbers not present
        probabilities.push({'number': num, 'probability': 0});
      }
    }
    probabilities = probabilities.sort((a: { probability: number; }, b: { probability: number; }) => b.probability - a.probability);
    // console.log("Probabilities:", probabilities);
    return probabilities;
  }


}