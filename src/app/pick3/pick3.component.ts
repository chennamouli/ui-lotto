import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatAccordion, MatExpansionModule } from '@angular/material/expansion';
import { MatDatepicker, MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { provideNativeDateAdapter } from '@angular/material/core';
import { FormGroup, FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule, DatePipe, JsonPipe } from '@angular/common';
import { LottoService } from '../services/lotto.service';
import { NumberStatsComponent } from '../number-stats/number-stats.component';
import { DateRangeComponent } from '../date-range/date-range.component';
import { DataTableComponent } from '../data-table/data-table.component';

@Component({
  selector: 'app-pick3',
  standalone: true,
  imports: [
    MatButtonModule,
    MatExpansionModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    MatDatepicker,
    MatDatepickerModule,
    MatFormFieldModule,
    MatDatepickerModule,
    FormsModule,
    ReactiveFormsModule,
    JsonPipe,
    DatePipe,
    CommonModule,
    NumberStatsComponent,
    DateRangeComponent,
    DataTableComponent
  ],
  providers: [provideNativeDateAdapter()],
  templateUrl: './pick3.component.html',
  styleUrl: './pick3.component.scss'
})
export class Pick3Component implements OnInit, AfterViewInit {
  @ViewChild(MatAccordion) accordion: MatAccordion | undefined;
  startDate: any;
  endDate: any;
  data: any;

  constructor(private service: LottoService) { }

  ngOnInit(): void {
    this.service.getPick3Data().subscribe((data: any) => {
      console.log('Pick 4 data: ', this.service.getPrettyJson(data[0]));
      this.data = data;
    })
  }

  ngAfterViewInit(): void {
    setTimeout(() => this.accordion?.openAll(), 1000);
  }

  onSelectDateRange(dateRange: any) {
    this.startDate = dateRange?.startDate;
    this.endDate = dateRange?.endDate;
  }

}
