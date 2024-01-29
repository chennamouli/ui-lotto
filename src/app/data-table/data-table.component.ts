import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AgGridAngular } from 'ag-grid-angular';
import { ColDef, GridReadyEvent, IDateFilterParams, ITextFilterParams, GridApi } from 'ag-grid-community';
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
import { FlexLayoutModule } from '@angular/flex-layout';

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
    FlexLayoutModule,
    ReactiveFormsModule,
  ],
  templateUrl: './data-table.component.html',
  styleUrl: './data-table.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DataTableComponent implements OnInit {
  @Input() game: any | undefined;
  @Input() data: any[] | undefined;
  public gridApi: GridApi | undefined;
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

  get displayedCount() {
    return this.gridApi?.getDisplayedRowCount()
  }

  toggleOptionalColumns(){
    this.gridApi?.getColumnDefs()?.forEach((col: ColDef) => {
      if(['Num1'].indexOf(col.field as any) >=0)  {
        col.hide = false;
      }
    })
    this.gridApi?.refreshCells();
  }

  getColDefs() {
    if (!this.data) return;
    if(this.columnDefs) return this.columnDefs;
    const columnDefs: ColDef[] = [];
    Object.keys(this.data[0]).forEach(key => {
      if (key.toLowerCase().indexOf('date') >= 0) {
        columnDefs.push({ 'field': key, pinned: 'left', 'filter': 'agDateColumnFilter', 'filterParams': filterParams });
      } else if (key.toLowerCase().indexOf('SortedNumberArray'.toLowerCase()) >= 0) {
        columnDefs.push({ 'field': key, 'filter': 'agTextColumnFilter', 'filterParams': customTextFilterParams });
      } else if(['Num1','Num2','Num3','Num4','Num5'].indexOf(key) >= 0) {
        columnDefs.push({ 'field': key, hide: true });
      } else {
        columnDefs.push({ 'field': key });
      }
    });
    this.columnDefs = columnDefs;
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

var customTextFilterParams: ITextFilterParams = {
  textMatcher: ({ filterOption, value, filterText }) => {
      if (filterText == null) {
          return false;
      }
      switch (filterOption) {
          case 'contains':
              return containsAllElements(value.split(/[,\s-]+/), filterText.trim().split(/[,\s-]+/)); // value.indexOf(filterText) >= 0;
          case 'notContains':
              return doesNotContainAnyElement(value.split(/[,\s-]+/), filterText.trim().split(/[,\s-]+/)); // value.indexOf(filterText) < 0;
          case 'equals':
              return value === filterText;
          case 'notEqual':
              return value != filterText;
          case 'startsWith':
              return value.indexOf(filterText) === 0;
          case 'endsWith':
              const index = value.lastIndexOf(filterText);
              return index >= 0 && index === (value.length - filterText.length);
          default:
              // should never happen
              console.warn('invalid filter type ' + filterOption);
              return false;
      }
  }
}

function findCommonValues(array1: any[], array2: any[]) {
  if(!Array.isArray(array1) || !Array.isArray(array2)) return [];
  return array1.filter(value => array2.includes(value));
}

function containsAllElements(array1: any[], array2: any[]) {
  if(!Array.isArray(array1) || !Array.isArray(array2)) false;
  return array2.every(element => array1.includes(element));
}

function doesNotContainAnyElement(array1: any[], array2: any[]) {
  return !array2.some(element => array1.includes(element));
}


