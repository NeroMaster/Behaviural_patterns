from chain.support import Support
from chain.support_type import SupportType
from entity.request import Request

class RefundLine(Support):
    def _get_assigned_type(self):
        return SupportType.REFUND
    
    def process(self, request: Request):
        print(f"Request from {request.get_name()} accepted on Refund Line!")

        if self._get_assigned_type() is not request.get_type():
            print(f"Request from {request.get_name()} passed on next node of support chain!")
            return self._pass(request)
        
        print(f"Request from {request.get_name()} successfully completed on Refund Line!")
        return True