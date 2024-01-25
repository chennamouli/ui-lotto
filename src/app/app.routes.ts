import { Routes } from '@angular/router';
import { CashfiveComponent } from './cashfive/cashfive.component';
import { Pick4Component } from './pick4/pick4.component';

export const routes: Routes = [
    {path: 'home', component: CashfiveComponent},
    {path: 'pick4', component: Pick4Component},
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: '**', component: CashfiveComponent}
];
