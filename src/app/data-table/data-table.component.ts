import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AgGridAngular } from 'ag-grid-angular';
import { ColDef, GridReadyEvent, IDateFilterParams } from 'ag-grid-community';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-quartz.css';
import { ChangeDetectionStrategy, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
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
  selector: 'app-data-table',
  standalone: true,
  imports: [
    AgGridAngular,
    HttpClientModule,
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
  templateUrl: './data-table.component.html',
  styleUrl: './data-table.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DataTableComponent implements OnInit {
  @Input() game: any | undefined;
  @Input() data: any[] | undefined;
  private gridApi: any;
  public columnDefs: ColDef[] = [];
  public columnDefs2: ColDef[] = [
    { field: 'athlete' },
    { field: 'age', filter: 'agNumberColumnFilter', maxWidth: 100 },
    {
      field: 'date',
      filter: 'agDateColumnFilter',
      filterParams: filterParams,
    },
    { field: 'country', filter: 'agSetColumnFilter' },
    { field: 'sport', filter: 'agMultiColumnFilter' },
    { field: 'gold', filter: 'agNumberColumnFilter' },
    { field: 'silver', filter: 'agNumberColumnFilter' },
    { field: 'bronze', filter: 'agNumberColumnFilter' },
    { field: 'total', filter: false },
  ];
  public defaultColDef: ColDef = {
    flex: 1,
    minWidth: 200,
    initialWidth: 200,
    wrapHeaderText: true,
    autoHeaderHeight: true,
    filter: 'agTextColumnFilter',
    menuTabs: ['filterMenuTab'],
  };
  public rowData!: any[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.columnDefs = this.getColDefs() as any;
  }

  onGridReady(params: GridReadyEvent<any>) {
    this.gridApi = params.api;
  }

  getColDefs() {
    if (!this.data) return;
    if(this.columnDefs) return this.columnDefs;
    const columnDefs: ColDef[] = [];
    Object.keys(this.data[0]).forEach(key => {
      if (key.toLowerCase().indexOf('date') >= 0) {
        columnDefs.push({ 'field': key, 'filter': 'agDateColumnFilter', 'filterParams': filterParams });
      } else {
        columnDefs.push({ 'field': key });
      }
    });
    console.log('Coldefs: ', columnDefs)
    return columnDefs;
  }

}

var filterParams: IDateFilterParams = {
  comparator: (filterLocalDateAtMidnight: Date, cellValue: string) => {
    var dateAsString = cellValue;
    if (dateAsString == null) return -1;
    var cellDate = new Date(cellValue);
    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
      return 0;
    }
    if (cellDate < filterLocalDateAtMidnight) {
      return -1;
    }
    if (cellDate > filterLocalDateAtMidnight) {
      return 1;
    }
    return 0;
  },
};


