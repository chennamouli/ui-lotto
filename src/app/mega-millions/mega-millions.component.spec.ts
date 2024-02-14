import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MegaMillionsComponent } from './mega-millions.component';

describe('MegaMillionsComponent', () => {
  let component: MegaMillionsComponent;
  let fixture: ComponentFixture<MegaMillionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MegaMillionsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MegaMillionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
