import { AfterViewInit, Component, Input, OnInit, ViewChild } from '@angular/core';
import { MatAccordion, MatExpansionModule } from '@angular/material/expansion';
import { MatDatepicker, MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { FormGroup, FormControl, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule, DatePipe, JsonPipe } from '@angular/common';
import { MatBadgeModule } from '@angular/material/badge';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatSelectModule } from '@angular/material/select';
import { CASH_FIVE, LOTTO } from '../app.constants';
import { filter } from 'rxjs';

@Component({
  selector: 'app-number-stats',
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
    MatBadgeModule,
    FlexLayoutModule,
    MatSelectModule
  ],
  templateUrl: './number-stats.component.html',
  styleUrl: './number-stats.component.scss'
})
export class NumberStatsComponent implements OnInit {
  badges: [{ 'label': any; 'value': number; }] | undefined;
  @Input() game: any | undefined;
  @Input() data: any[] | undefined;

  selected = new FormControl(null);

  ngOnInit(): void {
    this.selected.valueChanges
      .pipe(filter(value => !!value))
      .subscribe(data => {
        this.updateBadges();
      })
  }

  updateBadges() {
    this.badges = [] as any;
    let result: any = {};
    const selectedDraws = this.selected.value || 0;
    for (let i = 0; i <= this.getAllNumbers(this.game ?? ''); i++) {
      result[i] = 0;
    }
    for (let i = 0; i <= selectedDraws - 1; i++) {
      const numbers = this.data ? this.data[i]?.SortedNumberArray : [];
      numbers.forEach((number: number) => {
        result[number] = result[number] + 1;
      });
    }
    Object.keys(result).forEach(key => {
      this.badges?.push({ label: key, value: result[key] });
    });
  }

  getAllNumbers(game: string) {
    switch (game) {
      case CASH_FIVE:
        return 35;
      case LOTTO:
        return 54;
      default:
        return 9
    }
    return 0;
  }

}
