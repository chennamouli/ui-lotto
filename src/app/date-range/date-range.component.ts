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
export class DateRangeComponent {
  @Output() dateRange = new EventEmitter();
  startDate: any;
  endDate: any;
  range = new FormGroup({
    start: new FormControl<Date | null>(null),
    end: new FormControl<Date | null>(null),
  });

  onSubmit() {
    this.startDate = this.range.controls.start.value;
    this.endDate = this.range.controls.end.value;
    this.dateRange.emit({ startDate: this.startDate, endDate: this.endDate });
  }
}
