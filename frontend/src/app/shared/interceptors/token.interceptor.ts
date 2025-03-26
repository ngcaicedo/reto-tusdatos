// token.interceptor.ts
import { HttpInterceptorFn } from '@angular/common/http';
import { HttpRequest, HttpHandlerFn, HttpEvent } from '@angular/common/http';
import { finalize, Observable } from 'rxjs';
import { LoadingService } from './loading.service';
import { inject } from '@angular/core';

export const tokenInterceptor: HttpInterceptorFn = (
  req: HttpRequest<any>,
  next: HttpHandlerFn
): Observable<HttpEvent<any>> => {
  const token = sessionStorage.getItem('token');
  const loadingService = inject(LoadingService);

  const excludedUrls = [
    '/auth/login',
    '/users/register/assistant',
    '/events/events',
  ];

  const isExcluded = excludedUrls.some((url) => req.url.includes(url));

  loadingService.show();

  if (token && !isExcluded) {
    const authReq = req.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`,
      },
    });
    return next(authReq).pipe(
      finalize(() => {
        loadingService.hide();
      })
    );
  }

  return next(req).pipe(
    finalize(() => {
      loadingService.hide();
    })
  );
};
