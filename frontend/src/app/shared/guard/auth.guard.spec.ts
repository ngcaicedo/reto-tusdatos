import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { authGuard } from './auth.guard';
import { of } from 'rxjs';

describe('authGuard', () => {
  let authServiceMock: any;
  let routerMock: any;

  beforeEach(() => {
    authServiceMock = {
      isAuthenticated$: of(true),
    };

    routerMock = {
      navigate: jasmine.createSpy('navigate'),
    };
    TestBed.configureTestingModule({
      providers: [
        { provide: 'AuthService', useValue: authServiceMock },
        { provide: 'Router', useValue: routerMock },
      ],
    });
  });

  const executeGuard: CanActivateFn = (...guardParameters) =>
    TestBed.runInInjectionContext(() => authGuard(...guardParameters));

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });

  
  it('should return true if the user is authenticated', (done) => {
    authServiceMock.isAuthenticated$ = of(true);

    executeGuard({} as any, {} as any).subscribe(result => {
      expect(result).toBe(true);
      done();
    });
  });

  it('should return false if the user is not authenticated', (done) => {
    authServiceMock.isAuthenticated$ = of(false);

    executeGuard({} as any, {} as any).subscribe(result => {
      expect(result).toBe(false);
      expect(routerMock.navigate).toHaveBeenCalledWith(['/login']);
      done();
    });
  });


});
