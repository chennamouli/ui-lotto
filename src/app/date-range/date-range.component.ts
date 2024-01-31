import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatDatepicker, MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { provideNativeDateAdapter } from '@angular/material/core';
import { FormGroup, FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule, DatePipe } from '@angular/common';
@Component({
  selector: 'app-date-range',
  standalone: true,
  imports: [
    DatePipe,
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
    CommonModule,
    ReactiveFormsModule,
  ],
  templateUrl: './date-range.component.html',
  styleUrl: './date-range.component.scss'
})
export class DateRangeComponent implements OnInit{
  @Output() dateRange = new EventEmitter();
  range = new FormGroup({
    start: new FormControl<Date | null>(null),
    end: new FormControl<Date | null>(null),
  });

  ngOnInit(): void {
    this.setDefaultDateRange();
    setTimeout(() => {
      this.dateRange.emit({ startDate: this.startDate, endDate: this.endDate });
    }, 2000);
  }

  onSubmit() {
    this.saveDateRange();
    this.emitDateRange();
  }

  onClear() {
    this.range.controls.start.setValue(null);
    this.range.controls.end.setValue(null);
    this.saveDateRange();
    this.emitDateRange();
  }

  get startDate() {
    return this.range.controls.start.value;
  }

  get endDate() {
    return this.range.controls.end.value;
  }

  emitDateRange() {
    this.dateRange.emit({ startDate: this.startDate, endDate: this.endDate });
  }

  saveDateRange() {
    sessionStorage.setItem('startDate', this.startDate as any);
    sessionStorage.setItem('endDate', this.endDate as any);
  }

  setDefaultDateRange() {
    if(sessionStorage.getItem('startDate') && sessionStorage.getItem('startDate') != 'null') {
      this.range.controls.start.setValue(new Date(sessionStorage.getItem('startDate') as any));
    }
    if(sessionStorage.getItem('endDate') && sessionStorage.getItem('endDate') != 'null') {
      this.range.controls.end.setValue(new Date(sessionStorage.getItem('endDate') as any));
    }
    if(!this.startDate && !this.endDate) {
      var lastSeventhDay = new Date();
      lastSeventhDay.setDate(lastSeventhDay.getDate() - 7);
      this.range.controls.start.setValue(lastSeventhDay);
      this.range.controls.end.setValue(new Date());
    }
  }

}
