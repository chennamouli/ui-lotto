import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwoStepComponent } from './two-step.component';

describe('TwoStepComponent', () => {
  let component: TwoStepComponent;
  let fixture: ComponentFixture<TwoStepComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TwoStepComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TwoStepComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
