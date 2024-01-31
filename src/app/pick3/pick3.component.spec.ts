import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Pick3Component } from './pick3.component';

describe('Pick3Component', () => {
  let component: Pick3Component;
  let fixture: ComponentFixture<Pick3Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Pick3Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Pick3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
