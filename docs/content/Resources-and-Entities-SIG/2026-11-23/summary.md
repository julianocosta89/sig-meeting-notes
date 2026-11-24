## Key Topics
- **Disabling identifying resource attributes:** Jan Korona raised the problem of a user disabling a resource attribute that an enabled entity needs as its mandatory identifier. He proposed either validating at config load and throwing an error (a breaking change for existing definitions) or giving entity settings precedence and logging a warning.
- **Config model:** Each collector component has a metadata YAML file defining its telemetry, including resource attributes and entities that reference them. Users can currently enable or disable attributes and entities individually.
- **Relationship conflicts:** Disabling an entity that another entity depends on raises the question of whether to disable both, remove the relationship, or raise a validation error.
- **Possible future simplification:** Controlling attributes only at the entity level was mentioned as a later step, not for now.
- **Deferred decision:** Nathan Smith noted the group lacked enough participants for a substantive discussion, so the topic was postponed to the next meeting.

## Action Items
- Jan Korona to raise the identifying-attribute and relationship questions again at the next SIG meeting.
- Jan Korona to possibly open a GitHub issue so the discussion can continue offline.
- Nathan Smith to record the topic for the next meeting agenda.
- Josh (absent) to review the recording and share his opinions.
- Other attendees to think about the proposed options before the next meeting.

## Participants
Nathan Smith, Jan Korona
