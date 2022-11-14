from django.middleware.cache import UpdateCacheMiddleware, FetchFromCacheMiddleware


class FetchFromCacheResetCacheMiddleware(FetchFromCacheMiddleware):
    def process_request(self, request):
        if self.cache.delete(request.path):
            request._cache_update_cache = True
            return None
        return super().process_request(request)


class UpdateCaheWithChangeObject(UpdateCacheMiddleware):
    def process_response(self, request, response):
        return super().process_response(request, response)
