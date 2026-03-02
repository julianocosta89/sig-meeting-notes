## Meeting Notes

### Attendees
- Przemek Delewski (Quesma); **Facilitator**
- Kemal Akkoyun (Datadog)
- Huxing Zhang(Alibaba)
- Yang Yi(Alibaba)
- Ziming Liu(Alibaba)
- Xabier Martinez (Cabify)
- Haibin Zhang(Alibaba)

### Agenda
- Discussion on instrumentation pattern
  - Removing the premature abstraction
  - Flexible way provide instrumentation
- **CONSENSUS**:
  - This repo will eventually ONLY be responsible for injector code
  - We will try to enable other instrumentation libraries as much as possible in their own repos or modules
  - We will provide separate official repo for instrumentation
