from Products.CMFPlone.PloneBatch import Batch
from Products.Five import BrowserView


class FilteredBatchView(BrowserView):

    def batch(self, folder_view, **kwargs):
        kwargs.setdefault('exclude_from_nav', False)
        results = folder_view.results(**kwargs)
        batch = Batch(
            results,
            size=folder_view.b_size,
            start=folder_view.b_start,
            orphan=1
        )
        return batch
