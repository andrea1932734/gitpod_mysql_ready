import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FruitsComponent } from './fruits/fruits.component';
import { AnimalComponent } from './animal/animal.component';
import { GenericComponent } from './generic/generic.component';


const Routes: Routes = [
  { path: 'animals', component: AnimalComponent},
  {path: '', redirectTo: '/animals', pathMatch: 'full'},
  { path: 'generic/:id', component: GenericComponent },
  { path: 'fruits', component: FruitsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(Routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

