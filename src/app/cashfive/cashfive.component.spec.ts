import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CashfiveComponent } from './cashfive.component';

describe('CashfiveComponent', () => {
  let component: CashfiveComponent;
  let fixture: ComponentFixture<CashfiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CashfiveComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CashfiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
