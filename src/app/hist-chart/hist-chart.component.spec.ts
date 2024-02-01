import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistChartComponent } from './hist-chart.component';

describe('HistChartComponent', () => {
  let component: HistChartComponent;
  let fixture: ComponentFixture<HistChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HistChartComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(HistChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
