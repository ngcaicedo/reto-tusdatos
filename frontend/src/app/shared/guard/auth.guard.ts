import { Observable, of } from 'rxjs';
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthStateService } from '../states/auth-state.service';

export const authGuard: CanActivateFn = (): Observable<boolean> => {
  const auth = inject(AuthStateService);
  const router = inject(Router);

  const isLoggedIn = auth.isLoggedIn();

  if (!isLoggedIn) {
    router.navigate(['/events']);
  }

  return of(isLoggedIn); // 👈 retorna Observable<boolean> explícito
};
