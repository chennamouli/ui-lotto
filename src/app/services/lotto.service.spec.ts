import { TestBed } from '@angular/core/testing';

import { LottoService } from './lotto.service';

describe('LottoService', () => {
  let service: LottoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LottoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
