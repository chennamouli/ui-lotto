import { Routes } from '@angular/router';
import { CashfiveComponent } from './cashfive/cashfive.component';
import { Pick4Component } from './pick4/pick4.component';
import { LottoComponent } from './lotto/lotto.component';
import { Pick3Component } from './pick3/pick3.component';

export const routes: Routes = [
    {path: '', component: CashfiveComponent},
    {path: 'lotto', component: LottoComponent},
    {path: 'pick3', component: Pick3Component},
    {path: 'pick4', component: Pick4Component},
    // {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: '**', component: CashfiveComponent}
];
