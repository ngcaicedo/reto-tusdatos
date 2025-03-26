import { TestBed } from '@angular/core/testing';
import { CanActivateFn, Router } from '@angular/router';
import { authGuard } from './auth.guard';
import { AuthStateService } from '../states/auth-state.service';
import { Observable } from 'rxjs';

describe('authGuard (Observable)', () => {
  let authServiceMock: any;
  let routerMock: any;

  beforeEach(() => {
    authServiceMock = {
      isLoggedIn: jasmine.createSpy(),
    };

    routerMock = {
      navigate: jasmine.createSpy('navigate'),
    };

    TestBed.configureTestingModule({
      providers: [
        { provide: AuthStateService, useValue: authServiceMock },
        { provide: Router, useValue: routerMock },
      ],
    });
  });

  const executeGuard = (...params: Parameters<CanActivateFn>): Observable<boolean> =>
    TestBed.runInInjectionContext(() => authGuard(...params)) as Observable<boolean>;  

  it('should return true if the user is authenticated', (done) => {
    authServiceMock.isLoggedIn.and.returnValue(true);

    executeGuard({} as any, {} as any).subscribe(result => {
      expect(result).toBeTrue();
      expect(routerMock.navigate).not.toHaveBeenCalled();
      done();
    });
  });

  it('should return false and navigate to events if not authenticated', (done) => {
    authServiceMock.isLoggedIn.and.returnValue(false);

    executeGuard({} as any, {} as any).subscribe(result => {
      expect(result).toBeFalse();
      expect(routerMock.navigate).toHaveBeenCalledWith(['/events']);
      done();
    });
  });
});
