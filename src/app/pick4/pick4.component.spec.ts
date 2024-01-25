import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Pick4Component } from './pick4.component';

describe('Pick4Component', () => {
  let component: Pick4Component;
  let fixture: ComponentFixture<Pick4Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Pick4Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Pick4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
