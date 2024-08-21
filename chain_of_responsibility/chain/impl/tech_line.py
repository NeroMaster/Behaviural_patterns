from chain.support import Support
from chain.support_type import SupportType
from entity.request import Request

class TechLine(Support):
    def _get_assigned_type(self):
        return SupportType.TECH
    
    def process(self, request: Request):
        print(f"Request from {request.get_name()} accepted on Tech Line!")

        if self._get_assigned_type() is not request.get_type():
            print(f"Request from {request.get_name()} passed on next node of support chain!")
            return self._pass(request)
        
        print(f"Request from {request.get_name()} successfully completed on Tech Line!")
        return True