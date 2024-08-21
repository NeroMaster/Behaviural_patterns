from listener.impl.server_is_dead_listener import ServerIsDeadListener
from listener.impl.server_timeout_listener import ServerTimeoutListener
from domain.incident import Incident
from domain.incident_type import IncidentType
from incident_manager import IncidentManager

BLOCK_DELIMETR = "\n--\n"

def main():
    first_timeout_subscriber = ServerTimeoutListener()
    second_timeout_subscriber = ServerTimeoutListener()
    first_is_dead_subscriber = ServerIsDeadListener()

    manager:IncidentManager = IncidentManager()
    manager.subscribe(first_timeout_subscriber)
    manager.subscribe(second_timeout_subscriber)
    manager.subscribe(first_is_dead_subscriber)

    server_is_dead = Incident(
        IncidentType.SERVER_IS_DEAD,
        "It`s dead"
    )
    manager.notify(server_is_dead)
    print(BLOCK_DELIMETR)

    timeout_incident = Incident(
        IncidentType.SERVER_TIMEOUT,
        "First timeout"
    )
    manager.notify(timeout_incident)
    print(BLOCK_DELIMETR)

    manager.ubsubscribe(second_timeout_subscriber)
    timeout_incident = Incident(
        IncidentType.SERVER_TIMEOUT,
        "Second timeout"
    )
    manager.notify(timeout_incident)
    print(BLOCK_DELIMETR)


if __name__ == "__main__":
    main()