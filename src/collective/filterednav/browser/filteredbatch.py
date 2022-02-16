from Products.CMFPlone.PloneBatch import Batch
from Products.Five import BrowserView

ARBITRARY_BATCH_SIZE = 2000

class FilteredBatchView(BrowserView):

    def batch(self, folder_view, **kwargs):
        kwargs.setdefault('b_size', ARBITRARY_BATCH_SIZE)
        results = folder_view.results(**kwargs)
        results = [r for r in results if not r.exclude_from_nav]
        batch = Batch(
            results,
            size=ARBITRARY_BATCH_SIZE,
            start=folder_view.b_start,
            orphan=1
        )
        return batch
