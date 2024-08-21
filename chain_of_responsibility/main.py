from chain.support import Support
from chain.support_type import SupportType
from chain.impl.first_line import FirstLine
from chain.impl.refund_line import RefundLine
from chain.impl.tech_line import TechLine
from entity.request import Request

BLOCK_DELIMETR = "\n--\n"

def main():
    first_line: Support = FirstLine()
    tech_line: Support = TechLine()
    refund_line: Support = RefundLine()

    head: Support = Support.link(first_line, tech_line, refund_line)
    print(BLOCK_DELIMETR)

    assistant_request: Request = Request(
        name="SomebodyForAssistance",
        support_type=SupportType.ASSISTANCE,
        description="Need somebody (Help) not just anybody (Help) you know I need someone, help"
    )
    head.process(assistant_request)
    print(BLOCK_DELIMETR)

    assistant_request: Request = Request(
        name="SomebodyForTech",
        support_type=SupportType.TECH,
        description="I pressed the button and it exploded!"
    )
    head.process(assistant_request)
    print(BLOCK_DELIMETR)

    assistant_request: Request = Request(
        name="SomebodyForRefund",
        support_type=SupportType.REFUND,
        description="Give me my money!"
    )
    head.process(assistant_request)
    print(BLOCK_DELIMETR)

    assistant_request: Request = Request(
        name="SomebodyWithFeedback",
        support_type=SupportType.FEEDBACK,
        description="Such wow! Many cool!"
    )
    head.process(assistant_request)
    print(BLOCK_DELIMETR)



if __name__ == "__main__":
    main()