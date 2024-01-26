import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LottoComponent } from './lotto.component';

describe('LottoComponent', () => {
  let component: LottoComponent;
  let fixture: ComponentFixture<LottoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LottoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LottoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
